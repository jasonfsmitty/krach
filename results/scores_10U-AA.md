# 10U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1704|Championship|Ashburn Xtreme 2012|16|13|2|0|1|0|641|12.2|-0.8
2|1447|Championship|Philadelphia Blazers|37|25|6|5|1|0|548|28.7|-1.3
3|1407|Championship|MYHA 10U AA Blue|16|11|4|1|0|0|670|11.5|-0.5
4|1356|Championship|The St. James Gold|14|12|2|0|0|0|357|11.6|-0.4
5|1188|Gold|Team Philadelphia|37|27|6|2|2|0|555|27.8|-1.2
6|472|Gold|Long Island Rebels|16|9|6|0|1|0|595|8.9|-0.1
7|412|Gold|Lehigh Valley Phantoms|40|23|13|1|3|0|486|24.0|0.0
8|377|Gold|Wissahickon Warriors|36|18|12|3|3|0|523|21.0|0.0
9|346|Silver|Hollydell Hurricanes|38|21|12|3|2|0|359|24.4|0.4
10|336|Silver|Rye Rangers|14|7|5|1|1|0|510|8.1|0.1
11|249|Silver|NJ Stars Black|38|19|12|3|4|0|338|22.5|0.5
12|157|Silver|MYHA 10U AA Gold|16|8|5|0|3|0|330|8.2|0.2
13|140||Valley Forge Colonials 10U AA|40|15|18|3|4|0|408|18.5|0.5
14|136||Palmyra Black Knights|40|12|24|2|2|0|628|14.2|0.2
15|105||North Jersey Skylands Kings Navy|38|13|20|4|1|0|285|17.7|0.7
16|70||PAL Blue Knights|14|4|7|2|1|0|307|6.3|0.3
17|45||North Jersey Avalanche Blue|15|5|8|1|1|0|133|6.4|0.4
18|25||Haverford Hawks|39|6|28|2|3|0|418|8.4|0.4
19|21||Igloo Jaguars|40|7|32|1|0|0|278|8.4|0.4
20|5||Delaware Ducks Maroon|38|2|35|0|1|0|340|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.65|0.00
|Avg|0.43|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-AA -o scores_10U-AA.md scores_10U-AA.json
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

