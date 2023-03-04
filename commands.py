#!/usr/bin/env python3

import logging
import argparse
import sys
import datetime
import os.path

import gamesheets
import krach
import markdown_output as mo
import console_output as co
import scorereader
import blackbear_common as bb

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
        default = bb.DEFAULT_FAKES,
        help    = "Number of fake tie games given to each team")

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
	for d in divisions:
		gamesheets.downloadScores(d, SeasonId, Divisions)
        
#----------------------------------------------------------------------------
def updateCommand(args, SeasonId, League):
    options = krach.Options()

    options.maxIterations     = args.iterations
    options.maxRatingsDiff    = args.diff
    options.shootoutWinValue  = args.shootout_win
    options.tieValue          = args.tie
    options.fakeTies          = args.fakes
    options.minGamesPlayed    = args.min_games
    options.scaleMethod       = krach.ScaleMethod[args.scale.upper()]
    options.scaleFactor       = args.factor

    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)

    divisions = [args.div] if args.div else Divisions
    toc = []
    for divisionName in divisions:
        toc.append(updateRatings(options, args.cutoff, divisionName, args.test, Divisions, League))

    if not args.test:
        mo.writeDivisionIndex(toc)

#----------------------------------------------------------------------------
def teamsCommand(args, SeasonId, League):
    Divisions = gamesheets.populateDivisionsDictionary(SeasonId, League)
    divisions = [args.div] if args.div else Divisions
    for divisionName in divisions:
        co.listTeams(divisionName, Divisions)
        
#----------------------------------------------------------------------------
def updateRatings(options, dateCutoff, divisionName, testMode, Divions, League):
    info = Divions.get(divisionName, None)
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
    co.showRankings(divisionName, ledger, ratings, League)

    # optionally write to markdown file
    if not testMode:
        mo.writeMarkdownRankings(info['output'], options, divisionName, ledger, ratings, League)

    # (divisionName, startDate, endDate, .md path)
    return (divisionName, ledger.oldestGame, ledger.newestGame, info['output'])

#----------------------------------------------------------------------------
def loadInputs(dateCutoff, inputFile):
	ledger = krach.Ledger(dateCutoff)
	reader = scorereader.ScoreReader()
	reader.read(inputFile, ledger)
	return ledger