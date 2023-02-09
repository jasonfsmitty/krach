# 18U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|164|Championship|Wissahickon Warriors Red|35|29|3|2|1|0|38|29.4|-1.6
2|148|Championship|Ashburn Xtreme|17|11|2|4|0|0|30|14.6|-0.4
3|123|Championship|North Jersey Sportscare Kings Yellow|24|17|4|1|2|0|60|17.3|-0.7
4|110|Championship|Jersey Shore Wildcats Black|16|12|4|0|0|0|59|11.4|-0.6
5|104|Gold|Palmyra Black Knights|35|27|5|1|2|0|43|27.3|-0.7
6|85|Gold|Philadelphia Blazers|35|24|8|1|2|0|54|24.4|-0.6
7|73|Gold|NJ Bandits|16|10|4|1|1|0|57|10.7|-0.3
8|65|Gold|Lehigh Valley Phantoms 1|35|22|11|2|0|0|53|23.5|-0.5
9|35|Silver|Delaware Ducks|35|17|11|4|3|0|51|21.2|0.2
10|27|Silver|Wissahickon Warriors White|36|22|9|1|4|0|36|23.8|0.8
11|16|Silver|Maryland Jr Black Bears White|15|4|10|0|1|0|80|4.0|-0.0
12|14|Silver|Jersey Shore Wildcats Red|16|7|9|0|0|0|62|7.2|0.2
13|12||Valley Forge Colonials 18U A|36|13|18|2|3|0|52|15.6|0.6
14|12||Grundy Senators Gold|36|13|19|2|2|0|53|15.5|0.5
15|3||York Devils|35|8|25|2|0|0|40|10.9|0.9
16|2||Lehigh Valley Phantoms 2|35|5|29|1|0|0|48|6.5|0.5
17|2||Southern Maryland Sabres 18U Gold|16|4|11|0|1|0|28|4.4|0.4
18|1||Royals|36|7|27|0|2|0|38|7.6|0.6
19|1||The St. James Navy|17|3|14|0|0|0|30|3.3|0.3
20|1||Tomorrow's Ice North Stars White|16|0|15|1|0|0|70|1.0|0.0
21|1||North Jersey Sportscare Kings Grey|24|3|20|0|1|0|37|3.2|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|10.77|0.00
|Avg|0.51|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 18U-A -o scores_18U-A.md scores_18U-A.json
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

