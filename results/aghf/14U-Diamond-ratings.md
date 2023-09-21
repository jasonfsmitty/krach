[<- back to the index](readme.md)
# 14U Diamond KRACH Rankings
Rankings generated on Thu Sep 21 00:11:30 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1099|Playoffs|PTL Orange|6|4|2|0|0|0|663|4.9|0.0
2|724|Playoffs|STJ|6|4|2|0|0|0|516|4.9|0.0
3|552|Playoffs|PTL Black|3|1|2|0|0|0|1216|1.8|-0.0
4|448|Playoffs|Stateline Hawks|3|1|2|0|0|0|794|1.9|0.0
5|363||NJ Bandits|4|1|3|0|0|0|954|1.8|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PTL Orange|STJ|PTL Black|Stateline Hawks|NJ Bandits
| --: | --: | --: | --: | --: | --: 
|PTL Orange|--| 60%| 67%| 71%| 75%
|STJ| 40%|--| 57%| 62%| 67%
|PTL Black| 33%| 43%|--| 55%| 60%
|Stateline Hawks| 29%| 38%| 45%|--| 55%
|NJ Bandits| 25%| 33%| 40%| 45%|--

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

