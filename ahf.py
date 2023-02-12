#!/usr/bin/env python3

import logging
import argparse
import json
import sys
import datetime
import dataclasses
import itertools
import copy

import krach

#----------------------------------------------------------------------------
DEFAULT_ITERATIONS     = 10
DEFAULT_MAX_DIFF       = 0.0000001
DEFAULT_SHOOTOUT_VALUE = 1.0
DEFAULT_FAKES          = 0
DEFAULT_MIN_GAMES      = 12

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
def loadInputs(options):
    ledger = krach.Ledger(options.dateCutoff)

    # Read in raw game data
    reader = AhfScoreReader()
    reader.read(options.inputFile, ledger)

    return ledger

#----------------------------------------------------------------------------
def runTests(options, originalLedger):
    packedConfigs = {
        "krachMethod" : [
            krach.KrachMethod.BRADLEY_TERRY,
            krach.KrachMethod.WIN_LOSS,
        ],
        "sosMethod" : [
            krach.SoSMethod.AVERAGE,
            krach.SoSMethod.DBAKER,
            krach.SoSMethod.TBRW,
        ],
        "shootoutWinValue" : [0.5, 1.0],
        "fakeTies"         : [0, 1, 3],
        "maxIterations"    : [10, 100, 0],
    }
    configKeys, configValues = zip(*packedConfigs.items())
    configs = [dict(zip(configKeys, v)) for v in itertools.product(*configValues)]

    keys = set(sum(([k for k in config.keys()] for config in configs), []))

    table = [
        list(configs[0].keys()) + ['Total Diff', 'Avg Diff', 'Raw Total', 'Raw Avg', 'Spread'],
    ]

    for config in configs:
        ledger = copy.deepcopy(originalLedger)

        customOptions = dataclasses.replace(options, **config)
        ratings = krach.generate(customOptions, ledger)

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
def writeMarkdownTable(f, data, keyTitle="Option", valueTitle="Value"):
    f.write(f"| {keyTitle} | {valueTitle} |\n")
    f.write(f"| :----- | ----: |\n")
    for k,v in data.items():
        f.write(f"| {k} | {v} |\n")
    f.write(f"\n")

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
def writeOutputs(options, ledger, ratings):
    # Always show on the console
    showRankings(options, ledger, ratings)

    # optionally write to markdown file
    if options.outputFile:
        writeMarkdownRankings(options, ledger, ratings)

#----------------------------------------------------------------------------
def parseCommandLine():
    # FIXME: use groups to split options between general and krach-specific
    options = krach.Options()
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
        default = DEFAULT_ITERATIONS,
        help    = "Max iterations of the KRACH algorithm, or 0 for infinite")

    parser.add_argument("-d", "--diff",
        type    = float,
        default = DEFAULT_MAX_DIFF,
        help    = "Treat two iterations 'equal' if difference between them is less than this value")

    parser.add_argument("-w", "--shootout-win",
        type    = float,
        default = DEFAULT_SHOOTOUT_VALUE,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    parser.add_argument("-t", "--tie",
        type    = float,
        default = options.tieValue,
        help    = "Value given to both teams for a tie")

    parser.add_argument("--fakes",
        type    = int,
        default = DEFAULT_FAKES,
        help    = "Number of fake tie games given to each team")

    parser.add_argument("-f", "--filter",
        type    = str,
        default = ",".join(options.filteredTeams),
        help    = "Comma separated list of teams to remove from final rankings")

    parser.add_argument("-m", "--min-games",
        type    = int,
        default = DEFAULT_MIN_GAMES,
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
    options.krachMethod       = krach.KrachMethod[args.krach.upper()]
    options.sosMethod         = krach.SoSMethod[args.sos.upper()]
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
def main(options):
    logging.debug("Processing '{}' with options:".format(options.inputFile))
    logging.debug(options)

    ledger = loadInputs(options)

    if options.test:
        runTests(options, ledger)
    else:
        ratings = krach.generate(options, ledger)
        writeOutputs(options, ledger, ratings)

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    options = parseCommandLine()
    main(options)

