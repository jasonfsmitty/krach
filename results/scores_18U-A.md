# 18U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1643|Championship|Wissahickon Warriors Red|35|29|3|2|1|0|384|29.4|-1.6
2|1470|Championship|Ashburn Xtreme|17|11|2|4|0|0|297|14.6|-0.4
3|1227|Championship|North Jersey Sportscare Kings Yellow|24|17|4|1|2|0|597|17.3|-0.7
4|1105|Championship|Jersey Shore Wildcats Black|16|12|4|0|0|0|590|11.4|-0.6
5|1040|Gold|Palmyra Black Knights|35|27|5|1|2|0|430|27.3|-0.7
6|858|Gold|Philadelphia Blazers|35|24|8|1|2|0|536|24.4|-0.6
7|727|Gold|NJ Bandits|16|10|4|1|1|0|573|10.7|-0.3
8|652|Gold|Lehigh Valley Phantoms 1|35|22|11|2|0|0|533|23.5|-0.5
9|349|Silver|Delaware Ducks|35|17|11|4|3|0|510|21.2|0.2
10|273|Silver|Wissahickon Warriors White|36|22|9|1|4|0|355|23.8|0.8
11|166|Silver|Maryland Jr Black Bears White|16|5|10|0|1|0|754|5.0|-0.0
12|136|Silver|Jersey Shore Wildcats Red|16|7|9|0|0|0|620|7.2|0.2
13|123||Valley Forge Colonials 18U A|36|13|18|2|3|0|524|15.6|0.6
14|119||Grundy Senators Gold|36|13|19|2|2|0|530|15.5|0.5
15|28||York Devils|35|8|25|2|0|0|403|10.9|0.9
16|19||Southern Maryland Sabres 18U Gold|16|4|11|0|1|0|274|4.4|0.4
17|16||Lehigh Valley Phantoms 2|36|5|30|1|0|0|475|6.5|0.5
18|14||Royals|36|7|27|0|2|0|381|7.7|0.7
19|13||Tomorrow's Ice North Stars White|16|0|15|1|0|0|700|1.0|0.0
20|10||The St. James Navy|17|3|14|0|0|0|302|3.3|0.3
21|10||North Jersey Sportscare Kings Grey|24|3|20|0|1|0|375|3.2|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|10.77|-0.00
|Avg|0.51|-0.00

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

