#!/usr/bin/env python3
# General-purpose KRACH ratings calculator, based on:
#   Bradley-Terry Model: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
#   http://elynah.com/tbrw/tbrw.cgi?krach
# See readme.md for more details.

import sys
import logging
import datetime
import dataclasses
import math
import enum
import copy

#----------------------------------------------------------------------------
class ScaleMethod(enum.Enum):
    NONE   = 1  # No scaling, report raw floating point values.
    AUTO   = 2  # Repeatedly mutiple all ratings by 10 until all are > 0.
    FACTOR = 3  # Multiply all ratings by 'scaleFactor'.
    RANGE  = 4  # Scale ratings logarithically to range [0, scaleFactor].

#----------------------------------------------------------------------------
@dataclasses.dataclass
class Options:
    # Options to determine when to stop recursing through the KRACH algorithm.
    maxIterations:     int   = 1000       # max number of loops
    maxRatingsDiff:    float = 0.00001    # max diff between two runs that is considered "equal"

    # Options that control how shootout wins/losses and ties are weighted in the ratings
    overtimeWinValue:  float = 1.00       # loss value is (1.0 - winValue)
    shootoutWinValue:  float = 1.00       # loss value is (1.0 - winValue)
    tieValue:          float = 0.50
    alphaValue:        float = 0.50
    bonusPoints:       float = 0.00

    # Used to 'regularize' teams with undefeated records. There are two different methods that
    # can be used, each with their own weight
    fakeTies:          int   = 0
    alphaGames:        int   = 0

    # Explicit list of teams to remove from the final rankings
    filteredTeams:     list  = dataclasses.field(default_factory=lambda: [])

    # Remove any teams from the final rankings that have not played this many games.
    # A value of 0 will include all teams regardless of games played.
    minGamesPlayed:    int   = 0

    # The core algorithm generates ratings that are small floats < 1.0.  These
    # determines how the values are scaled for the final output.
    scaleMethod:       ScaleMethod = ScaleMethod.AUTO
    scaleFactor:       int   = 0

    def dict(self):
        return {
            "Max Iterations"      : "{}".format(self.maxIterations),
            "Max Ratings Diff"    : "{}".format(self.maxRatingsDiff),
            "Overtime Win/Loss"   : "{:3.2f} / {:3.2f}".format(self.overtimeWinValue, (1.0 - self.overtimeWinValue)),
            "Shootout Win/Loss"   : "{:3.2f} / {:3.2f}".format(self.shootoutWinValue, (1.0 - self.shootoutWinValue)),
            "Tie Value"           : "{:3.2f}".format(self.tieValue),
            "Alpha Value"         : "{:3.2f}".format(self.alphaValue),
            "Bonus Points"        : "{:3.2f}".format(self.bonusPoints),
            "Fake Ties"           : "{}".format(self.fakeTies),
            "Alpha Games"         : "{}".format(self.alphaGames),
            "Ignore teams"        : "{}".format(",".join(self.filteredTeams)),
            "Min Games Played"    : "{}".format(self.minGamesPlayed),
            # TODO
        }

    def __str__(self):
        return '\n'.join([""] + [ "  {:<20} : {}".format(k, v) for k,v in self.dict().items() ])

#----------------------------------------------------------------------------
def removeTeam(ratings, team):
    if team in ratings:
        ratings.pop(team)

#----------------------------------------------------------------------------
def filterTeams(options, ledger, ratings):
    # use intermediate mapping to allow ignoring case in filtered teams
    icaseTeams = { name.lower() : name for name in ratings.keys() }
    # remove teams explicitly called out
    for team in options.filteredTeams:
        camelTeam = icaseTeams.get(team.lower(), None)
        if camelTeam:
            removeTeam(ratings, camelTeam)

    for name,team in ledger.teams.items():
        if team.record.played < options.minGamesPlayed:
            removeTeam(ratings, name)

#----------------------------------------------------------------------------
def scaleRatings(options, ratings, sosAll):
    def _scale(factor, rating):
        return int(factor * rating + 0.5)

    def _scaleAll(factor):
        for team in ratings:
            ratings[team] = _scale(factor, ratings[team])
            sosAll[team]  = _scale(factor, sosAll[team])

    def _scaleNone():
        pass

    def _scaleAuto():
        # brute force search for a scaling factor that will
        # allow all ratings to be displayed as integers
        scaleFactor = 1
        for rating in ratings.values():
            while rating and _scale(scaleFactor, rating) <= 0:
                scaleFactor *= 10
        # Also scale such that the max value has at least 4 digits
        while len(str(_scale(scaleFactor, max(ratings.values())))) < 4:
            scaleFactor *= 10
        logging.debug("Auto-scaling all ratings by {}".format(scaleFactor))
        _scaleAll(scaleFactor)

    def _scaleFactor():
        logging.debug("Hard scaling all ratings by {}".format(options.scaleFactor))
        _scaleAll(options.scaleFactor)

    def _scaleRange():
        logging.debug("Scaling all ratings to range 0-{}".format(options.scaleFactor))
        for team in ratings:
            ratings[team] = int(options.scaleFactor * math.log1p(1000 * ratings[team]) / math.log1p(1000) + 0.5)
            sosAll[team]  = int(options.scaleFactor * math.log1p(1000 * sosAll[team])  / math.log1p(1000) + 0.5)

    methods = {
        ScaleMethod.NONE   : _scaleNone,
        ScaleMethod.AUTO   : _scaleAuto,
        ScaleMethod.FACTOR : _scaleFactor,
        ScaleMethod.RANGE  : _scaleRange,
    }
    method = methods.get(options.scaleMethod, None)
    if not method:
        raise RuntimeError("Failed to map scaling method to function")
    method()

#----------------------------------------------------------------------------
@dataclasses.dataclass
class Record:
    played:      int = 0
    wins:        int = 0
    losses:      int = 0
    otWins:      int = 0
    otLosses:    int = 0
    soWins:      int = 0
    soLosses:    int = 0
    ties:        int = 0
    alphaWins:   int = 0
    alphaLosses: int = 0

    def __str__(self):
        return f"{self.wins:>2}-{self.losses:>2}-{self.ties:>2}   {self.otWins:>2}  {self.otLosses:>2}"

    def addWin(self):
        self.played += 1
        self.wins += 1

    def addLoss(self):
        self.played += 1
        self.losses += 1

    def addOvertimeWin(self):
        self.played += 1
        self.otWins += 1

    def addOvertimeLoss(self):
        self.played += 1
        self.otLosses += 1

    def addShootoutWin(self):
        self.played += 1
        self.soWins += 1

    def addShootoutLoss(self):
        self.played += 1
        self.soLosses += 1

    def addTie(self):
        self.played += 1
        self.ties += 1

    def addAlphaWin(self):
        self.played += 1
        self.alphaWins += 1

    def addAlphaLoss(self):
        self.played += 1
        self.alphaLosses += 1

    def winPoints(self, options):
        return self.wins \
            + (self.otWins      * options.overtimeWinValue) \
            + (self.otLosses    * (1.0 - options.overtimeWinValue)) \
            + (self.soWins      * options.shootoutWinValue) \
            + (self.soLosses    * (1.0 - options.shootoutWinValue)) \
            + (self.ties        * options.tieValue) \
            + (self.alphaWins   * options.alphaValue) \
            + (self.alphaLosses * (1.0 - options.alphaValue)) \
            + options.bonusPoints

#----------------------------------------------------------------------------
class Team:
    def __init__(self, id):
        self.id = id
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

    def addOvertimeWin(self, opponent):
        self.record.addOvertimeWin()
        self.addOpponent(opponent)
        self.matchups[opponent].addOvertimeWin()

    def addOvertimeLoss(self, opponent):
        self.record.addOvertimeLoss()
        self.addOpponent(opponent)
        self.matchups[opponent].addOvertimeLoss()

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

    def addAlphaWin(self, opponent):
        self.record.addAlphaWin()
        self.addOpponent(opponent)
        self.matchups[opponent].addAlphaWin()

    def addAlphaLoss(self, opponent):
        self.record.addAlphaLoss()
        self.addOpponent(opponent)
        self.matchups[opponent].addAlphaLoss()

#----------------------------------------------------------------------------
# Tracks all teams and their game results.
class Ledger:
    def __init__(self, season, dateCutoff):
        self.season = season
        self.dateCutoff = dateCutoff
        self.teams = dict()
        self.oldestGame = None
        self.newestGame = None

    def isValid(self, date):
        return date <= self.dateCutoff

    def addGame(self, date, winner, loser):
        if self.isValid(date):
            self.recordDate(date)
            self.teams[winner].addWin(loser)
            self.teams[loser ].addLoss(winner)

    def addOvertime(self, date, winner, loser):
        if self.isValid(date):
            self.recordDate(date)
            self.teams[winner].addOvertimeWin(loser)
            self.teams[loser ].addOvertimeLoss(winner)

    def addShootout(self, date, winner, loser):
        if self.isValid(date):
            self.recordDate(date)
            self.teams[winner].addShootoutWin(loser)
            self.teams[loser ].addShootoutLoss(winner)

    def addTie(self, date, team1, team2):
        if self.isValid(date):
            self.recordDate(date)
            self.teams[team1].addTie(team2)
            self.teams[team2].addTie(team1)

    def addAlpha(self, date, fakeTeam, realTeam):
        if self.isValid(date):
            self.recordDate(date)
            self.teams[realTeam].addAlphaWin(fakeTeam)
            self.teams[fakeTeam].addAlphaLoss(realTeam)

    def addTeam(self, name, id):
        if not name in self.teams:
            self.teams[name] = Team(id)

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
    sos:       int   = 100  # strength-of-schedule
    expected:  float = 0.0  # Predicted number of wins based on KRACH ratings
    diff:      float = 0.0  # Difference between expected and actual number of wins (absolute)
    winPoints: float = 0.0  # Win points, including shootout and tie values
    matchupFactor: float = 0.0 # Sum of all matchup factors for this team
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
            loop += 1
            updated = self.calculateAll(ledger, ratings)
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
        for name in sorted(ledger.teams):
            updated[name] = self.calculate(ledger, ratings, name)
        return self.normalize(updated)

    #----------------------------------------------------------------------------
    # Calculates an updated rating for a single team, using:
    #   Ki = Vi / ( ∑j Nij / (Ki + Kj) )
    def calculate(self, ledger, ratings, i):
        winPoints = ledger.teams[i].record.winPoints(self.options)
        matchupFactor = self.calculateMatchupFactor(ledger, ratings, i)
        return winPoints / matchupFactor

    #----------------------------------------------------------------------------
    # Calculate: ∑j (Wij + Wji) / (Ki + Kj)
    # Different sources have the numerator as Nij versus (Wij + Wji). For most
    # scenarios every game is worth 1.0 points total, making the two forms identical.
    # But the AHF assigns 0.85 win points for their 'regularization' tie games,
    # breaking the equivalance.
    def calculateMatchupFactor(self, ledger, ratings, i):
        myTeam = ledger.teams[i]
        sumOfMatchups = 0.0
        # iterate across all teams we've played
        for j in myTeam.matchups:
            wij = myTeam.matchups[j].winPoints(self.options)
            wji = ledger.teams[j].matchups[i].winPoints(self.options)
            sumOfMatchups += (wij + wji) / (ratings[i] + ratings[j])
        return sumOfMatchups

    #----------------------------------------------------------------------------
    def strengthOfScheduleAll(self, ledger, ratings):
        return { team : self.strengthOfSchedule(ledger, ratings, team) for team in ledger.teams }

    #----------------------------------------------------------------------------
    def strengthOfSchedule(self, ledger, ratings, myTeam):
        total = 0.0
        for oppTeam in ledger.teams[myTeam].matchups:
            total += ledger.teams[myTeam].matchups[oppTeam].played * ratings[oppTeam]
        return total / ledger.teams[myTeam].record.played

    #----------------------------------------------------------------------------
    def normalize(self, ratings):
        total = sum(ratings.values())
        return { name : value / total for name,value in ratings.items() }

    #----------------------------------------------------------------------------
    def areRatingsEqual(self, original, updated):
        return sum(abs(original[team] - updated[team]) for team in original) < self.options.maxRatingsDiff

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

    if not fakeTeam in options.filteredTeams:
        options.filteredTeams.append(fakeTeam)

    for _ in range(options.fakeTies):
        ledger.addTeam(fakeTeam, None)
        for realTeam in ledger.teams:
            if realTeam != fakeTeam:
                ledger.addAlpha(ledger.oldestGame, fakeTeam, realTeam)

    for _ in range(options.alphaGames):
        ledger.addTeam(fakeTeam, None)
        for realTeam in ledger.teams:
            if realTeam != fakeTeam:
                ledger.addAlpha(ledger.oldestGame, fakeTeam, realTeam)

#----------------------------------------------------------------------------
def generate(options, ledger):

    # Make a copy of the ledger to avoid polluting ledger with any adjustments
    # made by the algorithm (e.g. adding fake ties)
    ledger = copy.deepcopy(ledger)

    addFakeTies(options, ledger)
    krach = KRACH(options)
    ratings = krach.run(ledger)

    # Calculate final strength of schedules
    sosAll = krach.strengthOfScheduleAll(ledger, ratings)

    # Validate ratings by converting back to expected number of wins
    expectedWins = krach.expectedWinsAll(ledger, ratings)

    # Done calculations; remove any filtered teams
    filterTeams(options, ledger, ratings)

    odds = krach.calculateOdds(ratings)

    # Scaling will lose precision, so do the sorting now with most precise values.
    rankings = [ x[0] for x in sorted(ratings.items(), key=lambda kv: kv[1], reverse = True)]

    # scale up so all values are integers
    scaleRatings(options, ratings, sosAll)

    # And finally, build a list of Rating() objects for easy consumption by caller
    def _rating(name, value):
        # difference between number of expected wins and actual wins
        # negative differerence indicates the KRACH rating is too low, likewise a
        # positive difference indicates rating is too high.
        diff = expectedWins[name] - ledger.teams[name].record.winPoints(options)
        return Rating(name, value, sosAll[name], expectedWins[name], diff, 
                      ledger.teams[name].record.winPoints(options), 
                      0,
                      odds[name])

    return [ _rating(name, ratings[name]) for name in rankings ]

