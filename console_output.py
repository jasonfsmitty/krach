#!/usr/bin/env python3

import logging
import datetime
import sys
import os.path

import blackbear_common as bb
import commands

#----------------------------------------------------------------------------
def showRankings(divisionName, ledger, ratings, league):
    dividor = "-" * 115
    print(f"Division: {divisionName}")
    print(f"Rank KRACH   Subdivision     Team                                     GP  WW-LL-SW-SL-TT    SoS | Predict Diff")
    print(dividor)

    diffTotal = 0.0
    rawTotal = 0.0
    numTeams = len(ratings)
    
    if numTeams == 0:
        print("No teams found")
        sys.exit(1)

    for rank,rating in enumerate(ratings):
        rank   += 1
        subdiv = bb.getSubDivision(league, numTeams, rank)
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
    print(f"")

#----------------------------------------------------------------------------
def listTeams(divisionName, Divisions):
    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    filterFile = info['filter']
    if os.path.exists(filterFile):
        filteredTeams = set(line.strip().lower() for line in open(info['filter']))
    else:
        filteredTeams = set()

    ledger = commands.loadInputs(datetime.date.today(), info['scores'])
    teamNames = sorted(list(team for team in ledger.teams if team.lower() not in filteredTeams))

    for name in teamNames:
        print("{}".format(name))