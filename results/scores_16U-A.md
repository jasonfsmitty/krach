# 16U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1199|Championship|Frederick Freeze|16|14|1|1|0|0|204|14.1|-0.9
2|1143|Championship|Lancaster Firebirds Black|35|29|3|3|0|0|245|30.1|-1.9
3|1062|Championship|Southern Maryland Sabres 16U Gold|14|12|2|0|0|0|343|11.3|-0.7
4|746|Championship|Team Philadelphia Orange|34|24|6|4|0|0|242|27.1|-0.9
5|743|Gold|Wissahickon Warriors Red|34|27|4|1|2|0|290|27.0|-1.0
6|708|Gold|Ashburn Xtreme|16|13|3|0|0|0|266|12.5|-0.5
7|661|Gold|Delaware Ducks|36|29|4|1|2|0|199|29.2|-0.8
8|451|Gold|Frederick Freeze LA|16|13|2|0|1|0|159|12.9|-0.1
9|408|Silver|The St. James White|16|13|3|0|0|0|107|13.1|0.1
10|386|Silver|Wissahickon Warriors White|35|23|6|2|4|0|249|24.8|-0.2
11|374|Silver|MYHA 16U LA|16|9|4|2|1|0|286|10.9|-0.1
12|361|Silver|MYHA 16U UA|16|10|3|1|2|0|351|10.8|-0.2
13|252|Bronze|Igloo Jaguars Black|36|24|11|0|1|0|281|24.2|0.2
14|138|Bronze|North Jersey Sportscare Kings|24|13|7|2|2|0|157|15.6|0.6
15|131|Bronze|Valley Forge Colonials 16U A Gold|35|18|15|0|2|0|332|18.4|0.4
16|129|Bronze|Maryland Jr Black Bears White|16|5|7|3|1|0|295|8.2|0.2
17|118||Royals Gold|36|14|15|5|2|0|251|19.5|0.5
18|117||Valley Forge Colonials 16U A Silver|36|15|15|2|4|0|268|17.3|0.3
19|107||Lancaster Firebirds Orange|36|17|19|0|0|0|250|17.4|0.4
20|81||Rockets Hockey Club|35|16|17|1|1|0|201|17.6|0.6
21|75||Maryland Jr Black Bears Red|16|5|9|1|1|0|332|6.1|0.1
22|71||Haverford Hawks|36|13|20|2|1|0|307|15.4|0.4
23|63||Team Philadelphia Black|34|13|19|0|2|0|299|13.4|0.4
24|63||Igloo Jaguars Green|35|11|20|3|1|0|230|14.4|0.4
25|62||Philadelphia Blazers|34|11|21|1|1|0|292|12.3|0.3
26|59||North Jersey Skylands Kings White|24|9|11|2|2|0|151|11.5|0.5
27|48||Hollydell Hurricanes|34|8|23|2|1|0|271|10.2|0.2
28|41||Royals Blue|34|10|20|2|2|0|204|12.4|0.4
29|40||Lehigh Valley Phantoms 1|34|8|20|3|3|0|299|11.4|0.4
30|38||The St. James Navy|16|4|10|1|1|0|270|5.2|0.2
31|18||Grundy Senators|35|4|26|1|4|0|300|5.1|0.1
32|12||Lehigh Valley Phantoms 2|34|3|29|1|1|0|238|4.1|0.1
33|10||Jersey Shore Wildcats Red|16|1|14|1|0|0|149|2.1|0.1
34|9||Jersey Shore Wildcats Black|16|2|13|0|1|0|154|2.1|0.1
35|2||Capital City Vipers|34|1|33|0|0|0|308|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|14.42|-0.15
|Avg|0.41|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 16U-A -o scores_16U-A.md scores_16U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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

