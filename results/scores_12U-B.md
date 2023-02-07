# 12U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2172|Championship|Ashburn Xtreme X2|16|14|0|1|1|0|408|13.7|-1.3
2|1825|Championship|Metro Militia|13|12|0|0|1|0|293|11.5|-1.0
3|1117|Championship|Jersey Shore Wildcats Black|16|14|1|1|0|0|334|13.7|-0.8
4|823|Championship|Palmyra Black Knights|35|27|6|1|1|0|381|26.9|-1.1
5|720|Gold|Royals White|35|27|6|0|2|0|336|27.0|-1.0
6|565|Gold|Frederick Freeze|16|14|2|0|0|0|107|14.0|-0.0
7|490|Gold|Valley Forge Colonials 12U B Herhal|34|22|9|1|2|0|422|23.0|-0.5
8|478|Gold|NJ Bandits White|16|10|4|1|1|0|421|10.7|-0.3
9|476|Silver|MYHA 12U B Blue|16|10|6|0|0|0|445|9.8|-0.2
10|263|Silver|Hollydell Hurricanes|34|23|10|1|0|0|303|24.0|0.5
11|200|Silver|Delaware Ducks Black|34|18|13|2|1|0|323|19.8|0.3
12|176|Silver|Royals Gray|34|16|15|1|2|0|364|17.7|0.2
13|122||North Jersey Sportscare Kings Yellow|16|7|8|1|0|0|517|7.5|-0.0
14|120||Lehigh Valley Phantoms|35|16|16|2|1|0|254|18.0|0.5
15|109||Igloo Jaguars|36|18|15|2|1|0|190|20.3|0.8
16|105||Philadelphia Jr Flyers Herold|34|13|19|1|1|0|309|14.2|0.2
17|81||Team Philadelphia|34|13|21|0|0|0|337|13.5|0.5
18|55||Grundy Senators|33|13|18|0|2|0|287|14.8|0.8
19|48||Wissahickon Warriors|37|9|24|2|2|0|322|11.4|0.4
20|22||Tomorrow's Ice North Stars Red|17|2|15|0|0|0|520|2.0|0.0
21|14||Valley Forge Colonials 12U B Fields|34|8|25|1|0|0|202|9.3|0.8
22|8||Jersey Shore Wildcats Red|16|4|11|0|1|0|315|5.1|0.6
23|5||Rockets Hockey Club Grey|35|4|31|0|0|0|341|4.3|0.3
24|3||NJ Stars|33|2|29|2|0|0|252|3.3|0.3
25|2||Philadelphia Jr Flyers Audit|15|1|13|0|1|0|104|1.7|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.77|-0.00
|Avg|0.51|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 12U-B -o scores_12U-B.md scores_12U-B.js
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

