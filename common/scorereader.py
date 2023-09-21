#!/usr/bin/env python3

import datetime
import json

#----------------------------------------------------------------------------
# Read AHF/AGHF/THGF score data into a ledger. This is specific to the JSON format
# provided by the gamesheetstats.com API. To use this script with a different
# data source, you would replace this reader with one specific to your context.
class ScoreReader:
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
        if game['date'] == 'Invalid Date':
            return

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
