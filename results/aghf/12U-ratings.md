[<- back to the index](readme.md)
# 12U KRACH Rankings
Rankings generated on Thu Sep 21 00:11:30 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3111|Playoffs|STJ|4|4|0|0|0|0|508|4.8|-0.0
2|504|Playoffs|WBS Lady Knights|5|1|4|0|0|0|2048|1.8|-0.0
3|263|Playoffs|LVPY|3|0|3|0|0|0|1933|0.8|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||STJ|WBS Lady Knights|LVPY
| --: | --: | --: | --: 
|STJ|--| 86%| 92%
|WBS Lady Knights| 14%|--| 66%
|LVPY|  8%| 34%|--

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

