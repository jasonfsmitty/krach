#!/usr/bin/env python3

import logging
import requests
import datetime
import json
import os
import sys

import common.blackbear_common as bb

API_URL = "https://gamesheetstats.com/api/"

#------------------------------------------------------------------------------
def ignoreDivision(name):
    return name.startswith('Mite') or any(map(lambda x: name.find(x) != -1, ['Guest', 'Championship', 'Gold', 'Silver', 'Bronze', 'Super 6', 'Frozen 4'])) or any(map(lambda x: name.find(x) != -1, bb.THF_DivisionsIgnore)) or any(map(lambda x: name.find(x) != -1, bb.AHF_DivisionsIgnore)) or any(map(lambda x: name.find(x) != -1, bb.AGHF_DivisionsIgnore))

#------------------------------------------------------------------------------
def getDivisions(season):
    url = "https://gamesheetstats.com/api/useSeasonDivisions/getDivisions/{}".format(season)
    print("Downloading list of divisions...")
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR: failed to read division info: url='{}' status={}".format(url, response.status_code))
        print("Response = " + str(response))
        raise RuntimeError("Failed to get divisions")
    return response.json()

#------------------------------------------------------------------------------
def loadDivisions(season, league, outputsDir):
    divisionsFile = outputsDir + "/divisions.json"
    if not os.path.exists(divisionsFile):
        logging.info("Creating cache of {} divisions ...".format(league))
        data = getDivisions(season)
        with open(divisionsFile, "w") as f:
            json.dump(data, f)

    with open(divisionsFile) as f:
        data = json.load(f)
        return { entry['title'] : entry['id'] for entry in data if not ignoreDivision(entry['title']) }

#------------------------------------------------------------------------------
def populateDivisionsDictionary(season, league):
    configDir  = 'config/{}'.format(bb.getLeagueAbbreviation(league).lower())
    outputsDir = 'results/{}'.format(bb.getLeagueAbbreviation(league).lower())

    divisions  = loadDivisions(season, league, outputsDir)

    returnDivisions = {}
    for division,divisionId in divisions.items():
        divisionName = division.replace(' ', '-').replace("/", '')
        configPrefix = '{}/{}-'.format(configDir, divisionName)
        outputPrefix = '{}/{}-'.format(outputsDir, divisionName)
        returnDivisions[division] = {
            'name'    : division,
            'id'      : divisionId,
            'input'   : {
                'teams'   : configPrefix + "teams.json",
                'filter'  : configPrefix + "filter.txt",
            },
            'output' : {
                'schedule': outputPrefix + "schedule.json",
                'scores'  : outputPrefix + "scores.json",
                'ratings' : outputPrefix + "ratings.md",
            },
        }

    return returnDivisions

#----------------------------------------------------------------------------
def buildScoresUrl(season, divisionId):
    baseURL = API_URL + "/useScoredGames/getSeasonScores"
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(baseURL, season, divisionId)

#----------------------------------------------------------------------------
def buildScheduleUrl(season, divisionId):
    baseURL = API_URL + "/useSchedule/getSeasonSchedule"
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(baseURL, season, divisionId)

#------------------------------------------------------------------------------
def getDivisionScores(season, divisionName, divisionId):
    url = buildScoresUrl(season, divisionId)
    logging.debug("GET: {}".format(url))
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Failed to query '{}' for season={} division={}: status={}".format(url, season, divisionId, response.status_code))
        logging.error("Response = {}".format(str(response)))
        raise RuntimeError("Failed to get scores")
    return response.json()

#------------------------------------------------------------------------------
def getDivisionSchedule(season, divisionName, divisionId):
    url = buildScheduleUrl(season, divisionId)
    logging.debug("GET: {}".format(url))
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("Failed to query '{}' for season={} division={}: status={}".format(url, season, divisionId, response.status_code))
        logging.error("Response = {}".format(str(response)))
        raise RuntimeError("Failed to get schedule")
    return response.json()

#----------------------------------------------------------------------------
def downloadScores(divisionName, SeasonId, Divisions):
    logging.info("Getting scores for division '{}'".format(divisionName))

    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    scores = getDivisionScores(SeasonId, divisionName, info['id'])
    with open(info['output']['scores'], "w") as f:
        json.dump(scores, f)

#----------------------------------------------------------------------------
def downloadSchedule(divisionName, SeasonId, Divisions, force=False):
    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    if force or not os.path.exists(info['schedule']):
        logging.info("Getting schedule for division '{}'".format(divisionName))
        schedule = getDivisionSchedule(SeasonId, divisionName, info['id'])
        with open(info['output']['schedule'], "w") as f:
            json.dump(schedule, f)


