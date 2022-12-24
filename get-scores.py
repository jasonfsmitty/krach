#!/usr/bin/env python3

import requests
import datetime
import json

BASE_URL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"

def buildUrl(season, division):
    return "{}/{}?filter[divisions]={}&filter=[gametype]=overall&filter[limit]=0".format(BASE_URL, season[1], division[1])

def getDivisionScores(season, division):
    url = buildUrl(season, division)
    print("GET: {}".format(url))
    response = requests.get(url)
    if response.status_code != 200:
        print("ERROR: failed to query '{}' for season={} division={}: status={}".format(url, season[0], division[0], response.status_code))
        print("Response = {}".format(str(response)))
        raise RuntimeError("Failed to get scores")
    return response.json()

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

def filename(season, division, scores):
    dt = getDate(scores)
    dateStr = dt.strftime("%Y-%m-%d")
    return "{}-scores-{}.js".format(dateStr, division[0])

def saveToFile(season, division, scores):
    with open(filename(season, division, scores), "w") as f:
        json.dump(scores, f)

if __name__ == "__main__":
    seasons = [ ("2022", 1654) ]
    divisions = [
        ("14U_AA", 9619),
    ]
    for season in seasons:
        for division in divisions:
            scores = getDivisionScores(season, division)
            saveToFile(season, division, scores)
