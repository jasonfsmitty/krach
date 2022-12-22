#!/bin/bash

BASE_URL="https://gamesheetstats.com/api/useScoredGames/getSeasonScores"
SEASON="1654"
DIVISION="9619"
QUERY_URL="${BASE_URL}/${SEASON}?filter[divisions]=${DIVISION}&filter=[gametype]=overall&filter[limit]=0"

wget -O scores.js "${QUERY_URL}"

