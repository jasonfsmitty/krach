# 10U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1008|Championship|Jersey Shore Wildcats Black|16|16|0|0|0|0|140|14.2|-1.8
2|770|Championship|Metro Militia|17|16|0|1|0|0|102|15.2|-1.3
3|567|Championship|Philadelphia Jr. Flyers|33|30|2|1|0|0|117|28.5|-2.0
4|351|Championship|Wissahickon Warriors Red|34|26|7|0|1|0|292|24.9|-1.6
5|196|Gold|Haverford Hawks Schneider|34|24|10|0|0|0|190|23.3|-0.7
6|174|Gold|NJ Bandits Red|16|10|6|0|0|0|288|9.6|-0.4
7|158|Gold|Frederick Freeze|16|12|3|1|0|0|86|12.6|0.1
8|148|Gold|Igloo Jaguars|36|24|10|1|1|0|158|24.7|-0.3
9|143|Silver|Hollydell Hurricanes|34|23|8|1|2|0|118|24.7|0.2
10|97|Silver|Royals Gray|35|23|12|0|0|0|110|23.6|0.6
11|95|Silver|Delaware Ducks Black|34|19|13|1|1|0|114|20.2|0.2
12|84|Silver|York Devils|35|22|10|3|0|0|84|24.3|0.8
13|63|Bronze|North Jersey Sportscare Kings Yellow|16|6|9|1|0|0|251|6.5|-0.0
14|55|Bronze|Southern Maryland Sabres 10U Black|16|9|7|0|0|0|66|9.3|0.3
15|51|Bronze|Valley Forge Colonials 10U B Skelton|35|15|19|1|0|0|176|15.6|0.1
16|50|Bronze|Lehigh Valley Phantoms|34|18|12|1|3|0|96|21.0|1.0
17|44||Royals Gold|36|15|18|0|3|0|163|16.8|0.3
18|23||Haverford Hawks Wharton|35|15|20|0|0|0|106|15.9|0.9
19|23||Team Philadelphia|35|13|21|0|1|0|79|13.9|0.4
20|21||Lancaster Firebirds|36|10|24|1|1|0|127|11.3|0.3
21|18||Jersey Shore Wildcats Red|15|7|8|0|0|0|45|7.5|0.5
22|13||Tomorrow's Ice North Stars White|16|6|10|0|0|0|47|6.5|0.5
23|12||MYHA 10U B Blue|16|3|13|0|0|0|113|3.1|0.1
24|10||Maryland Jr Black Bears Red|16|3|13|0|0|0|105|3.1|0.1
25|6||Wissahickon Warriors White|34|10|24|0|0|0|78|10.9|0.9
26|6||Rockets Hockey Club White|35|6|28|1|0|0|222|6.9|0.4
27|6||NJ Bandits White|16|5|11|0|0|0|62|5.4|0.4
28|4||Grundy Senators|35|7|27|1|0|0|91|8.2|0.7
29|3||Philadelphia Blazers|35|5|27|1|2|0|126|7.1|0.6
30|0||Valley Forge Colonials 10U B Malik|35|0|35|0|0|0|80|0.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|17.66|1.17
|Avg|0.59|0.04

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 10U-B -o scores_10U-B.md scores_10U-B.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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
| Date Cutoff | 2023-02-08 |

