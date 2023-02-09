# 15U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|5540|Championship|Delaware Ducks|41|33|5|3|0|0|1606|34.6|-1.4
2|2806|Championship|MYHA 16U AA Gold|16|10|3|1|2|0|3422|10.7|-0.3
3|2122|Championship|Team Philadelphia|39|24|10|3|2|0|2043|27.0|-0.0
4|1539|Championship|Long Island Rebels|20|7|10|3|0|0|3700|9.9|-0.1
5|1464||Royals|40|22|11|3|4|0|2426|25.3|0.3
6|236||NJ Bandits|34|11|19|1|3|0|1995|12.9|0.9
7|164||Palmyra Black Knights|40|10|25|1|4|0|2190|11.7|0.7
8|115||North Jersey Sportscare Kings Yellow|24|5|16|1|2|0|1111|6.5|0.5
9|60||Tomorrow's Ice Selects|39|1|33|3|2|0|1971|4.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|4.48|0.79
|Avg|0.50|0.09

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 15U-AA -o scores_15U-AA.md scores_15U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-02-05 |
| KRACH Method | BRADLEY_TERRY |
| SoS Method | AVERAGE |
| Max Iterations | 10 |
| Max Ratings Diff | 0.0001 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.50 |
| Fake Ties | 0 |
| Ignore teams |  |
| Min Games Played | 12 |
| Date Cutoff | 2023-02-09 |

