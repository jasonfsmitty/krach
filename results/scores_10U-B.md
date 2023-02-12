# 10U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|9901|Championship|Jersey Shore Wildcats Black|16|16|0|0|0|0|1345|14.3|-1.7
2|8901|Championship|Metro Militia|17|16|0|1|0|0|985|15.4|-1.6
3|5456|Championship|Philadelphia Jr. Flyers|35|30|3|2|0|0|1199|29.9|-2.1
4|3487|Championship|Wissahickon Warriors Red|35|27|7|0|1|0|2980|25.3|-1.7
5|1894|Gold|Frederick Freeze|16|12|3|1|0|0|926|12.9|-0.1
6|1743|Gold|NJ Bandits Red|16|10|6|0|0|0|2814|9.6|-0.4
7|1728|Gold|Haverford Hawks Schneider|35|24|11|0|0|0|1876|23.5|-0.5
8|1468|Gold|Igloo Jaguars|37|24|10|2|1|0|1583|25.7|-0.3
9|1324|Silver|Hollydell Hurricanes|35|24|8|1|2|0|1221|25.2|0.2
10|1094|Silver|York Devils|36|23|10|3|0|0|797|26.7|0.7
11|1023|Silver|Royals Gray|36|24|12|0|0|0|1144|24.6|0.6
12|999|Silver|Delaware Ducks Black|35|20|13|1|1|0|1124|21.2|0.2
13|704|Bronze|North Jersey Sportscare Kings Yellow|16|6|9|1|0|0|2451|7.0|-0.0
14|552|Bronze|Southern Maryland Sabres 10U Black|16|9|7|0|0|0|657|9.3|0.3
15|506|Bronze|Valley Forge Colonials 10U B Skelton|36|15|19|1|1|0|1811|16.1|0.1
16|396|Bronze|Lehigh Valley Phantoms|35|18|13|1|3|0|1014|20.1|1.1
17|344||Royals Gold|36|15|18|0|3|0|1630|15.4|0.4
18|207||Haverford Hawks Wharton|36|15|21|0|0|0|1082|15.9|0.9
19|204||Team Philadelphia|35|13|21|0|1|0|771|13.5|0.5
20|197||Lancaster Firebirds|37|10|25|1|1|0|1243|11.3|0.3
21|147||Jersey Shore Wildcats Red|16|7|9|0|0|0|429|7.5|0.5
22|136||Tomorrow's Ice North Stars White|16|6|10|0|0|0|488|6.4|0.4
23|108||MYHA 10U B Blue|16|3|13|0|0|0|1077|3.1|0.1
24|92||Maryland Jr Black Bears Red|16|3|13|0|0|0|964|3.1|0.1
25|83||Rockets Hockey Club White|36|7|28|1|0|0|2179|8.5|0.5
26|73||Wissahickon Warriors White|35|11|24|0|0|0|756|12.0|1.0
27|68||NJ Bandits White|16|5|11|0|0|0|604|5.4|0.4
28|49||Grundy Senators|35|7|27|1|0|0|941|8.7|0.7
29|27||Philadelphia Blazers|36|5|27|1|3|0|1320|6.6|0.6
30|0||Valley Forge Colonials 10U B Malik|36|0|36|0|0|0|840|0.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|18.01|1.10
|Avg|0.60|0.04

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-B -o scores_10U-B.md scores_10U-B.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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

