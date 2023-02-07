# 15U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|495|Championship|Delaware Ducks|41|33|5|3|0|0|154|33.5|-1.0
2|372|Championship|MYHA 16U AA Gold|16|10|3|1|2|0|300|11.2|-0.3
3|217|Championship|Team Philadelphia|39|24|10|3|2|0|183|26.6|0.1
4|180|Championship|Royals|40|22|11|3|4|0|271|25.7|0.2
5|122||Long Island Rebels|20|7|10|3|0|0|345|8.5|-0.0
6|36||NJ Bandits|34|11|19|1|3|0|192|13.7|0.7
7|26||Palmyra Black Knights|40|10|25|1|4|0|188|13.0|0.5
8|18||North Jersey Sportscare Kings Yellow|24|5|16|1|2|0|115|6.9|0.4
9|7||Tomorrow's Ice Selects|39|1|33|3|2|0|219|3.7|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|3.32|0.71
|Avg|0.37|0.08

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 15U-AA -o scores_15U-AA.md scores_15U-AA.js
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-02-05 |
| KRACH Method | BRADLEY_TERRY |
| SoS Method | AVERAGE |
| Max Iterations | 10 |
| Max Ratings Diff | 0.0001 |
| Shootout Win Value | 0.50 |
| Shootout Loss Value | 0.50 |
| Tie Value | 0.50 |
| Fake Ties | 0 |
| Ignore teams |  |
| Min Games Played | 12 |
| Date Cutoff | 2023-02-07 |

