# 18U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1733|Championship|Wissahickon Warriors Red|36|30|3|2|1|0|394|30.3|-1.7
2|1474|Championship|Ashburn Xtreme|17|11|2|4|0|0|293|14.6|-0.4
3|1226|Championship|North Jersey Sportscare Kings Yellow|24|17|4|1|2|0|597|17.3|-0.7
4|1099|Championship|Jersey Shore Wildcats Black|16|12|4|0|0|0|589|11.5|-0.5
5|971|Gold|Palmyra Black Knights|36|27|6|1|2|0|469|27.3|-0.7
6|858|Gold|Philadelphia Blazers|36|25|8|1|2|0|521|25.5|-0.5
7|732|Gold|NJ Bandits|16|10|4|1|1|0|576|10.7|-0.3
8|595|Gold|Lehigh Valley Phantoms 1|36|22|12|2|0|0|532|23.6|-0.4
9|386|Silver|Delaware Ducks|36|18|11|4|3|0|513|22.1|0.1
10|274|Silver|Wissahickon Warriors White|36|22|9|1|4|0|353|23.8|0.8
11|166|Silver|Maryland Jr Black Bears White|16|5|10|0|1|0|760|5.0|-0.0
12|135|Silver|Jersey Shore Wildcats Red|16|7|9|0|0|0|624|7.2|0.2
13|122||Valley Forge Colonials 18U A|36|13|18|2|3|0|523|15.6|0.6
14|119||Grundy Senators Gold|36|13|19|2|2|0|531|15.5|0.5
15|28||York Devils|36|8|26|2|0|0|414|10.9|0.9
16|19||Southern Maryland Sabres 18U Gold|16|4|11|0|1|0|268|4.4|0.4
17|16||Lehigh Valley Phantoms 2|36|5|30|1|0|0|480|6.5|0.5
18|14||Royals|36|7|27|0|2|0|381|7.6|0.6
19|13||Tomorrow's Ice North Stars White|16|0|15|1|0|0|711|1.0|0.0
20|10||The St. James Navy|17|3|14|0|0|0|296|3.3|0.3
21|10||North Jersey Sportscare Kings Grey|24|3|20|0|1|0|369|3.2|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|10.59|-0.00
|Avg|0.50|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 18U-A -o scores_18U-A.md scores_18U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-02-11 |
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
| Date Cutoff | 2023-02-12 |

