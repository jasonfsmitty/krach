#!/usr/bin/env python3

import requests
import datetime
import json
import os

#------------------------------------------------------------------------------
def buildUrl(season, divisionId):
    baseURL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(baseURL, season, divisionId)

#------------------------------------------------------------------------------
def getDivisionScores(season, divisionName, divisionId):
    url = buildUrl(season, divisionId)
    print("Getting scores for division {}".format(divisionName))
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR: failed to query '{}' for season={} division={}: status={}".format(url, season, divisionId, response.status_code))
        print("Response = {}".format(str(response)))
        raise RuntimeError("Failed to get scores")
    return response.json()

#------------------------------------------------------------------------------
# Date of the scoring data is based on the latest date of all game data.
def getDate(scores):
    #print(scores)
    latestDate = None
    for key in scores:
        for page in scores[key]:
            tokens = page.get('date', "").split('-')
            if len(tokens) == 2:
                dateStr = tokens[0].strip()
                dt = datetime.datetime.strptime(tokens[0].strip(), "%a, %b %d, %Y")
                if not latestDate or (latestDate < dt):
                    latestDate = dt
    return latestDate

#------------------------------------------------------------------------------
def filename(divisionName, scores):
    return "scores_{}.js".format(divisionName.replace(' ', '-'))

#------------------------------------------------------------------------------
def saveToFile(divisionName, scores):
    with open(filename(divisionName, scores), "w") as f:
        json.dump(scores, f)

#------------------------------------------------------------------------------
def ignoreDivision(name):
    return name.startswith('Mite') or any(map(lambda x: name.find(x) != -1, ['Guest', 'Championship', 'Gold', 'Silver', 'Bronze']))

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
if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    os.chdir("results")

    season = 1654 # Hard-coded for the 2022-2023 season
    divisions = getDivisions(season)
    print("Found {} divisions.".format(len(divisions)))

    for divisionName, divisionId in divisions.items():
        scores = getDivisionScores(season, divisionName, divisionId)
        saveToFile(divisionName, scores)

