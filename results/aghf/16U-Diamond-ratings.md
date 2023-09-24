[<- back to the index](readme.md)
# 16U Diamond KRACH Rankings
Rankings generated on Sun Sep 24 21:44:28 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2958|Playoffs|[PTL Black](https://gamesheetstats.com/seasons/3663/teams/140833/schedule)|5|5|0|0|0|0|441|5.8|-0.0
2|864|Playoffs|[NJ Bandits](https://gamesheetstats.com/seasons/3663/teams/140836/schedule)|4|3|0|0|0|1|306|4.7|0.0
3|645|Playoffs|[New York Islanders 1](https://gamesheetstats.com/seasons/3663/teams/140847/schedule)|4|3|1|0|0|0|354|3.9|0.0
4|599|Playoffs|[STJ](https://gamesheetstats.com/seasons/3663/teams/140841/schedule)|6|2|3|0|0|1|1249|3.7|-0.0
5|566|Playoffs|[PTL Orange](https://gamesheetstats.com/seasons/3663/teams/140842/schedule)|5|3|1|0|0|1|340|4.7|-0.0
6|474|Playoffs|[MassConn United Hockey Club](https://gamesheetstats.com/seasons/3663/teams/140835/schedule)|4|2|2|0|0|0|1303|2.8|-0.0
7|377||[York Lady Devils](https://gamesheetstats.com/seasons/3663/teams/140845/schedule)|3|1|2|0|0|0|822|1.9|0.0
8|128||[Stateline Hawks](https://gamesheetstats.com/seasons/3663/teams/140840/schedule)|3|0|3|0|0|0|675|0.9|0.0
9|98||[CT Ice Cats](https://gamesheetstats.com/seasons/3663/teams/140846/schedule)|4|0|4|0|0|0|975|0.8|-0.0
10|84||[LVPY](https://gamesheetstats.com/seasons/3663/teams/140844/schedule)|4|0|4|0|0|0|565|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PTL Black|NJ Bandits|New York Islanders 1|STJ|PTL Orange|MassConn United Hockey Club|York Lady Devils|Stateline Hawks|CT Ice Cats|LVPY
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|PTL Black|--| 77%| 82%| 83%| 84%| 86%| 89%| 96%| 97%| 97%
|NJ Bandits| 23%|--| 57%| 59%| 60%| 65%| 70%| 87%| 90%| 91%
|New York Islanders 1| 18%| 43%|--| 52%| 53%| 58%| 63%| 83%| 87%| 88%
|STJ| 17%| 41%| 48%|--| 51%| 56%| 61%| 82%| 86%| 88%
|PTL Orange| 16%| 40%| 47%| 49%|--| 54%| 60%| 82%| 85%| 87%
|MassConn United Hockey Club| 14%| 35%| 42%| 44%| 46%|--| 56%| 79%| 83%| 85%
|York Lady Devils| 11%| 30%| 37%| 39%| 40%| 44%|--| 75%| 79%| 82%
|Stateline Hawks|  4%| 13%| 17%| 18%| 18%| 21%| 25%|--| 57%| 60%
|CT Ice Cats|  3%| 10%| 13%| 14%| 15%| 17%| 21%| 43%|--| 54%
|LVPY|  3%|  9%| 12%| 12%| 13%| 15%| 18%| 40%| 46%|--

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

