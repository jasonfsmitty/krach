#!/usr/bin/env python3

import datetime
import os.path
import sys

import common.blackbear_common as bb

#----------------------------------------------------------------------------
def writeMarkdownTable(f, data, keyTitle="Option", valueTitle="Value"):
    f.write(f"| {keyTitle} | {valueTitle} |\n")
    f.write(f"| :----- | ----: |\n")
    for k,v in data.items():
        f.write(f"| {k} | {v} |\n")
    f.write(f"\n")

#----------------------------------------------------------------------------
def writeMarkdownRankings(outputFile, options, divisionName, ledger, ratings, league):
    with open(outputFile, "w") as f:
        f.write(f"[<- back to the index](readme.md)\n")
        f.write(f"# {divisionName} KRACH Rankings\n")
        f.write("Rankings generated on {}.\n".format(datetime.datetime.now().strftime("%c")))
        f.write("\n")

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
            columns = [rank, value, bb.getSubDivision(league, numTeams, rank), team, gp, wins, losses, otw, otl, ties, sos, expW, diff]
            f.write('|'.join(map(str, columns)))
            f.write('\n')
        f.write('\n')

        # magnitude
        totalDiff = sum(abs(x.diff) for x in ratings)
        avgDiff   = totalDiff / len(ratings)

        totalRaw  = sum(x.diff for x in ratings)
        avgRaw    = totalRaw / len(ratings)

        #-------------------------------------------------------
        f.write(f"## Actual vs Expected\n")

        f.write("Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.\n")
        f.write("\n")

        f.write(f"||Absolute|Raw\n")
        f.write(f"|---:|---:|---:\n")
        f.write(f"|Total|{totalDiff:.2f}|{totalRaw:.2f}\n")
        f.write(f"|Avg|{avgDiff:.2f}|{avgRaw:.2f}\n")
        f.write(f"\n")

        #-------------------------------------------------------
        f.write(f"## Predictions\n")
        f.write(f"Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).\n")

        # headings
        f.write(f"|".join( ["", ""] + [rating.name for rating in ratings]))
        f.write(f"\n")
        f.write(f"| --: " * (len(ratings) + 1))
        f.write(f"\n")

        for myRating in ratings:
            def _percentage(opp):
                if myRating.name == opp.name:
                    return "--"
                return "{:>3}%".format(int(myRating.odds[opp.name] * 100.0 + 0.5))
            f.write(f"|{myRating.name}|")
            f.write(f"|".join( _percentage(opp) for opp in ratings))
            f.write(f"\n")
        f.write(f"\n")

        #-------------------------------------------------------
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
def writeDivisionIndex(toc, league):
    directory = "results/{}".format(bb.getLeagueAbbreviation(league).lower())+"/"
    with open(directory+"readme.md", "w") as f:
        f.write("[<- Back](../readme.md)\n")
        f.write("# KRACH Ratings\n")
        f.write("Click below to see KRACH ratings for each division\n")
        f.write("\n")
        f.write("| Division | Season Start | Latest Game |\n")
        f.write("| :-- | :-- | :-- |\n")

        for entry in toc:
            f.write("| [{}]({}) | {} | {} |\n".format(entry[0], os.path.basename(entry[3]), entry[1], entry[2]))
        f.write("\n")
        f.write("Generated on {}.\n".format(datetime.datetime.now()))
