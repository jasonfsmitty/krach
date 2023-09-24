[<- back to the index](readme.md)
# 14U Diamond KRACH Rankings
Rankings generated on Sun Sep 24 21:44:28 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1316|Playoffs|[MYHA Blue](https://gamesheetstats.com/seasons/3663/teams/140816/schedule)|4|3|1|0|0|0|660|3.8|-0.0
2|1035|Playoffs|[PTL Orange](https://gamesheetstats.com/seasons/3663/teams/140821/schedule)|6|4|2|0|0|0|640|4.9|0.0
3|834|Playoffs|[STJ](https://gamesheetstats.com/seasons/3663/teams/140822/schedule)|6|4|2|0|0|0|552|4.9|0.0
4|494|Playoffs|[CT Polar Bears](https://gamesheetstats.com/seasons/3663/teams/140818/schedule)|3|2|1|0|0|0|332|2.8|-0.0
5|473||[PTL Black](https://gamesheetstats.com/seasons/3663/teams/140815/schedule)|5|2|3|0|0|0|832|2.8|-0.0
6|409||[WBS Lady Knights](https://gamesheetstats.com/seasons/3663/teams/140825/schedule)|4|2|2|0|0|0|505|2.9|0.0
7|340||[Stateline Hawks](https://gamesheetstats.com/seasons/3663/teams/140813/schedule)|5|2|3|0|0|0|573|2.9|0.0
8|328||[CT Ice Cats](https://gamesheetstats.com/seasons/3663/teams/140826/schedule)|3|1|2|0|0|0|567|1.9|0.0
9|144||[NJ Bandits](https://gamesheetstats.com/seasons/3663/teams/140828/schedule)|6|1|5|0|0|0|455|1.8|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA Blue|PTL Orange|STJ|CT Polar Bears|PTL Black|WBS Lady Knights|Stateline Hawks|CT Ice Cats|NJ Bandits
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA Blue|--| 56%| 61%| 73%| 74%| 76%| 79%| 80%| 90%
|PTL Orange| 44%|--| 55%| 68%| 69%| 72%| 75%| 76%| 88%
|STJ| 39%| 45%|--| 63%| 64%| 67%| 71%| 72%| 85%
|CT Polar Bears| 27%| 32%| 37%|--| 51%| 55%| 59%| 60%| 77%
|PTL Black| 26%| 31%| 36%| 49%|--| 54%| 58%| 59%| 77%
|WBS Lady Knights| 24%| 28%| 33%| 45%| 46%|--| 55%| 55%| 74%
|Stateline Hawks| 21%| 25%| 29%| 41%| 42%| 45%|--| 51%| 70%
|CT Ice Cats| 20%| 24%| 28%| 40%| 41%| 45%| 49%|--| 69%
|NJ Bandits| 10%| 12%| 15%| 23%| 23%| 26%| 30%| 31%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-09 |
| End Date | 2023-09-24 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

