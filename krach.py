#!/usr/bin/env python3
# General-purpose KRACH ratings calculator, based on:
#   Bradley-Terry Model: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
#   http://elynah.com/tbrw/tbrw.cgi?krach
# See readme.md for more details.

import sys
import logging
import datetime
import dataclasses
from enum import Enum

#----------------------------------------------------------------------------
# Method to calculate the KRACH rating
class KrachMethod(Enum):
    BRADLEY_TERRY = 1
    WIN_LOSS      = 2

#----------------------------------------------------------------------------
# See KRACH::strengthOfSchedule() for details
class SoSMethod(Enum):
    AVERAGE = 1
    DBAKER  = 2
    TBRW    = 3

#----------------------------------------------------------------------------
@dataclasses.dataclass
class Options:
    inputFile:         str   = ""
    outputFile:        str   = ""

    divisionName:      str   = ""

    # Algorithm used for calculating the KRACH rating
    krachMethod:       KrachMethod = KrachMethod.BRADLEY_TERRY

    # Method used to calculate strength-of-schedule
    sosMethod:         SoSMethod = SoSMethod.AVERAGE

    # Options to determine when to stop recursing through the KRACH algorithm.
    maxIterations:     int   = 100       # max number of loops
    maxRatingsDiff:    float = 0.00001  # max diff between two runs that is considered "equal"

    # Options that control how shootout wins/losses and ties are weighted in the rankings
    shootoutWinValue:  float = 1.00  # loss value is (1.0 - winValue)
    tieValue:          float = 0.50

    # Option to control whether teams are given fake ties, a method some implementations
    # use to deal with undefeated teams.
    fakeTies:          int   = 0

    # Showcases may include guest teams, that play valid games that count toward
    # KRACH ratings, but are not included in the final standings. These options
    # are for filtering out these teams.
    filteredTeams:     list  = dataclasses.field(default_factory=lambda: []) # Explicit list of teams
    minGamesPlayed:    int   = 0 # ignore teams with less than the min number of games

    # Option to ignore games after a specific date cutoff. This allows using
    # the latest score results to recreate the KRACH ratings from previous weeks.
    dateCutoff:        str   = dataclasses.field(default_factory=lambda: datetime.date.today())

    # Enable test mode, which iterates through a set of pre-configured settings
    # to try and find the 'best' set of options.
    test:              bool  = False

    def dict(self):
        return {
            "KRACH Method"        : "{}".format(self.krachMethod.name),
            "SoS Method"          : "{}".format(self.sosMethod.name),
            "Max Iterations"      : "{}".format(self.maxIterations),
            "Max Ratings Diff"    : "{}".format(self.maxRatingsDiff),
            "Shootout Win Value"  : "{:3.2f}".format(self.shootoutWinValue),
            "Shootout Loss Value" : "{:3.2f}".format(1.0 - self.shootoutWinValue),
            "Tie Value"           : "{:3.2f}".format(self.tieValue),
            "Fake Ties"           : "{}".format(self.fakeTies),
            "Ignore teams"        : "{}".format(",".join(self.filteredTeams)),
            "Min Games Played"    : "{}".format(self.minGamesPlayed),
            "Date Cutoff"         : "{}".format(self.dateCutoff),
        }

    def __str__(self):
        return '\n'.join([""] + [ "  {:<20} : {}".format(k, v) for k,v in self.dict().items() ])

#----------------------------------------------------------------------------
def removeTeam(ratings, team):
    if team in ratings:
        ratings.pop(team)

#----------------------------------------------------------------------------
def filterTeams(options, ledger, ratings):
    # remove teams explicitly called out
    for team in options.filteredTeams:
        removeTeam(ratings, team)

    for name,team in ledger.teams.items():
        if team.record.played < options.minGamesPlayed:
            removeTeam(ratings, name)

#----------------------------------------------------------------------------
def scaleRankings(ratings, sosAll):
    # brute force search for a scaling factor that will
    # allow all ratings to be displayed as integers
    scaleFactor = 1
    for rating in ratings.values():
        while rating and int(rating * scaleFactor) <= 0:
            scaleFactor *= 10

    # Also thumb the scale so that the max value has 4 digits
    while len(str(int(max(ratings.values()) * scaleFactor + 0.5))) < 4:
        scaleFactor *= 10

    logging.debug("Scaling all ratings by {}".format(scaleFactor))

    for team in ratings:
        ratings[team] = int(ratings[team] * scaleFactor + 0.5)

    for team in sosAll:
        sosAll[team] = int(sosAll[team] * scaleFactor + 0.5)

#----------------------------------------------------------------------------
@dataclasses.dataclass
class Record:
    played:   int = 0
    wins:     int = 0
    losses:   int = 0
    soWins:   int = 0
    soLosses: int = 0
    ties:     int = 0

    def __str__(self):
        return f"{self.wins:>2}-{self.losses:>2}-{self.soWins:>2}-{self.soLosses:>2}-{self.ties:>2}"

    def addWin(self):
        self.played += 1
        self.wins += 1

    def addLoss(self):
        self.played += 1
        self.losses += 1

    def addShootoutWin(self):
        self.played += 1
        self.soWins += 1

    def addShootoutLoss(self):
        self.played += 1
        self.soLosses += 1

    def addTie(self):
        self.played += 1
        self.ties += 1

    def winPoints(self, options):
        return self.wins \
            + (self.soWins   * options.shootoutWinValue) \
            + (self.soLosses * (1.0 - options.shootoutWinValue)) \
            + (self.ties     * options.tieValue)

    def lossPoints(self, options):
        return self.played - self.winPoints(options)

#----------------------------------------------------------------------------
class Team:
    def __init__(self):
        self.matchups = dict()
        self.record = Record()

    def addOpponent(self, opponent):
        if opponent not in self.matchups:
            self.matchups[opponent] = Record()

    def addWin(self, opponent):
        self.record.addWin()
        self.addOpponent(opponent)
        self.matchups[opponent].addWin()

    def addLoss(self, opponent):
        self.record.addLoss()
        self.addOpponent(opponent)
        self.matchups[opponent].addLoss()

    def addShootoutWin(self, opponent):
        self.record.addShootoutWin()
        self.addOpponent(opponent)
        self.matchups[opponent].addShootoutWin()

    def addShootoutLoss(self, opponent):
        self.record.addShootoutLoss()
        self.addOpponent(opponent)
        self.matchups[opponent].addShootoutLoss()

    def addTie(self, opponent):
        self.record.addTie()
        self.addOpponent(opponent)
        self.matchups[opponent].addTie()

#----------------------------------------------------------------------------
# Tracks all teams and their game results.
class Ledger:
    def __init__(self, dateCutoff):
        self.dateCutoff = dateCutoff
        self.teams = dict()
        self.oldestGame = None
        self.newestGame = None

    def isValid(self, date):
        return date <= self.dateCutoff

    def addGame(self, date, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        if self.isValid(date):
            self.recordDate(date)
            self.teams[winner].addWin(loser)
            self.teams[loser ].addLoss(winner)

    def addShootout(self, date, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        if self.isValid(date):
            self.recordDate(date)
            self.teams[winner].addShootoutWin(loser)
            self.teams[loser ].addShootoutLoss(winner)

    def addTie(self, date, team1, team2):
        self.addTeam(team1)
        self.addTeam(team2)
        if self.isValid(date):
            self.recordDate(date)
            self.teams[team1].addTie(team2)
            self.teams[team2].addTie(team1)

    def addTeam(self, team):
        if not team in self.teams:
            self.teams[team] = Team()

    def recordDate(self, date):
        if not self.oldestGame or date < self.oldestGame:
            self.oldestGame = date
        if not self.newestGame or date > self.newestGame:
            self.newestGame = date

#----------------------------------------------------------------------------
@dataclasses.dataclass
class Rating:
    name:      str = ""     # Name of the team, used for display and lookup in ledger
    value:     int   = 100  # KRACH rating value
    sos:       float = 100  # strength-of-schedule
    expected:  float = 0.0  # Predicted number of wins based on KRACH ratings
    diff:      float = 0.0  # Difference between expected and actual number of wins (absolute)
    odds:      dict  = dataclasses.field(default_factory=lambda: dict())

#----------------------------------------------------------------------------
# Implements the KRACH algorithm.
class KRACH:
    def __init__(self, options):
        self.options = options

    #----------------------------------------------------------------------------
    # Execute the KRACH algorithm until the ratings converge, or
    # we hit our max iteration limit.
    def run(self, ledger) -> dict[str, float]:
        # Initial guesses at the krach ratings; doesn't really matter as we'll iterate
        # until we get to the correct values.
        ratings = { k : 1.0 for k in ledger.teams.keys() }

        loop = 0
        while (self.options.maxIterations <= 0) or (self.options.maxIterations > 0 and loop < self.options.maxIterations):
            updated = self.calculateAll(ledger, ratings)
            loop += 1
            if self.areRatingsEqual(ratings, updated):
                logging.debug("Convergence to final results took {} interations".format(loop))
                return updated
            ratings = updated

        logging.debug("Failed to reach convergence after {} interations".format(loop))
        return ratings

    #----------------------------------------------------------------------------
    # Calculate new KRACH ratings for all teams
    def calculateAll(self, ledger, ratings):
        updated = dict()
        for name in ledger.teams:
            updated[name] = self.calculate(ledger, ratings, name)
        return self.normalize(updated)

    #----------------------------------------------------------------------------
    def calculate(self, ledger, ratings, i):
        methods = {
            KrachMethod.BRADLEY_TERRY : self.calculateBradleyTerry,
            KrachMethod.WIN_LOSS      : self.calculateWinLoss,
        }
        method = methods.get(self.options.krachMethod, None)
        if not method:
            raise RuntimeError("Failed to map KRACH method to function")
        return method(ledger, ratings, i)

    #----------------------------------------------------------------------------
    # Calculates an updated rating for a single team, using:
    #   Ki = Vi / ( ∑j Nij / (Ki + Kj) )
    def calculateBradleyTerry(self, ledger, ratings, i):
        return ledger.teams[i].record.winPoints(self.options) / self.calculateMatchupFactor(ledger, ratings, i)

    #----------------------------------------------------------------------------
    # Calculate: ∑j Nij / (Ki + Kj)
    def calculateMatchupFactor(self, ledger, ratings, i):
        myTeam = ledger.teams[i]
        sumOfMatchups = 0.0
        # iterate across all teams we've played
        for j in myTeam.matchups:
            gp = myTeam.matchups[j].played
            sumOfMatchups += (gp) / (ratings[i] + ratings[j])
        return sumOfMatchups

    #----------------------------------------------------------------------------
    # Calculate rating based on simple (WINS / LOSSES) / SOS
    def calculateWinLoss(self, ledger, ratings, i):
        wins = ledger.teams[i].record.winPoints(self.options)
        losses = ledger.teams[i].record.lossPoints(self.options)
        if losses == 0.0:
            losses = 0.1
        return (wins / losses) * self.strengthOfSchedule(ledger, ratings, i)

    #----------------------------------------------------------------------------
    def strengthOfScheduleAll(self, ledger, ratings):
        return { team : self.strengthOfSchedule(ledger, ratings, team) for team in ledger.teams }

    #----------------------------------------------------------------------------
    def strengthOfSchedule(self, ledger, ratings, myTeam):
        methods = {
            SoSMethod.AVERAGE : self.sosAverage,
            SoSMethod.DBAKER  : self.sosDanBaker,
            SoSMethod.TBRW    : self.sosTbrw,
        }
        method = methods.get(self.options.sosMethod, None)
        if not method:
            raise RuntimeError("Failed to map SOS method to function")
        return method(ledger, ratings, myTeam)

    #----------------------------------------------------------------------------
    # SoS based on the average rating of all opponents played.
    def sosAverage(self, ledger, ratings, myTeam):
        total = 0.0
        for oppTeam in ledger.teams[myTeam].matchups:
            total += ledger.teams[myTeam].matchups[oppTeam].played * ratings[oppTeam]
        return total / ledger.teams[myTeam].record.played

    #----------------------------------------------------------------------------
    # SoS based on the formula provided by Dan Baker's KRACH page at
    # http://dbaker.50webs.com/method.html
    #          ∑ ( Ro / (Ro + Rs))
    #  SoS =  ---------------------
    #          ∑ ( 1  / (Ro + Rs))
    # NOTE: this does NOT produce viable results; the SoS values end up
    # being proportional to the team's own KRACH rating, not the opponents.
    # FYI: I tried tweaking this, thinking that maybe the sum was meant to be
    # over the entire fraction, but that ended up being just the average.
    def sosDanBaker(self, ledger, ratings, myTeam):
        rs = ratings[myTeam]
        top = 0.0
        bot = 0.0
        for oppTeam in ledger.teams[myTeam].matchups:
            gp = ledger.teams[myTeam].matchups[oppTeam].played
            ro = ratings[oppTeam]
            top += gp * ro  / (ro + rs)
            bot += gp * 1.0 / (ro + rs)
        return top / bot

    #----------------------------------------------------------------------------
    # SoS (aka 'weighting factor') as described at TBRW site:
    # http://elynah.com/tbrw/tbrw.cgi?krach
    # Sos is defined as:
    #    ∑j fij * Kj
    # And fij:
    #  fij = [ Nij / (Ki+Kj) ] / [ ∑k Nik / (Ki+Kk) ]
    #
    def sosTbrw(self, ledger, ratings, myTeam):
        rs = ratings[myTeam]
        total = 0.0

        # precalc: ∑k Nik / (Ki+Kk)
        bottomSum = 0.0
        for oppTeam in ledger.teams[myTeam].matchups:
            gp = ledger.teams[myTeam].matchups[oppTeam].played
            ro = ratings[oppTeam]
            bottomSum += (gp / (ro + rs))

        # calc fij and add into the total sum
        for oppTeam in ledger.teams[myTeam].matchups:
            gp = ledger.teams[myTeam].matchups[oppTeam].played
            ro = ratings[oppTeam]
            fij = (gp / (ro + rs)) / bottomSum
            total += ro * fij
        return total

    #----------------------------------------------------------------------------
    def normalize(self, ratings):
        total = sum(ratings.values())
        return { name : value / total for name,value in ratings.items() }

    #----------------------------------------------------------------------------
    def areRatingsEqual(self, original, updated):
        return all( abs(original[team] - updated[team]) <= self.options.maxRatingsDiff for team in original )

    #----------------------------------------------------------------------------
    def expectedWinsAll(self, ledger, ratings):
        return { team : self.expectedWins(ledger, ratings, team) for team in ledger.teams }

    #----------------------------------------------------------------------------
    # Validate KRACH ratings by calculating the expected wins using:
    #    Vi = ∑j Nij*Ki/(Ki+Kj)
    def expectedWins(self, ledger, ratings, myTeam):
        return ratings[myTeam] * self.calculateMatchupFactor(ledger, ratings, myTeam)

    #----------------------------------------------------------------------------
    def calculateOdds(self, ratings):
        return { team : self.calculateTeamOdds(team, ratings) for team in ratings }

    #----------------------------------------------------------------------------
    def calculateTeamOdds(self, team, ratings):
        def _calcOdds(rating1, rating2):
            try:
                return (rating1 / (rating1 + rating2))
            except:
                return float("NaN")

        myRating = ratings[team]
        return { oppTeam : _calcOdds(myRating, oppRating) for oppTeam,oppRating in ratings.items() }

#----------------------------------------------------------------------------
def addFakeTies(options, ledger):
    fakeTeam = "__KRACH_FAKE_TEAM__"

    for _ in range(options.fakeTies):
        if not fakeTeam in options.filteredTeams:
            options.filteredTeams.append(fakeTeam)

        ledger.addTeam(fakeTeam)
        for realTeam in ledger.teams:
            if realTeam != fakeTeam:
                ledger.addTie(ledger.oldestGame, fakeTeam, realTeam)

#----------------------------------------------------------------------------
def generate(options, ledger):
    # Add in any fake game data
    addFakeTies(options, ledger)

    krach = KRACH(options)
    ratings = krach.run(ledger)

    # Calculate final strength of schedules
    sosAll = krach.strengthOfScheduleAll(ledger, ratings)

    # Validate ratings by converting back to expected number of wins
    expectedWins = krach.expectedWinsAll(ledger, ratings)

    # Now that we're done all calculations, remove any ignored teams
    # (such as showcase teams)
    filterTeams(options, ledger, ratings)

    odds = krach.calculateOdds(ratings)

    # scale up so all values are integers
    scaleRankings(ratings, sosAll)

    # sort by self ratings, highest first.
    ratings = sorted(ratings.items(), key=lambda kv: kv[1], reverse = True)

    # And finally, build a list of Rating() objects for easy consumption by caller
    def _rating(name, value):
        # difference between number of expected wins and actual wins
        # negative differerence indicates the KRACH rating is too low, likewise a
        # positive difference indicates rating is too high.
        diff = expectedWins[name] - ledger.teams[name].record.winPoints(options)
        return Rating(name, value, sosAll[name], expectedWins[name], diff, odds[name])
    return [ _rating(name,value) for name,value in ratings ]

