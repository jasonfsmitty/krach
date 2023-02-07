#!/usr/bin/env python3
# General-purpose KRACH ratings calculator, based on:
#   Bradley-Terry Model: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model
#   http://elynah.com/tbrw/tbrw.cgi?krach
# See readme.md for more details.

import sys
import logging
import argparse
import json
import datetime
import dataclasses
import itertools
from enum import Enum

#----------------------------------------------------------------------------
def writeMarkdownTable(f, data, keyTitle="Option", valueTitle="Value"):
    f.write(f"| {keyTitle} | {valueTitle} |\n")
    f.write(f"| :----- | ----: |\n")
    for k,v in data.items():
        f.write(f"| {k} | {v} |\n")
    f.write(f"\n")

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
    maxIterations:     int   = 10000   # max number of loops
    maxRatingsDiff:    float = 0.0001  # max diff between two runs that is considered "equal"

    # Options that control how shootout wins/losses and ties are weighted in the rankings
    shootoutWinValue:  float = 0.50  # loss value is (1.0 - winValue)
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
# AHF specific: each division gets split into subdivisions, with each
# competing in their own playoffs.
SUBDIVISIONS = [
    'Championship',
    'Gold',
    'Silver',
    'Bronze',
]

# Only the top 4 teams of each subdivision compete in the playoffs;
# THe AHF KRACH rankings list other teams as being in the lowest
# subdivision, but this makes it clearer who is in/out of playoff
# contention.
NO_SUBDIVISION = ""

def subdivision(numTeams, rank):
    if numTeams <= 10:
        if rank <=  4: return SUBDIVISIONS[0]
    elif numTeams >= 11 and numTeams <= 14:
        if rank <=  4: return SUBDIVISIONS[0]
        if rank <=  8: return SUBDIVISIONS[1]
    elif numTeams >= 15 and numTeams <= 26:
        if rank <=  4: return SUBDIVISIONS[0]
        if rank <=  8: return SUBDIVISIONS[1]
        if rank <= 12: return SUBDIVISIONS[2]
    else:
        if rank <=  4: return SUBDIVISIONS[0]
        if rank <=  8: return SUBDIVISIONS[1]
        if rank <= 12: return SUBDIVISIONS[2]
        if rank <= 16: return SUBDIVISIONS[3]
    return NO_SUBDIVISION

#----------------------------------------------------------------------------
def scaleRankings(ratings, sosAll):
    # brute force search for a scaling factor that will
    # allow all ratings to be displayed as integers
    scaleFactor = 1
    for rating in ratings.values():
        while rating and int(rating * scaleFactor) <= 0:
            scaleFactor *= 10

    logging.debug("Scaling all ratings by {}".format(scaleFactor))

    for team in ratings:
        ratings[team] = int(ratings[team] * scaleFactor + 0.5)

    for team in sosAll:
        sosAll[team] = int(sosAll[team] * scaleFactor + 0.5)

#----------------------------------------------------------------------------
def showRankings(options, ledger, ratings):
    dividor = "-" * 115
    print(f"Rank KRACH   Subdivision     Team                                     GP  WW-LL-SW-SL-TT    SoS | Predict Diff")
    print(dividor)

    diffTotal = 0.0
    rawTotal = 0.0
    numTeams = len(ratings)
    for rank,rating in enumerate(ratings):
        rank   += 1
        subdiv = subdivision(numTeams, rank)
        team   = rating.name
        value  = rating.value
        gp     = ledger.teams[team].record.played
        record = str(ledger.teams[team].record)
        sos    = rating.sos
        exp    = rating.expected
        diff   = rating.diff
        print(f"{rank:>3} {value:>6} : {subdiv:<13} : {team:<40} {gp:>2}  {record} {sos:>6} | {exp:>5.1f} {diff:>5.1f}")
        rawTotal  += diff
        diffTotal += abs(diff)
    print("")
    diffAvg = diffTotal / numTeams
    rawAvg = rawTotal / numTeams
    print(f"Differences between expected and actual wins:")
    print(f"          ABS    RAW")
    print(f"  Total: {diffTotal:5.2f} {rawTotal:>5.2f}")
    print(f"  Avg  : {diffAvg:5.2f} {rawAvg:>5.2f}")

#----------------------------------------------------------------------------
def writeMarkdownRankings(options, ledger, ratings):

    with open(options.outputFile, "w") as f:
        f.write(f"# {options.divisionName} KRACH Rankings\n")

        lines = [
            ['Rank', 'KRACH', 'Subdivision', 'Team', 'GP',   'W',    'L',    'SOW',  'SOL',  'T',    'SoS', 'Exp Wins', 'Win Diff'],
            ['---:', '---:',  ':---',        ':---', '---:', '---:', '---:', '---:', '---:', '---:', '---:', '---:', '---:'],
        ]
        for line in lines:
            f.write('|'.join(line))
            f.write('\n')

        numTeams = len(ratings)
        for rank,rating in enumerate(ratings):
            rank   += 1
            team   = rating.name
            value  = rating.value
            record = ledger.teams[team].record
            gp     = record.played
            wins   = record.wins
            losses = record.losses
            otw    = record.soWins
            otl    = record.soLosses
            ties   = record.ties
            sos    = rating.sos
            expW   = "{:.1f}".format(rating.expected)
            diff   = "{:.1f}".format(rating.diff)
            columns = [rank, value, subdivision(numTeams, rank), team, gp, wins, losses, otw, otl, ties, sos, expW, diff]
            f.write('|'.join(map(str, columns)))
            f.write('\n')
        f.write('\n')

        # magnitude
        totalDiff = sum(abs(x.diff) for x in ratings)
        avgDiff   = totalDiff / len(ratings)

        totalRaw  = sum(x.diff for x in ratings)
        avgRaw    = totalRaw / len(ratings)

        f.write(f"## Actual vs Expected\n")

        f.write("Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.\n")
        f.write("\n")

        f.write(f"||Absolute|Raw\n")
        f.write(f"|---:|---:|---:\n")
        f.write(f"|Total|{totalDiff:.2f}|{totalRaw:.2f}\n")
        f.write(f"|Avg|{avgDiff:.2f}|{avgRaw:.2f}\n")
        f.write(f"\n")

        f.write("## Generation Details\n")
        f.write("\n")

        f.write("Generated with command line:\n")
        f.write("```\n")
        f.write(" ".join(sys.argv[:]))
        f.write("\n```\n")
        f.write("\n")

        data = {
            "Start Date" : f"{ledger.oldestGame}",
            "End Date"   : f"{ledger.newestGame}",
        }
        data.update(options.dict())
        writeMarkdownTable(f, data)

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
# Read AHF score data into a ledger. This is specific to the JSON format
# provided by the gamesheetstats.com API. To use this script with a different
# data source, you would replace this reader with one specific to your context.
class AhfScoreReader:
    def __init__(self):
        pass

    #----------------------------------------------------------------------------
    def read(self, filename, ledger):
        with open(filename) as f:
            jdata = json.load(f)
            for game in jdata:
                self.readGame(ledger, game['game'])

    #----------------------------------------------------------------------------
    def readGame(self, ledger, game):
        date       = datetime.datetime.strptime(game['date'], "%b %d, %Y").date()
        team1      = game['homeTeam']['name']
        team1score = game['finalScore']['homeGoals']
        team2      = game['visitorTeam']['name']
        team2score = game['finalScore']['visitorGoals']
        shootout   = any(map(lambda x: x['title'] == 'SO', game['scoresByPeriod']))

        winner = team1 if team1score > team2score else team2
        loser  = team2 if team1score > team2score else team1

        if team1score == team2score:
            ledger.addTie(date, team1, team2)
        elif shootout:
            ledger.addShootout(date, winner, loser)
        else:
            ledger.addGame(date, winner, loser)

#----------------------------------------------------------------------------
def addFakeTies(options, ledger):
    fakeTeam = "__AHF_FAKE_TEAM__"
    for _ in range(options.fakeTies):
        if not fakeTeam in options.filteredTeams:
            options.filteredTeams.append(fakeTeam)
            ledger.addTeam(fakeTeam)

        for realTeam in ledger.teams:
            if realTeam != fakeTeam:
                ledger.addTie(ledger.oldestGame, fakeTeam, realTeam)

#----------------------------------------------------------------------------
def parseCommandLine():
    options = Options()
    parser = argparse.ArgumentParser()

    parser.add_argument("--debug",
        action  = 'store_true',
        default = False,
        help    = "Enable extra debug logging")

    parser.add_argument("-n", "--name",
        type    = str,
        default = options.divisionName,
        help    = "Division Name")

    parser.add_argument("--krach",
        metavar = "<method>",
        choices = ["bradley_terry", "win_loss"],
        default = "bradley_terry",
        help    = "Method used to calculate KRACH")

    parser.add_argument("--sos",
        metavar = "<method>",
        choices = ["average", "dbaker", "tbrw"],
        default = "average",
        help    = "Method used to calculate Sos")

    parser.add_argument("-i", "--iterations",
        type    = int,
        default = options.maxIterations,
        help    = "Max iterations of the KRACH algorithm, or 0 for infinite")

    parser.add_argument("-d", "--diff",
        type    = float,
        default = options.maxRatingsDiff,
        help    = "Treat two iterations 'equal' if difference between them is less than this value")

    parser.add_argument("-w", "--shootout-win",
        type    = float,
        default = options.shootoutWinValue,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    parser.add_argument("-t", "--tie",
        type    = float,
        default = options.tieValue,
        help    = "Value given to both teams for a tie")

    parser.add_argument("--fakes",
        type    = int,
        default = options.fakeTies,
        help    = "Number of fake tie games given to each team")

    parser.add_argument("-f", "--filter",
        type    = str,
        default = ",".join(options.filteredTeams),
        help    = "Comma separated list of teams to remove from final rankings")

    parser.add_argument("-m", "--min-games",
        type    = int,
        default = options.minGamesPlayed,
        help    = "Filter teams from final standings that have less than this many games played")

    parser.add_argument("--cutoff",
        type    = datetime.date.fromisoformat,
        default = options.dateCutoff,
        help    = "Cutoff date; games played after this date will be ignored")

    parser.add_argument("--test",
        action  = "store_true",
        default = False,
        help    = "Enable test mode")

    parser.add_argument("-o", "--output",
        metavar = "<output.md>",
        type    = str,
        default = "",
        help    = "Write final rankings as a markdown formatted file")

    parser.add_argument("inputFile")

    args = parser.parse_args()
    options.inputFile         = args.inputFile
    options.outputFile        = args.output
    options.divisionName      = args.name
    options.krachMethod       = KrachMethod[args.krach.upper()]
    options.sosMethod         = SoSMethod[args.sos.upper()]
    options.maxIterations     = args.iterations
    options.maxRatingsDiff    = args.diff
    options.shootoutWinValue  = args.shootout_win
    options.tieValue          = args.tie
    options.fakeTies          = args.fakes
    options.filteredTeams     = args.filter.split(',')
    options.minGamesPlayed    = args.min_games
    options.dateCutoff        = args.cutoff
    options.test              = args.test

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return options

#----------------------------------------------------------------------------
def generate(options, ledger):
    krach = KRACH(options)
    ratings = krach.run(ledger)

    # Calculate final strength of schedules
    sosAll = krach.strengthOfScheduleAll(ledger, ratings)

    # Validate ratings by converting back to expected number of wins
    expectedWins = krach.expectedWinsAll(ledger, ratings)

    # Now that we're done all calculations, remove any ignored teams
    # (such as showcase teams)
    filterTeams(options, ledger, ratings)

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
        return Rating(name, value, sosAll[name], expectedWins[name], diff)
    return [ _rating(name,value) for name,value in ratings ]

#----------------------------------------------------------------------------
def runTests(options, ledger):
    packedConfigs = {
        "krachMethod" : [
            KrachMethod.BRADLEY_TERRY,
            KrachMethod.WIN_LOSS,
        ],
        "sosMethod" : [
            SoSMethod.AVERAGE,
            SoSMethod.DBAKER,
            SoSMethod.TBRW,
        ],
        "shootoutWinValue" : [0.5, 1.0],
        "fakeTies"         : [0, 1, 3],
        "maxIterations"    : [10, 100, 1000, 0],
    }
    configKeys, configValues = zip(*packedConfigs.items())
    configs = [dict(zip(configKeys, v)) for v in itertools.product(*configValues)]

    keys = set(sum(([k for k in config.keys()] for config in configs), []))

    table = [
        list(configs[0].keys()) + ['Total Diff', 'Avg Diff', 'Raw Total', 'Raw Avg', 'Spread'],
    ]

    for config in configs:
        customOptions = dataclasses.replace(options, **config)
        ratings = generate(customOptions, ledger)

        diffTotal = sum(abs(x.diff) for x in ratings)
        diffAvg   = diffTotal / len(ratings)
        rawTotal  = sum(x.diff for x in ratings)
        rawAvg    = rawTotal / len(ratings)

        if False:
            # filter out results at are clearly bad
            if diffTotal > 0.10 or rawTotal > 0.05:
                continue

        diffs = [
            f"{diffTotal:.2f}",
            f"{diffAvg:.2f}",
            f"{rawTotal:.2f}",
            f"{rawAvg:.2f}",
        ]
        spread = ratings[0].value - ratings[-1].value
        optionsDict = dataclasses.asdict(customOptions)
        results = [optionsDict[option] for option in packedConfigs.keys()] + diffs + [spread]
        table.append([str(x) for x in results])

    def _maxLen(col):
        return max(len(row[col]) for row in table)
    widths = [ _maxLen(col) for col in range(len(table[0])) ]

    for row in table:
        columns = [ " {0:>{width}} ".format(row[col], width=widths[col]) for col in range(len(row)) ]
        print("|".join( [""] + columns + [""] ))

    print("")

#----------------------------------------------------------------------------
def loadInputs(options):
    ledger = Ledger(options.dateCutoff)

    # Read in raw game data
    reader = AhfScoreReader()
    reader.read(options.inputFile, ledger)

    # Add in any fake game data
    addFakeTies(options, ledger)

    return ledger

#----------------------------------------------------------------------------
def writeOutputs(options, ledger, ratings):
    # Always show on the console
    showRankings(options, ledger, ratings)

    # optionally write to markdown file
    if options.outputFile:
        writeMarkdownRankings(options, ledger, ratings)

#----------------------------------------------------------------------------
def main(options):
    logging.debug("Processing '{}' with options:".format(options.inputFile))
    logging.debug(options)

    ledger = loadInputs(options)

    if options.test:
        runTests(options, ledger)
    else:
        ratings = generate(options, ledger)
        writeOutputs(options, ledger, ratings)

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    options = parseCommandLine()
    main(options)

