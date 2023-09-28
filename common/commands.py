#!/usr/bin/env python3

import logging
import argparse
import sys
import datetime
import os
import re
import json

import common.gamesheets as gamesheets
import common.krach as krach
import common.markdown_output as mo
import common.console_output as co
import common.scorereader as scorereader
import common.blackbear_common as bb

def sortDivisions(divisions):
    return sorted(divisions, key=lambda x:[int(re.findall('^\d+', x)[0]), x])

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
        default = bb.DEFAULT_ITERATIONS,
        help    = "Max iterations of the KRACH algorithm, or 0 for infinite")

    update.add_argument("--diff",
        type    = float,
        default = bb.DEFAULT_MAX_DIFF,
        help    = "Treat two iterations 'equal' if difference between them is less than this value")

    update.add_argument("-w", "--shootout-win",
        type    = float,
        default = bb.DEFAULT_SHOOTOUT_VALUE,
        help    = "Value of winning a game in overtime/shootout [0.0-1.0]")

    update.add_argument("-t", "--tie",
        type    = float,
        default = bb.DEFAULT_TIE_VALUE,
        help    = "Value given to both teams for a tie")

    update.add_argument("--fakes",
        type    = int,
        default = bb.DEFAULT_NUM_FAKE_TIES,
        help    = "Number of fake tie games given to each team")

    update.add_argument("--alpha-value",
        type    = float,
        default = bb.DEFAULT_ALPHA_VALUE,
        help    = "Value given to the real team for an alpha 'win'")

    update.add_argument("--alphas",
        type    = int,
        default = bb.DEFAULT_NUM_ALPHAS,
        help    = "Number of fake 'alpha' games given to each team")

    update.add_argument("--bonus",
        type    = float,
        default = bb.DEFAULT_BONUS_POINTS,
        help    = "Bonus 'win' points given to each team, in range [0.0-1.0]")

    update.add_argument("--scale",
        metavar = "<method>",
        choices = ["none", "auto", "factor", "range"],
        default = "factor",
        help    = "Method used to scale ratings for final rankings")

    update.add_argument("--factor",
        type    = int,
        default = bb.DEFAULT_SCALE_FACTOR,
        help    = "Scaling factor used by the scaling method.")

    update.add_argument("-m", "--min-games",
        type    = int,
        default = bb.DEFAULT_MIN_GAMES,
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
    cross = subparsers.add_parser('cross', help="Scan schedules for cross-division games")
    cross.set_defaults(func=crossCommand)

    cross.add_argument('-d', '--div', help="Single division to scan")
    cross.add_argument('-v', '--verbose', action='store_true', default=False, help="Show PURE divisions in addition to MIXED.")

    #----------------------------------------------------------
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)

    return args

#----------------------------------------------------------------------------
def downloadCommand(args, SeasonId, League):
    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)
    logging.info("Downloading scores ...")
    divisions = [args.div] if args.div else Divisions
    for d in sortDivisions(divisions):
        cleanOutputsForDivision(Divisions[d])
        gamesheets.downloadScores(d, SeasonId, Divisions)

#----------------------------------------------------------------------------
def updateCommand(args, SeasonId, League):
    options = krach.Options()

    options.maxIterations     = args.iterations
    options.maxRatingsDiff    = args.diff
    options.shootoutWinValue  = args.shootout_win
    options.tieValue          = args.tie
    options.fakeTies          = args.fakes
    options.alphaValue        = args.alpha_value
    options.alphaGames        = args.alphas
    options.bonusPoints       = args.bonus
    options.minGamesPlayed    = args.min_games
    options.scaleMethod       = krach.ScaleMethod[args.scale.upper()]
    options.scaleFactor       = args.factor

    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)

    divisions = [args.div] if args.div else Divisions
    toc = []
    for divisionName in sortDivisions(divisions):
        logging.info("Updating ratings for " + divisionName)
        toc.append(updateRatings(options, SeasonId, args.cutoff, divisionName, args.test, Divisions, League))

    if not args.test:
        mo.writeDivisionIndex(toc, League)

#----------------------------------------------------------------------------
def teamsCommand(args, SeasonId, League):
    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)
    divisions = [args.div] if args.div else Divisions

    for divisionName in sortDivisions(divisions):
        options = krach.Options()
        ledger,info = loadInputs(options, SeasonId, datetime.date.today(), divisionName, Divisions)
        teamNames = sorted(list(team for team in ledger.teams if team.lower() not in options.filteredTeams))
        for name in teamNames:
            print("{}".format(name))


#----------------------------------------------------------------------------
def crossCommand(args, SeasonId, League):
    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)
    divisions = [args.div] if args.div else Divisions

    pureDivisions = set()
    mixedDivisions = dict()

    for divisionName in sortDivisions(divisions):
        gamesheets.downloadSchedule(divisionName, SeasonId, Divisions, force=False)
        seenDivisions = scanForCrossTeamPlay(divisionName, Divisions)
        if len(seenDivisions) == 1:
            pureDivisions.add(divisionName)
        else:
            mixedDivisions[divisionName] = seenDivisions

    if args.verbose:
        print("Pure divisions:")
        for pure in pureDivisions:
            print("  * {}".format(pure))

        for mixed,others in mixedDivisions.items():
            print("{} is mixed with:".format(mixed))
            for other in others:
                print("  * {}".format(other))

        print("")

    alreadySeen = set()
    for primaryDivision, seenDivisions in mixedDivisions.items():
        if primaryDivision in alreadySeen:
            continue

        changed = True
        grouping = set(seenDivisions)
        grouping.difference_update(alreadySeen)
        while changed:
            changed = False
            for d in list(grouping):
                if d in alreadySeen:
                    continue
                alreadySeen.add(d)
                grouping.update(mixedDivisions.get(d, set()))
                changed = True

        if len(grouping) == 0:
            continue

        print("Mixed Group:")
        for entry in grouping:
            print("  * {}".format(entry))
        print("")

#----------------------------------------------------------------------------
def scanForCrossTeamPlay(divisionName, Divisions):
    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    seenDivisions = set()
    with open(info['schedule']) as f:
        jdata = json.load(f)
        for chunk in jdata.values():
            for gameDay in chunk:
                for game in gameDay.get('games',[]):
                    seenDivisions.add(game['homeTeam']['division'])
                    seenDivisions.add(game['visitorTeam']['division'])

    #seenDivisions.discard(divisionName)
    return seenDivisions

#----------------------------------------------------------------------------
def cleanOutputsForDivision(info):
    for filename in info['output'].values():
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.mkdir(directory)
        elif os.path.exists(filename):
            os.remove(filename)

#----------------------------------------------------------------------------
def updateRatings(options, seasonId, dateCutoff, divisionName, testMode, Divisions, League):
    ledger,info = loadInputs(options, seasonId, dateCutoff, divisionName, Divisions)
    ratings = krach.generate(options, ledger)

    if len(ledger.teams) == 0:
        logging.info("No teams found for %s", divisionName)
        sys.exit(1)

    # Always show on the console
    co.showRankings(divisionName, ledger, ratings, League, options if testMode else None)

    # optionally write to markdown file
    if not testMode:
        mo.writeMarkdownRankings(info['output']['ratings'], options, divisionName, ledger, ratings, League)

    # (divisionName, startDate, endDate, .md path)
    return (divisionName, ledger.oldestGame, ledger.newestGame, info['output']['ratings'])

#----------------------------------------------------------------------------
def loadInputs(options, seasonId, dateCutoff, divisionName, Divisions):
    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    inputFile = info['output']['scores']
    filterFile = info['input']['filter']
    if os.path.exists(filterFile):
        options.filteredTeams = [ line.strip() for line in open(filterFile) ]
    else:
        options.filteredTeams = []

    ledger = krach.Ledger(seasonId, dateCutoff)
    reader = scorereader.ScoreReader()
    reader.read(inputFile, ledger)
    return (ledger, info)

