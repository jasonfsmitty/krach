# 12U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2196|Championship|Ashburn Xtreme X2|16|14|0|1|1|0|417|13.7|-1.3
2|1532|Championship|Metro Militia|14|13|0|0|1|0|305|12.1|-0.9
3|1408|Championship|Jersey Shore Wildcats Black|16|14|1|1|0|0|326|13.9|-1.1
4|820|Championship|Palmyra Black Knights|35|27|6|1|1|0|370|26.9|-1.1
5|651|Gold|Royals White|36|28|6|0|2|0|335|27.2|-0.8
6|566|Gold|Frederick Freeze|16|14|2|0|0|0|103|14.0|-0.0
7|485|Gold|NJ Bandits White|16|10|4|1|1|0|418|10.7|-0.3
8|476|Gold|Valley Forge Colonials 12U B Herhal|35|23|9|1|2|0|404|23.6|-0.4
9|456|Silver|MYHA 12U B Blue|16|10|6|0|0|0|412|9.8|-0.2
10|296|Silver|Hollydell Hurricanes|35|24|10|1|0|0|288|25.4|0.4
11|198|Silver|Delaware Ducks Black|36|18|15|2|1|0|340|20.2|0.2
12|167|Silver|Royals Gray|34|16|15|1|2|0|366|17.2|0.2
13|160||North Jersey Sportscare Kings Yellow|16|7|8|1|0|0|522|7.9|-0.1
14|130||Lehigh Valley Phantoms|35|16|16|2|1|0|257|18.5|0.5
15|119||Igloo Jaguars|37|18|16|2|1|0|245|20.8|0.8
16|96||Philadelphia Jr Flyers Herold|35|13|20|1|1|0|294|14.3|0.3
17|87||Team Philadelphia|35|14|21|0|0|0|336|14.5|0.5
18|53||Grundy Senators|34|14|18|0|2|0|287|14.8|0.8
19|48||Wissahickon Warriors|37|9|24|2|2|0|317|11.3|0.3
20|22||Tomorrow's Ice North Stars Red|17|2|15|0|0|0|486|2.0|0.0
21|15||Valley Forge Colonials 12U B Fields|35|8|26|1|0|0|203|9.8|0.8
22|6||Jersey Shore Wildcats Red|16|4|11|0|1|0|284|4.5|0.5
23|6||Rockets Hockey Club Grey|35|4|31|0|0|0|357|4.3|0.3
24|4||NJ Stars|34|2|30|2|0|0|268|4.4|0.4
25|1||Philadelphia Jr Flyers Audit|15|1|13|0|1|0|110|1.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.31|-0.00
|Avg|0.49|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 12U-B -o scores_12U-B.md scores_12U-B.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

