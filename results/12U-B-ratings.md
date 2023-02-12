# 12U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2193|Championship|Ashburn Xtreme X2|16|14|0|1|1|0|416|13.7|-1.3
2|1528|Championship|Metro Militia|14|13|0|0|1|0|302|12.1|-0.9
3|1414|Championship|Jersey Shore Wildcats Black|16|14|1|1|0|0|327|13.9|-1.1
4|757|Championship|Palmyra Black Knights|36|27|7|1|1|0|382|27.0|-1.0
5|699|Gold|Royals White|37|29|6|0|2|0|344|28.0|-1.0
6|573|Gold|Frederick Freeze|16|14|2|0|0|0|107|14.0|-0.0
7|485|Gold|NJ Bandits White|16|10|4|1|1|0|416|10.7|-0.3
8|476|Gold|Valley Forge Colonials 12U B Herhal|36|24|9|1|2|0|391|24.5|-0.5
9|456|Silver|MYHA 12U B Blue|16|10|6|0|0|0|410|9.8|-0.2
10|298|Silver|Hollydell Hurricanes|35|24|10|1|0|0|288|25.4|0.4
11|199|Silver|Delaware Ducks Black|36|18|15|2|1|0|340|20.2|0.2
12|167|Silver|Royals Gray|34|16|15|1|2|0|361|17.2|0.2
13|160||North Jersey Sportscare Kings Yellow|16|7|8|1|0|0|523|7.9|-0.1
14|131||Lehigh Valley Phantoms|35|16|16|2|1|0|258|18.5|0.5
15|120||Igloo Jaguars|37|18|16|2|1|0|245|20.8|0.8
16|96||Philadelphia Jr Flyers Herold|35|13|20|1|1|0|293|14.3|0.3
17|88||Team Philadelphia|35|14|21|0|0|0|336|14.5|0.5
18|54||Grundy Senators|34|14|18|0|2|0|286|14.8|0.8
19|49||Wissahickon Warriors|37|9|24|2|2|0|316|11.3|0.3
20|22||Tomorrow's Ice North Stars Red|17|2|15|0|0|0|483|2.0|0.0
21|16||Valley Forge Colonials 12U B Fields|36|9|26|1|0|0|198|10.9|0.9
22|6||Rockets Hockey Club Grey|36|4|32|0|0|0|365|4.3|0.3
23|6||Jersey Shore Wildcats Red|16|4|11|0|1|0|285|4.5|0.5
24|4||NJ Stars|34|2|30|2|0|0|269|4.4|0.4
25|1||Philadelphia Jr Flyers Audit|16|1|14|0|1|0|105|1.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.51|0.00
|Avg|0.50|0.00

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 12U-B -o 12U-B-ratings.md 12U-B-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

