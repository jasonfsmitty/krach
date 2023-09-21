[<- back to the index](readme.md)
# 16U Diamond KRACH Rankings
Rankings generated on Thu Sep 21 00:11:30 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3076|Playoffs|PTL Black|4|4|0|0|0|0|553|4.8|-0.0
2|711|Playoffs|NJ Bandits|3|2|0|0|0|1|314|3.7|0.0
3|588|Playoffs|STJ|4|1|2|0|0|1|1534|2.7|-0.0
4|572|Playoffs|MassConn United Hockey Club|4|2|2|0|0|0|1380|2.8|-0.0
5|537||PTL Orange|4|2|1|0|0|1|400|3.7|-0.0
6|413||York Lady Devils|3|1|2|0|0|0|902|1.9|0.0
7|90||LVPY|4|0|4|0|0|0|589|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PTL Black|NJ Bandits|STJ|MassConn United Hockey Club|PTL Orange|York Lady Devils|LVPY
| --: | --: | --: | --: | --: | --: | --: | --: 
|PTL Black|--| 81%| 84%| 84%| 85%| 88%| 97%
|NJ Bandits| 19%|--| 55%| 55%| 57%| 63%| 89%
|STJ| 16%| 45%|--| 51%| 52%| 59%| 87%
|MassConn United Hockey Club| 16%| 45%| 49%|--| 52%| 58%| 86%
|PTL Orange| 15%| 43%| 48%| 48%|--| 57%| 86%
|York Lady Devils| 12%| 37%| 41%| 42%| 43%|--| 82%
|LVPY|  3%| 11%| 13%| 14%| 14%| 18%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-09 |
| End Date | 2023-09-17 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

