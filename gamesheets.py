#!/usr/bin/env python3

import logging
import requests
import datetime
import json
import os
import sys

import blackbear_common as bb
    
#------------------------------------------------------------------------------
def ignoreDivision(name):
    return name.startswith('Mite') or any(map(lambda x: name.find(x) != -1, ['Guest', 'Championship', 'Gold', 'Silver', 'Bronze', 'Super 6', 'Frozen 4']))

#------------------------------------------------------------------------------
def getDivisions(season):
    url = "https://gamesheetstats.com/api/useSeasonDivisions/getDivisions/{}".format(season)
    print("Reading list of divisions...")
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR: failed to read division info: url='{}' status={}".format(url, response.status_code))
        print("Response = " + str(response))
        raise RuntimeError("Failed to get divisions")
    return { entry['title'] : entry['id'] for entry in response.json() if not ignoreDivision(entry['title']) }

#------------------------------------------------------------------------------
def populateDivisionsDictionary(season, league):
	returnDivisions = {}
	divisions = getDivisions(season)
        
	if league == bb.League.THF:
		subfolder = 'thf'
	elif league == bb.League.AHF:
		subfolder = 'ahf'
	elif league == bb.League.AGHF:
		subfolder = 'aghf'
        
	for division in divisions:
		divisionName = division.replace(' ', '-').replace("/", '')
		returnDivision = {}
		returnDivision['id'] = divisions[division]
		returnDivision['scores'] = 'results/{}/{}-scores.json'.format(subfolder, divisionName)
		returnDivision['filter'] = 'results/{}/{}-filter.txt'.format(subfolder, divisionName)
		returnDivision['output'] = 'results/{}/{}-ratings.md'.format(subfolder, divisionName)
		returnDivisions[division] = returnDivision
	
	return returnDivisions

#----------------------------------------------------------------------------
def buildScoresUrl(season, divisionId):
    baseURL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"
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

#----------------------------------------------------------------------------
def downloadScores(divisionName, SeasonId, Divisions):
    logging.info("Getting scores for division '{}'".format(divisionName))

    info = Divisions.get(divisionName, None)
    if not info:
        logging.error("Unknown division '%s'", divisionName)
        sys.exit(1)

    scores = getDivisionScores(SeasonId, divisionName, info['id'])
    with open(info['scores'], "w") as f:
        json.dump(scores, f)