# 10U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1019|Championship|Jersey Shore Wildcats Black|16|16|0|0|0|0|142|14.2|-1.8
2|902|Championship|Metro Militia|17|16|0|1|0|0|99|15.4|-1.6
3|624|Championship|Philadelphia Jr. Flyers|33|30|2|1|0|0|117|28.8|-2.2
4|326|Championship|Wissahickon Warriors Red|34|26|7|0|1|0|294|24.5|-1.5
5|195|Gold|Haverford Hawks Schneider|34|24|10|0|0|0|198|23.4|-0.6
6|194|Gold|Frederick Freeze|16|12|3|1|0|0|94|12.9|-0.1
7|177|Gold|NJ Bandits Red|16|10|6|0|0|0|292|9.6|-0.4
8|149|Gold|Igloo Jaguars|36|24|10|1|1|0|163|24.7|-0.3
9|134|Silver|Hollydell Hurricanes|34|23|8|1|2|0|129|24.2|0.2
10|108|Silver|York Devils|35|22|10|3|0|0|88|25.7|0.7
11|100|Silver|Royals Gray|35|23|12|0|0|0|121|23.5|0.5
12|94|Silver|Delaware Ducks Black|34|19|13|1|1|0|116|20.2|0.2
13|73|Bronze|North Jersey Sportscare Kings Yellow|16|6|9|1|0|0|254|7.0|-0.0
14|55|Bronze|Southern Maryland Sabres 10U Black|16|9|7|0|0|0|66|9.3|0.3
15|53|Bronze|Valley Forge Colonials 10U B Skelton|35|15|19|1|0|0|177|16.2|0.2
16|42|Bronze|Lehigh Valley Phantoms|34|18|12|1|3|0|106|20.1|1.1
17|35||Royals Gold|36|15|18|0|3|0|171|15.4|0.4
18|24||Haverford Hawks Wharton|35|15|20|0|0|0|114|15.9|0.9
19|21||Lancaster Firebirds|36|10|24|1|1|0|132|11.3|0.3
20|21||Team Philadelphia|35|13|21|0|1|0|78|13.5|0.5
21|19||Jersey Shore Wildcats Red|15|7|8|0|0|0|46|7.5|0.5
22|14||Tomorrow's Ice North Stars White|16|6|10|0|0|0|49|6.5|0.5
23|11||MYHA 10U B Blue|16|3|13|0|0|0|108|3.1|0.1
24|9||Maryland Jr Black Bears Red|16|3|13|0|0|0|104|3.1|0.1
25|7||Rockets Hockey Club White|35|6|28|1|0|0|230|7.5|0.5
26|7||NJ Bandits White|16|5|11|0|0|0|59|5.4|0.4
27|6||Wissahickon Warriors White|34|10|24|0|0|0|78|10.9|0.9
28|5||Grundy Senators|35|7|27|1|0|0|97|8.7|0.7
29|3||Philadelphia Blazers|35|5|27|1|2|0|135|6.6|0.6
30|0||Valley Forge Colonials 10U B Malik|35|0|35|0|0|0|86|0.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|18.12|1.08
|Avg|0.60|0.04

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-B -o scores_10U-B.md scores_10U-B.json
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

