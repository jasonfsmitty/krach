# 14U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3067|Championship|MYHA 14U B Blue|16|14|0|1|1|0|485|14.0|-1.0
2|2584|Championship|Ashburn Xtreme|16|13|1|2|0|0|392|14.1|-0.9
3|1259|Championship|Frederick Freeze|16|12|3|1|0|0|495|12.6|-0.4
4|1004|Championship|Team Philadelphia|34|23|8|2|1|0|733|24.4|-0.6
5|480|Gold|Wissahickon Warriors|35|21|9|2|3|0|446|23.3|0.3
6|461|Gold|Palmyra Black Knights|36|21|14|1|0|0|723|22.1|0.1
7|416|Gold|Grundy Senators|36|21|9|0|6|0|689|21.2|0.2
8|133|Gold|Maryland Jr Black Bears|16|5|9|1|1|0|347|6.1|0.1
9|108|Silver|North Jersey Sportscare Kings|15|2|7|4|2|0|301|6.2|0.2
10|106|Silver|North Jersey Skylands Kings|16|5|8|2|0|1|366|7.9|0.4
11|93|Silver|Lehigh Valley Phantoms|34|9|22|2|1|0|612|11.4|0.4
12|88|Silver|Hollydell Hurricanes|33|10|20|1|2|0|445|11.4|0.4
13|80||Igloo Jaguars|33|11|20|0|1|1|373|11.9|0.4
14|59||Royals White|35|6|25|2|2|0|710|8.3|0.3
15|32||Jersey Shore Wildcats|15|3|12|0|0|0|205|3.1|0.1
16|32||NJ Bandits|16|1|10|2|3|0|327|3.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|5.86|0.00
|Avg|0.37|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-B -o scores_14U-B.md scores_14U-B.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

