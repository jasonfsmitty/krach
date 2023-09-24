[<- back to the index](readme.md)
# 16U Diamond KRACH Rankings
Rankings generated on Sun Sep 24 18:45:46 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3031|Playoffs|PTL Black|5|5|0|0|0|0|452|5.8|-0.0
2|855|Playoffs|NJ Bandits|4|3|0|0|0|1|303|4.7|0.0
3|628|Playoffs|New York Islanders 1|4|3|1|0|0|0|341|3.9|0.0
4|568|Playoffs|STJ|6|2|3|0|0|1|1245|3.7|-0.0
5|520|Playoffs|MassConn United Hockey Club|4|2|2|0|0|0|1345|2.8|-0.0
6|494|Playoffs|PTL Orange|4|2|1|0|0|1|373|3.7|0.0
7|376||York Lady Devils|3|1|2|0|0|0|821|1.9|0.0
8|129||CT Ice Cats|3|0|3|0|0|0|1119|0.8|-0.0
9|124||Stateline Hawks|3|0|3|0|0|0|652|0.9|0.0
10|83||LVPY|4|0|4|0|0|0|557|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PTL Black|NJ Bandits|New York Islanders 1|STJ|MassConn United Hockey Club|PTL Orange|York Lady Devils|CT Ice Cats|Stateline Hawks|LVPY
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|PTL Black|--| 78%| 83%| 84%| 85%| 86%| 89%| 96%| 96%| 97%
|NJ Bandits| 22%|--| 58%| 60%| 62%| 63%| 69%| 87%| 87%| 91%
|New York Islanders 1| 17%| 42%|--| 53%| 55%| 56%| 63%| 83%| 84%| 88%
|STJ| 16%| 40%| 47%|--| 52%| 53%| 60%| 81%| 82%| 87%
|MassConn United Hockey Club| 15%| 38%| 45%| 48%|--| 51%| 58%| 80%| 81%| 86%
|PTL Orange| 14%| 37%| 44%| 47%| 49%|--| 57%| 79%| 80%| 86%
|York Lady Devils| 11%| 31%| 37%| 40%| 42%| 43%|--| 74%| 75%| 82%
|CT Ice Cats|  4%| 13%| 17%| 19%| 20%| 21%| 26%|--| 51%| 61%
|Stateline Hawks|  4%| 13%| 16%| 18%| 19%| 20%| 25%| 49%|--| 60%
|LVPY|  3%|  9%| 12%| 13%| 14%| 14%| 18%| 39%| 40%|--

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

