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
    def _addTeam(self, ledger, team):
        ledger.addTeam(team['name'], team['id'], team['division'])

    def _addTeams(self, ledger, game):
        for x in ['homeTeam', 'visitorTeam']:
            self._addTeam(ledger, game[x])

    #----------------------------------------------------------------------------
    def read(self, scheduleFile, scoresFile, ledger):
        with open(scheduleFile) as f:
            jdata = json.load(f)
            for chunk in jdata.values():
                for gameDay in chunk:
                    for game in gameDay.get('games',[]):
                        self._addTeams(ledger, game)

        with open(scoresFile) as f:
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
        overtime   = any(map(lambda x: x['title'] == 'OT', game['scoresByPeriod']))

        winner = team1 if team1score > team2score else team2
        loser  = team2 if team1score > team2score else team1

        self._addTeams(ledger, game)

        if team1score == team2score:
            ledger.addTie(date, team1, team2)
        elif overtime:
            ledger.addOvertime(date, winner, loser)
        elif shootout:
            ledger.addShootout(date, winner, loser)
        else:
            ledger.addGame(date, winner, loser)

