# 14U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|336|Championship|MYHA 14U B Blue|16|14|0|1|1|0|53|13.9|-1.1
2|199|Championship|Ashburn Xtreme|16|13|1|2|0|0|44|13.4|-0.6
3|120|Championship|Frederick Freeze|16|12|3|1|0|0|56|12.2|-0.3
4|99|Championship|Team Philadelphia|34|23|8|2|1|0|74|24.0|-0.5
5|69|Gold|Grundy Senators|36|21|9|0|6|0|69|23.8|-0.2
6|56|Gold|Wissahickon Warriors|35|21|9|2|3|0|44|23.7|0.2
7|47|Gold|Palmyra Black Knights|36|21|14|1|0|0|75|21.6|0.1
8|15|Gold|Maryland Jr Black Bears|16|5|9|1|1|0|40|6.1|0.1
9|10|Silver|Hollydell Hurricanes|33|10|20|1|2|0|46|11.9|0.4
10|9|Silver|Igloo Jaguars|33|11|20|0|1|1|42|12.5|0.5
11|9|Silver|Lehigh Valley Phantoms|34|9|22|2|1|0|60|10.8|0.3
12|8|Silver|North Jersey Skylands Kings|16|5|8|2|0|1|39|6.8|0.3
13|8||North Jersey Sportscare Kings|15|2|7|4|2|0|35|5.2|0.2
14|6||Royals White|35|6|25|2|2|0|70|8.3|0.3
15|4||NJ Bandits|16|1|10|2|3|0|33|3.6|0.1
16|3||Jersey Shore Wildcats|15|3|12|0|0|0|25|3.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|5.24|-0.00
|Avg|0.33|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --shootout-loss 0.5 --tie 0.5 --min-games 12 -n 14U-B -o scores_14U-B.md scores_14U-B.js
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

