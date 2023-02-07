# 16U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1107|Championship|Southern Maryland Sabres 16U Gold|14|12|2|0|0|0|335|11.3|-0.7
2|1024|Championship|Frederick Freeze|16|14|1|1|0|0|204|13.8|-0.7
3|929|Championship|Lancaster Firebirds Black|35|29|3|3|0|0|259|29.1|-1.4
4|826|Championship|Wissahickon Warriors Red|34|27|4|1|2|0|278|27.4|-1.1
5|732|Gold|Delaware Ducks|36|29|4|1|2|0|195|29.6|-0.9
6|711|Gold|Ashburn Xtreme|16|13|3|0|0|0|249|12.6|-0.4
7|571|Gold|Frederick Freeze LA|16|13|2|0|1|0|161|13.3|-0.2
8|565|Gold|Team Philadelphia Orange|34|24|6|4|0|0|256|25.5|-0.5
9|461|Silver|Wissahickon Warriors White|35|23|6|2|4|0|245|25.6|-0.4
10|440|Silver|The St. James White|16|13|3|0|0|0|122|13.1|0.1
11|438|Silver|MYHA 16U UA|16|10|3|1|2|0|324|11.3|-0.2
12|320|Silver|MYHA 16U LA|16|9|4|2|1|0|269|10.5|-0.0
13|291|Bronze|Igloo Jaguars Black|36|24|11|0|1|0|280|24.6|0.1
14|155|Bronze|Valley Forge Colonials 16U A Gold|35|18|15|0|2|0|313|19.3|0.3
15|139|Bronze|Valley Forge Colonials 16U A Silver|36|15|15|2|4|0|271|18.2|0.2
16|137|Bronze|North Jersey Sportscare Kings|24|13|7|2|2|0|153|15.6|0.6
17|114||Lancaster Firebirds Orange|36|17|19|0|0|0|265|17.3|0.3
18|101||Royals Gold|36|14|15|5|2|0|245|18.0|0.5
19|99||Maryland Jr Black Bears White|16|5|7|3|1|0|283|7.2|0.2
20|88||Rockets Hockey Club|35|16|17|1|1|0|211|17.5|0.5
21|82||Maryland Jr Black Bears Red|16|5|9|1|1|0|340|6.1|0.1
22|76||Team Philadelphia Black|34|13|19|0|2|0|281|14.4|0.4
23|71||Haverford Hawks|36|13|20|2|1|0|294|14.9|0.4
24|66||Philadelphia Blazers|34|11|21|1|1|0|294|12.3|0.3
25|57||North Jersey Skylands Kings White|24|9|11|2|2|0|138|11.5|0.5
26|55||Igloo Jaguars Green|35|11|20|3|1|0|232|13.4|0.4
27|46||Hollydell Hurricanes|34|8|23|2|1|0|281|9.7|0.2
28|43||Royals Blue|34|10|20|2|2|0|213|12.4|0.4
29|43||Lehigh Valley Phantoms 1|34|8|20|3|3|0|288|11.3|0.3
30|39||The St. James Navy|16|4|10|1|1|0|254|5.2|0.2
31|26||Grundy Senators|35|4|26|1|4|0|301|6.6|0.1
32|14||Jersey Shore Wildcats Black|16|2|13|0|1|0|169|2.6|0.1
33|12||Lehigh Valley Phantoms 2|34|3|29|1|1|0|250|4.1|0.1
34|7||Jersey Shore Wildcats Red|16|1|14|1|0|0|163|1.6|0.1
35|2||Capital City Vipers|34|1|33|0|0|0|293|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|13.01|-0.15
|Avg|0.37|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --shootout-loss 0.5 --tie 0.5 --min-games 12 -n 16U-A -o scores_16U-A.md scores_16U-A.js
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
| Date Cutoff | 2023-02-07 |

