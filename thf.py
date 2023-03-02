#!/usr/bin/env python3

import logging
import argparse
import requests
import json
import sys
import datetime
import dataclasses
import itertools
import copy
import os.path

import krach

#----------------------------------------------------------------------------
# Default settings to mimic THF results

DEFAULT_ITERATIONS     = 200
DEFAULT_MAX_DIFF       = 0.00001
DEFAULT_SHOOTOUT_VALUE = 1.0
DEFAULT_FAKES          = 1
DEFAULT_TIE_VALUE      = 0.85
DEFAULT_MIN_GAMES      = 12
DEFAULT_SCALE_FACTOR   = 10000

#----------------------------------------------------------------------------
SEASON = 1684 # Hard-coded for the 2022-2023 season

DIVISIONS = {
    # 10U ------------------------------------------------
    'USPHL North 15 Pure' : {
        'id'     : 12782,
        'scores' : 'results/USPHL-North-15-Pure-scores.json',
        'filter' : 'results/USPHL-North-15-Pure-filter.txt',
        'output' : 'results/USPHL-North-15-Pure-ratings.md',
    },
}

#----------------------------------------------------------------------------
# Read THF score data into a ledger. This is specific to the JSON format
# provided by the gamesheetstats.com API. To use this script with a different
# data source, you would replace this reader with one specific to your context.
class THFScoreReader:
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
# THF specific: each division gets split into subdivisions, with each
# competing in their own playoffs.
SUBDIVISIONS = [
    'Super 6',
    'Frozen 4',
]

# Only the top 4 teams of each subdivision compete in the playoffs;
# THe THF KRACH rankings list other teams as being in the lowest
# subdivision, but this makes it clearer who is in/out of playoff
# contention.
NO_SUBDIVISION = ""

def subdivision(numTeams, rank):
    if numTeams <= 9:
        if rank <=  4: return SUBDIVISIONS[1]
    elif numTeams >= 11:
        if rank <=  6: return SUBDIVISIONS[0]
        if rank >=  7: return SUBDIVISIONS[1]
    return NO_SUBDIVISION

#----------------------------------------------------------------------------
def writeMarkdownTable(f, data, keyTitle="Option", valueTitle="Value"):
    f.write(f"| {keyTitle} | {valueTitle} |\n")
    f.write(f"| :----- | ----: |\n")
    for k,v in data.items():
        f.write(f"| {k} | {v} |\n")
    f.write(f"\n")

#----------------------------------------------------------------------------
def writeMarkdownRankings(outputFile, options, divisionName, ledger, ratings):
    with open(outputFile, "w") as f:
        f.write(f"[<- back to the index](readme.md)\n")
        f.write(f"# {divisionName} KRACH Rankings\n")

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
def showRankings(divisionName, ledger, ratings):
    dividor = "-" * 115
    print(f"Division: {divisionName}")
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
    print(f"")

#----------------------------------------------------------------------------
def buildUrl(season, divisionId):
    baseURL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(baseURL, season, divisionId)

#------------------------------------------------------------------------------
def getDivisionScores(season, divisionName, divisionId):
    url = buildUrl(season, divisionId)
    logging.debug("GET: {}".format(url))
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Failed to query '{}' for season={} division={}: status={}".format(url, season, divisionId, response.status_code))
        logging.error("Response = {}".format(str(response)))
        raise RuntimeError("Failed to get scores")
    return response.json()

#----------------------------------------------------------------------------
def downloadScores(divisionName):
    logging.info("Getting scores for division '{}'".format(divisionName))

    info = DIVISIONS.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    scores = getDivisionScores(SEASON, divisionName, info['id'])
    with open(info['scores'], "w") as f:
        json.dump(scores, f)
    
#----------------------------------------------------------------------------
def downloadCommand(args):
    logging.info("Downloading scores ...")
    divisions = [args.div] if args.div else DIVISIONS
    for d in divisions:
        downloadScores(d)

#----------------------------------------------------------------------------
def loadInputs(dateCutoff, inputFile):
    ledger = krach.Ledger(dateCutoff)
    reader = THFScoreReader()
    reader.read(inputFile, ledger)
    return ledger

#----------------------------------------------------------------------------
def updateRatings(options, dateCutoff, divisionName, testMode):
    info = DIVISIONS.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    filterFile = info['filter']
    if os.path.exists(filterFile):
        options.filteredTeams = [ line.strip() for line in open(info['filter']) ]
    else:
        options.filteredTeams = []

    ledger = loadInputs(dateCutoff, info['scores'])
    ratings = krach.generate(options, ledger)

    # Always show on the console
    showRankings(divisionName, ledger, ratings)

    # optionally write to markdown file
    if not testMode:
        writeMarkdownRankings(info['output'], options, divisionName, ledger, ratings)

    # (divisionName, startDate, endDate, .md path)
    return (divisionName, ledger.oldestGame, ledger.newestGame, info['output'])

#----------------------------------------------------------------------------
def writeDivisionIndex(toc):
    with open("results/readme.md", "w") as f:
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

#----------------------------------------------------------------------------
def updateCommand(args):
    options = krach.Options()

    options.maxIterations     = args.iterations
    options.maxRatingsDiff    = args.diff
    options.shootoutWinValue  = args.shootout_win
    options.tieValue          = args.tie
    options.fakeTies          = args.fakes
    options.minGamesPlayed    = args.min_games
    options.scaleMethod       = krach.ScaleMethod[args.scale.upper()]
    options.scaleFactor       = args.factor

    divisions = [args.div] if args.div else DIVISIONS
    toc = []
    for divisionName in divisions:
        toc.append(updateRatings(options, args.cutoff, divisionName, args.test))

    if not args.test:
        writeDivisionIndex(toc)

#----------------------------------------------------------------------------
def listTeams(divisionName):
    info = DIVISIONS.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    filterFile = info['filter']
    if os.path.exists(filterFile):
        filteredTeams = set(line.strip().lower() for line in open(info['filter']))
    else:
        filteredTeams = set()

    ledger = loadInputs(datetime.date.today(), info['scores'])
    teamNames = sorted(list(team for team in ledger.teams if team.lower() not in filteredTeams))

    for name in teamNames:
        print("{}".format(name))
    
#----------------------------------------------------------------------------
def teamsCommand(args):
    divisions = [args.div] if args.div else DIVISIONS
    for divisionName in divisions:
        listTeams(divisionName)

#----------------------------------------------------------------------------
def parseCommandLine():
    options = krach.Options()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="Commands")

    parser.add_argument("--debug",
        action  = 'store_true',
        default = False,
        help    = "Enable extra debug logging")

    #----------------------------------------------------------
    # Download scores for all/single divisions

    download = subparsers.add_parser('download', help="Download latest scores")
    download.set_defaults(func=downloadCommand)

    download.add_argument('-d', '--div', help="Single division to update")

    #----------------------------------------------------------
    # Refresh ratings for all/single divisions

    update = subparsers.add_parser('update', help="Update krach ratings")
    update.set_defaults(func=updateCommand)

    update.add_argument('-d', '--div', help="Single division to update")

    update.add_argument("-i", "--iterations",
        type    = int,
        default = DEFAULT_ITERATIONS,
        help    = "Max iterations of the KRACH algorithm, or 0 for infinite")

    update.add_argument("--diff",
        type    = float,
        default = DEFAULT_MAX_DIFF,
        help    = "Treat two iterations 'equal' if difference between them is less than this value")

    update.add_argument("-w", "--shootout-win",
        type    = float,
        default = DEFAULT_SHOOTOUT_VALUE,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    update.add_argument("-t", "--tie",
        type    = float,
        default = DEFAULT_TIE_VALUE,
        help    = "Value given to both teams for a tie")

    update.add_argument("--fakes",
        type    = int,
        default = DEFAULT_FAKES,
        help    = "Number of fake tie games given to each team")

    update.add_argument("--scale",
        metavar = "<method>",
        choices = ["none", "auto", "factor", "range"],
        default = "factor",
        help    = "Method used to scale ratings for final rankings")

    update.add_argument("--factor",
        type    = int,
        default = DEFAULT_SCALE_FACTOR,
        help    = "Scaling factor used by the scaling method.")

    update.add_argument("-m", "--min-games",
        type    = int,
        default = DEFAULT_MIN_GAMES,
        help    = "Filter teams from final standings that have less than this many games played")

    update.add_argument("--cutoff",
        type    = datetime.date.fromisoformat,
        default = datetime.date.today(),
        help    = "Cutoff date; games played after this date will be ignored")

    update.add_argument("--test",
        action  = "store_true",
        default = False,
        help    = "Write to console only.")

    #----------------------------------------------------------
    teams = subparsers.add_parser('teams', help="List the teams per division")
    teams.set_defaults(func=teamsCommand)

    teams.add_argument('-d', '--div', help="Single division to update")

    #----------------------------------------------------------
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)

    return args

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args = parseCommandLine()
    args.func(args)

