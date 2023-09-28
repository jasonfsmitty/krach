#!/usr/bin/env python3

import logging
import datetime
import sys
import os.path

import common.blackbear_common as bb
import common.commands as commands

#----------------------------------------------------------------------------
def showRankings(divisionName, ledger, ratings, league):
    dividor = "-" * 120
    print(f"Division: {divisionName}")
    print(f"Rank KRACH   Subdivision     Team                                     GP  WW-LL-TT  OTW OTL    SoS | Predict Diff WinPt Match")
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
        winPts = rating.winPoints
        matchupFactor = rating.matchupFactor
        print(f"{rank:>3} {value:>6} : {subdiv:<13} : {team:<40} {gp:>2}  {record} {sos:>6} | {exp:>5.1f} {diff:>5.1f} {winPts:>5.1f} {matchupFactor:>5.1f}")
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

