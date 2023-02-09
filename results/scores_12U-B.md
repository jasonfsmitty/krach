# 12U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2191|Championship|Ashburn Xtreme X2|16|14|0|1|1|0|416|13.7|-1.3
2|1509|Championship|Metro Militia|13|12|0|0|1|0|320|11.1|-0.9
3|1415|Championship|Jersey Shore Wildcats Black|16|14|1|1|0|0|326|13.9|-1.1
4|829|Championship|Palmyra Black Knights|35|27|6|1|1|0|370|26.9|-1.1
5|634|Gold|Royals White|35|27|6|0|2|0|341|26.2|-0.8
6|567|Gold|Frederick Freeze|16|14|2|0|0|0|104|14.0|-0.0
7|485|Gold|NJ Bandits White|16|10|4|1|1|0|416|10.7|-0.3
8|469|Gold|MYHA 12U B Blue|16|10|6|0|0|0|414|9.8|-0.2
9|461|Silver|Valley Forge Colonials 12U B Herhal|34|22|9|1|2|0|411|22.6|-0.4
10|294|Silver|Hollydell Hurricanes|34|23|10|1|0|0|295|24.4|0.4
11|221|Silver|Delaware Ducks Black|34|18|13|2|1|0|329|20.2|0.2
12|170|Silver|Royals Gray|34|16|15|1|2|0|368|17.2|0.2
13|159||North Jersey Sportscare Kings Yellow|16|7|8|1|0|0|518|7.9|-0.1
14|131||Lehigh Valley Phantoms|35|16|16|2|1|0|256|18.5|0.5
15|121||Igloo Jaguars|36|18|15|2|1|0|209|20.8|0.8
16|108||Philadelphia Jr Flyers Herold|34|13|19|1|1|0|303|14.2|0.2
17|84||Team Philadelphia|34|13|21|0|0|0|345|13.4|0.4
18|49||Wissahickon Warriors|37|9|24|2|2|0|318|11.3|0.3
19|47||Grundy Senators|33|13|18|0|2|0|294|13.8|0.8
20|22||Tomorrow's Ice North Stars Red|17|2|15|0|0|0|484|2.0|0.0
21|16||Valley Forge Colonials 12U B Fields|34|8|25|1|0|0|208|9.8|0.8
22|6||Jersey Shore Wildcats Red|16|4|11|0|1|0|281|4.5|0.5
23|6||Rockets Hockey Club Grey|35|4|31|0|0|0|356|4.3|0.3
24|5||NJ Stars|33|2|29|2|0|0|268|4.4|0.4
25|1||Philadelphia Jr Flyers Audit|15|1|13|0|1|0|110|1.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.12|-0.00
|Avg|0.48|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 12U-B -o scores_12U-B.md scores_12U-B.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

