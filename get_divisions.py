#!/usr/bin/env python3

import requests
import datetime
import json
import os
from enum import Enum

#----------------------------------------------------------------------------
class League(Enum):
    THF = 1
    AHF = 2
    AGHF = 3

#------------------------------------------------------------------------------
def buildUrl(season, divisionId):
    baseURL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(baseURL, season, divisionId)

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
def populateDivisionsDictionary(season, league=League.THF):
	returnDivisions = {}
	divisions = getDivisions(season)

	if league == League.THF:
		subfolder = 'thf'
	elif league == League.AHF:
		subfolder = 'ahf'
	elif league == League.AGHF:
		subfolder = 'aghf'
        
	for division in divisions:
		divisionName = division.replace(' ', '-').replace("/", '')
		returnDivision = {}
		returnDivision['id'] = divisions[division]
		returnDivision['scores'] = 'results/{}/{}-scores.json'.format(subfolder, divisionName)
		returnDivision['filter'] = 'results/{}/{}-filter.txt'.format(subfolder, divisionName)
		returnDivision['output'] = 'results/{}/{}-ratings.txt'.format(subfolder, divisionName)
		returnDivisions[division] = returnDivision
        
	return returnDivisions


#------------------------------------------------------------------------------
if __name__ == "__main__":
    SEASON = 1654
    DIVISIONS = populateDivisionsDictionary(SEASON)
    print(DIVISIONS)

        
    '''
	divisions = getDivisions(SEASON)
    names = sorted(divisions.keys())
    print("DIVISIONS = {")
    for name in names:
        name = name.replace(' - ', ' ')
        scoreName = name
        if any(map(lambda x: name.find(x) != -1, ['Gretzky', 'Lemieux'])):
            tokens = name.split(' ')
            scoreName = " ".join(tokens[0:2])
            name = " ".join(tokens[0:3])
        elif 'Championship' in name:
            continue

        print("    '{}' : {{".format(name))
        print("        'id'     : {},".format(divisions[scoreName]))
        print("        'scores' : 'results/{}-scores.json',".format(scoreName.replace(' ', '-')))
        print("        'filter' : 'results/{}-filter.txt',".format(name.replace(' ', '-')))
        print("        'output' : 'results/{}-ratings.txt',".format(name.replace(' ', '-')))
        print("    },")
    print("}")
	'''
