# 14U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3067|Championship|MYHA 14U B Blue|16|14|0|1|1|0|486|14.0|-1.0
2|2572|Championship|Ashburn Xtreme|16|13|1|2|0|0|393|14.1|-0.9
3|1262|Championship|Frederick Freeze|16|12|3|1|0|0|497|12.6|-0.4
4|1006|Championship|Team Philadelphia|35|24|8|2|1|0|714|25.4|-0.6
5|494|Gold|Wissahickon Warriors|36|22|9|2|3|0|436|24.3|0.3
6|463|Gold|Palmyra Black Knights|36|21|14|1|0|0|725|22.1|0.1
7|416|Gold|Grundy Senators|36|21|9|0|6|0|690|21.1|0.1
8|134|Gold|Maryland Jr Black Bears|16|5|9|1|1|0|351|6.1|0.1
9|105|Silver|North Jersey Skylands Kings|16|5|8|2|0|1|367|7.9|0.4
10|94|Silver|Igloo Jaguars|35|13|20|0|1|1|358|14.0|0.5
11|93|Silver|North Jersey Sportscare Kings|16|2|8|4|2|0|291|6.2|0.2
12|86|Silver|Lehigh Valley Phantoms|35|9|23|2|1|0|598|11.4|0.4
13|86||Hollydell Hurricanes|34|10|21|1|2|0|448|11.4|0.4
14|59||Royals White|36|6|26|2|2|0|719|8.3|0.3
15|33||Jersey Shore Wildcats|15|3|12|0|0|0|208|3.1|0.1
16|32||NJ Bandits|16|1|10|2|3|0|327|3.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|5.99|-0.00
|Avg|0.37|-0.00

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-B -o 14U-B-ratings.md 14U-B-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

