[<- back to the index](readme.md)
# 14U Diamond KRACH Rankings
Rankings generated on Sun Sep 24 18:45:46 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1321|Playoffs|MYHA Blue|4|3|1|0|0|0|663|3.8|-0.0
2|916|Playoffs|PTL Orange|6|4|2|0|0|0|570|4.9|0.0
3|737|Playoffs|STJ|6|4|2|0|0|0|485|4.9|0.0
4|515|Playoffs|CT Polar Bears|3|2|1|0|0|0|342|2.8|-0.0
5|484||PTL Black|5|2|3|0|0|0|840|2.8|-0.0
6|309||WBS Lady Knights|3|1|2|0|0|0|550|1.9|0.0
7|246||Stateline Hawks|4|1|3|0|0|0|622|1.9|0.0
8|162||NJ Bandits|5|1|4|0|0|0|438|1.8|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA Blue|PTL Orange|STJ|CT Polar Bears|PTL Black|WBS Lady Knights|Stateline Hawks|NJ Bandits
| --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA Blue|--| 59%| 64%| 72%| 73%| 81%| 84%| 89%
|PTL Orange| 41%|--| 55%| 64%| 65%| 75%| 79%| 85%
|STJ| 36%| 45%|--| 59%| 60%| 70%| 75%| 82%
|CT Polar Bears| 28%| 36%| 41%|--| 52%| 62%| 68%| 76%
|PTL Black| 27%| 35%| 40%| 48%|--| 61%| 66%| 75%
|WBS Lady Knights| 19%| 25%| 30%| 38%| 39%|--| 56%| 66%
|Stateline Hawks| 16%| 21%| 25%| 32%| 34%| 44%|--| 60%
|NJ Bandits| 11%| 15%| 18%| 24%| 25%| 34%| 40%|--

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

