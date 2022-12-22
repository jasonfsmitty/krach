#!/usr/bin/env python3
# KRACH ratings calculator. See readme.md for more details

import argparse
import json
from dataclasses import dataclass, field

FILTERED_TEAMS = [
    'Littleton Hockey Association',
    'NYC Raiders Hockey Club',
    'Orland Park Vikings',
]

#----------------------------------------------------------------------------
@dataclass
class Options:
    maxIterations:  int   = 10000
    maxRatingsDiff: float = 0.0001
    soWinValue:     float = 0.50
    filteredTeams:  list  = field( default_factory=lambda: FILTERED_TEAMS )

g_options = Options()

#----------------------------------------------------------------------------
def shouldIgnore(team):
    return team in g_options.filteredTeams

#----------------------------------------------------------------------------
def filterTeams(ratings):
    for team in g_options.filteredTeams:
        if team in ratings:
            ratings.pop(team)
    return ratings

#----------------------------------------------------------------------------
def showRankings(ledger, ratings, sosAll):
    # brute force search for a scaling factor that will
    # allow all ratings to be displayed as integers
    scaleFactor = 1
    for rating in ratings.values():
        while int(rating * scaleFactor) <= 0:
            scaleFactor *= 10

    def scale(value):
        return int(scaleFactor * value + 0.5)

    dividor = "-" * 65
    print(f"Rank KRACH   Team                           WW-LL-SW-SL    SoS")
    print(dividor)

    ratings = sorted(ratings.items(), key=lambda kv: kv[1], reverse = True)
    for rank,entry in enumerate(ratings):
        # show subdivision split
        if rank in [4, 8]:
            print(dividor)

        rank   += 1
        team   = entry[0]
        rating = scale(entry[1])
        record = ledger.teams[team].record
        wins   = record.wins
        losses = record.losses
        sow    = record.soWins
        sol    = record.soLosses
        sos    = scale(sosAll.get(team, 0))
        print(f"{rank:>3} {rating:>6} : {team:<30} {wins:>2}-{losses:>2}-{sow:>2}-{sol:>2} {sos:>7}")

#----------------------------------------------------------------------------
@dataclass
class Record:
    played:   int = 0
    wins:     int = 0
    losses:   int = 0
    soWins:   int = 0
    soLosses: int = 0

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

    def winPoints(self):
        return self.wins + (self.soWins * g_options.soWinValue) + (self.soLosses * (1.0 - g_options.soWinValue))

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

#----------------------------------------------------------------------------
# Tracks all teams and their game results
class Ledger:
    def __init__(self):
        self.teams = dict()

    def addGame(self, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        self.teams[winner].addWin(loser)
        self.teams[loser ].addLoss(winner)

    def addShootout(self, winner, loser):
        self.addTeam(winner)
        self.addTeam(loser)
        self.teams[winner].addShootoutWin(loser)
        self.teams[loser ].addShootoutLoss(winner)

    def addTeam(self, team):
        if not team in self.teams:
            self.teams[team] = Team()

#----------------------------------------------------------------------------
# Read AHF score data into a ledger. This is specific to the JSON format
# provided by the gamesheetstats.com API. To use this script with a different
# data source, you would replace this reader with one specific to your context.
class AhfScoreReader:
    def __init__(self):
        pass

    def read(self, filename):
        ledger = Ledger()
        with open(filename) as f:
            jdata = json.load(f)
            for entry in jdata['0_0']:
                for game in entry['games']:
                    self.readGame(ledger, game)
        return ledger

    def readGame(self, ledger, game):
        team1      = game['homeTeam']['name']
        team1score = game['finalScore']['homeGoals']
        team2      = game['visitorTeam']['name']
        team2score = game['finalScore']['visitorGoals']
        shootout   = any(map(lambda x: x['title'] == 'SO', game['scoresByPeriod'])) 

        # Thanks to the shootout, AHF does not permit tie games
        assert team1score != team2score, f"Teams {team1} and {team2} have a tie score!"

        winner = team1 if team1score > team2score else team2
        loser  = team2 if team1score > team2score else team1

        if shootout:
            ledger.addShootout(winner, loser)
        else:
            ledger.addGame(winner, loser)

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
                print("Finished after {} interations".format(loop))
                return updated
            ratings = updated

        print("Bailed out after {} interations".format(loop))
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
                    matchup = ledger.teams[i].matchups[j]
                    total += matchup.played * ratings[j]
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
def parse_cmdline():
    parser = argparse.ArgumentParser()

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
        default = g_options.soWinValue,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    parser.add_argument("-f", "--filter",
        type    = str,
        default = ",".join(g_options.filteredTeams),
        help    = "Comma separated list of teams to remove from final rankings")

    parser.add_argument("inputFile")

    args = parser.parse_args()
    g_options.maxIterations  = args.iterations
    g_options.maxRatingsDiff = args.diff
    g_options.soWinValue     = args.shootout_win
    g_options.filteredTeams  = args.filter.split(',')

    return args.inputFile

#----------------------------------------------------------------------------
if __name__ == "__main__":
    inputFile = parse_cmdline()

    reader = AhfScoreReader()
    ledger = reader.read(inputFile)

    krach = KRACH()

    # generate krach ratings
    ratings = krach.run(ledger)

    # Calculate strength of schedules
    sosAll = krach.strengthOfSchedule(ledger, ratings)

    # Remove the one-off showcase teams
    ratings = filterTeams(ratings)

    # Re-normalize now that the showcase teams are gone
    #ratings = krach.normalize(ratings)

    showRankings(ledger, ratings, sosAll)

