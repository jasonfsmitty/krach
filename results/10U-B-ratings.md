# 10U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|9711|Championship|Jersey Shore Wildcats Black|16|16|0|0|0|0|1320|14.3|-1.7
2|8813|Championship|Metro Militia|17|16|0|1|0|0|977|15.4|-1.6
3|5462|Championship|Philadelphia Jr. Flyers|36|31|3|2|0|0|1174|30.8|-2.2
4|3582|Championship|Wissahickon Warriors Red|36|28|7|0|1|0|2938|26.2|-1.8
5|1865|Gold|Frederick Freeze|16|12|3|1|0|0|914|12.9|-0.1
6|1703|Gold|NJ Bandits Red|16|10|6|0|0|0|2767|9.6|-0.4
7|1594|Gold|Haverford Hawks Schneider|36|24|12|0|0|0|1904|23.5|-0.5
8|1468|Gold|Igloo Jaguars|38|25|10|2|1|0|1544|26.7|-0.3
9|1318|Silver|Hollydell Hurricanes|36|25|8|1|2|0|1176|26.2|0.2
10|1075|Silver|York Devils|36|23|10|3|0|0|791|26.7|0.7
11|1007|Silver|Royals Gray|36|24|12|0|0|0|1127|24.6|0.6
12|948|Silver|Delaware Ducks Black|36|20|14|1|1|0|1230|21.2|0.2
13|692|Bronze|North Jersey Sportscare Kings Yellow|16|6|9|1|0|0|2422|7.0|-0.0
14|538|Bronze|Southern Maryland Sabres 10U Black|16|9|7|0|0|0|637|9.3|0.3
15|490|Bronze|Valley Forge Colonials 10U B Skelton|36|15|19|1|1|0|1786|16.2|0.2
16|415|Bronze|Lehigh Valley Phantoms|36|19|13|1|3|0|982|21.1|1.1
17|332||Royals Gold|36|15|18|0|3|0|1608|15.4|0.4
18|204||Haverford Hawks Wharton|36|15|21|0|0|0|1071|15.9|0.9
19|191||Lancaster Firebirds|37|10|25|1|1|0|1226|11.3|0.3
20|188||Team Philadelphia|36|13|22|0|1|0|746|13.5|0.5
21|143||Jersey Shore Wildcats Red|16|7|9|0|0|0|424|7.5|0.5
22|133||Tomorrow's Ice North Stars White|16|6|10|0|0|0|481|6.4|0.4
23|104||MYHA 10U B Blue|16|3|13|0|0|0|1060|3.1|0.1
24|89||Maryland Jr Black Bears Red|16|3|13|0|0|0|938|3.1|0.1
25|80||Rockets Hockey Club White|36|7|28|1|0|0|2150|8.5|0.5
26|71||Wissahickon Warriors White|36|11|25|0|0|0|771|12.0|1.0
27|66||NJ Bandits White|16|5|11|0|0|0|605|5.4|0.4
28|48||Grundy Senators|36|7|28|1|0|0|946|8.7|0.7
29|27||Philadelphia Blazers|36|5|27|1|3|0|1310|6.6|0.6
30|0||Valley Forge Colonials 10U B Malik|36|0|36|0|0|0|834|0.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|18.26|1.11
|Avg|0.61|0.04

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-B -o 10U-B-ratings.md 10U-B-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
| End Date | 2023-02-12 |
| KRACH Method | BRADLEY_TERRY |
| SoS Method | AVERAGE |
| Max Iterations | 10 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.50 |
| Fake Ties | 0 |
| Ignore teams |  |
| Min Games Played | 12 |
| Date Cutoff | 2023-02-12 |

