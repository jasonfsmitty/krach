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
from dataclasses import dataclass, field

#----------------------------------------------------------------------------
def writeMarkdownTable(f, data, keyTitle="Option", valueTitle="Value"):
    f.write(f"| {keyTitle} | {valueTitle} |\n")
    f.write(f"| :----- | ----: |\n")
    for k,v in data.items():
        f.write(f"| {k} | {v} |\n")
    f.write(f"\n")

#----------------------------------------------------------------------------
@dataclass
class Options:
    divisionName:      str   = ""

    # Options to determine when to stop recursing through the KRACH algorithm.
    maxIterations:     int   = 10000   # max number of loops
    maxRatingsDiff:    float = 0.0001  # max diff between two runs that is considered "equal"

    # Options that control how shootout wins/losses and ties are weighted in the rankings
    shootoutWinValue:  float = 0.50
    shootoutLossValue: float = 0.50
    tieValue:          float = 0.50

    # Showcases may include guest teams, that play valid games that count toward
    # KRACH ratings, but are not included in the final standings. These options
    # are for filtering out these teams.
    filteredTeams:     list  = field(default_factory=lambda: []) # Explicit list of teams
    minGamesPlayed:    int   = 0 # ignore teams with less than the min number of games

    # Option to ignore games after a specific date cutoff. This allows using
    # the latest score results to recreate the KRACH ratings from previous weeks.
    dateCutoff:        str   = field(default_factory=lambda: datetime.date.today())

    def isValid(self, date):
        return date <= self.dateCutoff

    def dict(self):
        return {
            "Max Iterations"      : "{}".format(self.maxIterations),
            "Max Ratings Diff"    : "{}".format(self.maxRatingsDiff),
            "Shootout Win Value"  : "{:3.2f}".format(self.shootoutWinValue),
            "Shootout Loss Value" : "{:3.2f}".format(self.shootoutLossValue),
            "Tie Value"           : "{:3.2f}".format(self.tieValue),
            "Ignore teams"        : "{}".format(",".join(self.filteredTeams)),
            "Min Games Played"    : "{}".format(self.minGamesPlayed),
            "Date Cutoff"         : "{}".format(self.dateCutoff),
        }

    def __str__(self):
        return '\n'.join([ "  {:<20} : {}".format(k, v) for k,v in self.dict().items() ])

g_options = Options()

#----------------------------------------------------------------------------
def removeTeam(ratings, team):
    if team in ratings:
        ratings.pop(team)

#----------------------------------------------------------------------------
def filterTeams(ledger, ratings):
    # remove teams explicitly called out
    for team in g_options.filteredTeams:
        removeTeam(ratings, team)

    for name,team in ledger.teams.items():
        if team.record.played < g_options.minGamesPlayed:
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
def showRankings(ledger, ratings, sosAll):
    dividor = "-" * 80
    print(f"Rank KRACH   Team                                     GP  WW-LL-SW-SL-TT    SoS")
    print(dividor)

    numTeams = len(ratings)
    for rank,entry in enumerate(ratings):
        rank   += 1
        subdiv = subdivision(numTeams, rank)
        team   = entry[0]
        rating = entry[1]
        gp     = ledger.teams[team].record.played
        record = str(ledger.teams[team].record)
        sos    = sosAll.get(team, 0)
        print(f"{rank:>3} {rating:>6} : {subdiv:<13} : {team:<40} {gp:>2}  {record} {sos:>7}")

#----------------------------------------------------------------------------
def writeMarkdownRankings(outputFile, ledger, ratings, sosAll):

    with open(outputFile, "w") as f:
        f.write(f"# {g_options.divisionName} KRACH Rankings\n")

        lines = [
            ['Rank', 'KRACH', 'Subdivision', 'Team', 'GP',   'W',    'L',    'SOW',  'SOL',  'T',    'SoS'],
            ['---:', '---:',  ':---',        ':---', '---:', '---:', '---:', '---:', '---:', '---:', '---:'],
        ]
        for line in lines:
            f.write('|'.join(line))
            f.write('\n')

        numTeams = len(ratings)
        for rank,entry in enumerate(ratings):
            rank   += 1
            team   = entry[0]
            rating = entry[1]
            record = ledger.teams[team].record
            gp     = record.played
            wins   = record.wins
            losses = record.losses
            otw    = record.soWins
            otl    = record.soLosses
            ties   = record.ties
            sos    = sosAll.get(team, 0)
            columns = [rank, rating, subdivision(numTeams, rank), team, gp, wins, losses, otw, otl, ties, sos]
            f.write('|'.join(map(str, columns)))
            f.write('\n')


        f.write("# Generation Details\n")
        f.write("\n")

        f.write("Generated with command line:\n")
        f.write("```\n")
        f.write(" ".join(sys.argv[:]))
        f.write("\n```\n")
        f.write("\n")
        
        data = {
            "Game Start Date" : f"{ledger.newestGame}",
            "Game End Date"   : f"{ledger.oldestGame}",
        }
        data.update(g_options.dict())
        writeMarkdownTable(f, data)

#----------------------------------------------------------------------------
@dataclass
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

    def winPoints(self):
        return self.wins \
            + (self.soWins   * g_options.shootoutWinValue) \
            + (self.soLosses * g_options.shootoutLossValue) \
            + (self.ties     * g_options.tieValue)

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
    def __init__(self):
        self.teams = dict()
        self.oldestGame = None
        self.newestGame = None

    def addGame(self, date, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        if g_options.isValid(date):
            self.recordDate(date)
            self.teams[winner].addWin(loser)
            self.teams[loser ].addLoss(winner)

    def addShootout(self, date, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        if g_options.isValid(date):
            self.recordDate(date)
            self.teams[winner].addShootoutWin(loser)
            self.teams[loser ].addShootoutLoss(winner)

    def addTie(self, date, team1, team2):
        self.addTeam(team1)
        self.addTeam(team2)
        if g_options.isValid(date):
            self.recordDate(date)
            self.teams[team1].addTie(team2)
            self.teams[team2].addTie(team1)

    def addTeam(self, team):
        if not team in self.teams:
            self.teams[team] = Team()

    def recordDate(self, date):
        if not self.oldestGame or date < self.oldestGame:
            self.oldestGame = date
        if not self.newestGame or date < self.newestGame:
            self.newestGame = date

#----------------------------------------------------------------------------
# Implements the KRACH algorithm.
class KRACH:
    def __init__(self):
        pass

    #----------------------------------------------------------------------------
    # Execute the KRACH/Bradley-Terry algorithm until the ratings converge, or
    # we hit our max iteration limit.
    def run(self, ledger) -> dict[str, float]:
        # Initial guesses at the krach ratings; doesn't really matter as we'll iterate
        # until we get to the correct values.
        ratings = { k : 1.0 for k in ledger.teams.keys() }

        loop = 0
        while (g_options.maxIterations <= 0) or (g_options.maxIterations > 0 and loop < g_options.maxIterations):
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
    # Calculates an updated rating for a single team, using:
    #   Ki = Vi / ( ∑j Nij / (Ki + Kj) )
    def calculate(self, ledger, ratings, i):
        return ledger.teams[i].record.winPoints() / self.calculateMatchupFactor(ledger, ratings, i)

    #----------------------------------------------------------------------------
    # Calculate: ∑j Nij / (Ki + Kj)
    def calculateMatchupFactor(self, ledger, ratings, i):
        myTeam = ledger.teams[i]
        sumOfMatchups = 0.0
        # Iterate through all other teams in the league
        for j,otherTeam in ledger.teams.items():
            # Ignore ourselves, and any teams we haven't played
            if i != j and (j in myTeam.matchups):
                myPoints = myTeam.matchups[j].winPoints()
                theirPoints = otherTeam.matchups[i].winPoints()
                sumOfMatchups += (myPoints + theirPoints) / (ratings[i] + ratings[j])
        return sumOfMatchups

    #----------------------------------------------------------------------------
    def strengthOfSchedule(self, ledger, ratings):
        sos = {}
        for i in ledger.teams:
            total = 0.0
            for j in ledger.teams:
                if i != j and j in ledger.teams[i].matchups:
                    total += ledger.teams[i].matchups[j].played * ratings[j]
            sos[i] = total / ledger.teams[i].record.played
        return sos

    #----------------------------------------------------------------------------
    def normalize(self, ratings):
        total = sum(ratings.values())
        return { name : value / total for name,value in ratings.items() }

    #----------------------------------------------------------------------------
    def areRatingsEqual(self, original, updated):
        return all( abs(original[team] - updated[team]) <= g_options.maxRatingsDiff for team in original )

#----------------------------------------------------------------------------
# Read AHF score data into a ledger. This is specific to the JSON format
# provided by the gamesheetstats.com API. To use this script with a different
# data source, you would replace this reader with one specific to your context.
class AhfScoreReader:
    def __init__(self):
        pass

    #----------------------------------------------------------------------------
    def read(self, filename):
        ledger = Ledger()
        with open(filename) as f:
            jdata = json.load(f)
            for entry in jdata['0_0']:
                for game in entry['games']:
                    self.readGame(ledger, game)
        return ledger

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
def parseCommandLine():
    parser = argparse.ArgumentParser()

    parser.add_argument("--debug",
        action  = 'store_true',
        default = False,
        help    = "Enable extra debug logging")

    parser.add_argument("-n", "--name",
        type    = str,
        default = g_options.divisionName,
        help    = "Division Name")

    parser.add_argument("-i", "--iterations",
        type    = int,
        default = g_options.maxIterations,
        help    = "Max iterations of the KRACH algorithm, or 0 for infinite")

    parser.add_argument("-d", "--diff",
        type    = float,
        default = g_options.maxRatingsDiff,
        help    = "Treat two iterations 'equal' if difference between them is less than this value")

    parser.add_argument("-w", "--shootout-win",
        type    = float,
        default = g_options.shootoutWinValue,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    parser.add_argument("-l", "--shootout-loss",
        type    = float,
        default = None,
        help    = "Value of losing a game in overtime/shootout [0.0-1.0] (defaults to (1.0 - shootoutWin)")

    parser.add_argument("-t", "--tie",
        type    = float,
        default = g_options.tieValue,
        help    = "Value given to both teams for a tie")

    parser.add_argument("-f", "--filter",
        type    = str,
        default = ",".join(g_options.filteredTeams),
        help    = "Comma separated list of teams to remove from final rankings")

    parser.add_argument("-m", "--min-games",
        type    = int,
        default = g_options.minGamesPlayed,
        help    = "Filter teams from final standings that have less than this many games played")

    parser.add_argument("--cutoff",
        type    = datetime.date.fromisoformat,
        default = g_options.dateCutoff,
        help    = "Cutoff date; games played after this date will be ignored")

    parser.add_argument("-o", "--output",
        metavar = "<output.md>",
        type    = str,
        default = "",
        help    = "Write final rankings as a markdown formatted file")

    parser.add_argument("inputFile")

    args = parser.parse_args()
    g_options.divisionName      = args.name
    g_options.maxIterations     = args.iterations
    g_options.maxRatingsDiff    = args.diff
    g_options.shootoutWinValue  = args.shootout_win
    g_options.shootoutLossValue = args.shootout_loss if args.shootout_loss else (1.0 - args.shootout_win)
    g_options.tieValue          = args.tie
    g_options.filteredTeams     = args.filter.split(',')
    g_options.minGamesPlayed    = args.min_games
    g_options.dateCutoff        = args.cutoff

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return (args.inputFile, args.output)

#----------------------------------------------------------------------------
def main(inputFile, outputFile):
    logging.debug("Processing '{}' with options:".format(inputFile))
    logging.debug(g_options)

    reader = AhfScoreReader()
    ledger = reader.read(inputFile)

    # generate krach ratings
    krach = KRACH()
    ratings = krach.run(ledger)

    # Calculate strength of schedules
    sosAll = krach.strengthOfSchedule(ledger, ratings)

    # Remove the one-off showcase teams
    filterTeams(ledger, ratings)

    # scale up so all values are integers
    scaleRankings(ratings, sosAll)

    # sort by krach ratings, highest first.
    ratings = sorted(ratings.items(), key=lambda kv: kv[1], reverse = True)

    # display to console
    showRankings(ledger, ratings, sosAll)

    if outputFile:
        writeMarkdownRankings(outputFile, ledger, ratings, sosAll)

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main(*parseCommandLine())

