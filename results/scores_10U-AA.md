# 10U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1705|Championship|Ashburn Xtreme 2012|16|13|2|0|1|0|644|12.2|-0.8
2|1446|Championship|Philadelphia Blazers|37|25|6|5|1|0|549|28.7|-1.3
3|1407|Championship|MYHA 10U AA Blue|16|11|4|1|0|0|673|11.5|-0.5
4|1349|Championship|The St. James Gold|14|12|2|0|0|0|356|11.6|-0.4
5|1221|Gold|Team Philadelphia|38|28|6|2|2|0|548|28.7|-1.3
6|471|Gold|Long Island Rebels|16|9|6|0|1|0|598|8.9|-0.1
7|410|Gold|Lehigh Valley Phantoms|40|23|13|1|3|0|487|24.0|0.0
8|362|Gold|Wissahickon Warriors|37|18|13|3|3|0|543|21.0|-0.0
9|345|Silver|Hollydell Hurricanes|38|21|12|3|2|0|359|24.4|0.4
10|336|Silver|Rye Rangers|14|7|5|1|1|0|513|8.1|0.1
11|248|Silver|NJ Stars Black|38|19|12|3|4|0|338|22.5|0.5
12|157|Silver|MYHA 10U AA Gold|16|8|5|0|3|0|329|8.2|0.2
13|140||Valley Forge Colonials 10U AA|40|15|18|3|4|0|409|18.5|0.5
14|135||Palmyra Black Knights|40|12|24|2|2|0|628|14.2|0.2
15|105||North Jersey Skylands Kings Navy|38|13|20|4|1|0|283|17.7|0.7
16|70||PAL Blue Knights|14|4|7|2|1|0|309|6.3|0.3
17|45||North Jersey Avalanche Blue|15|5|8|1|1|0|132|6.4|0.4
18|25||Haverford Hawks|39|6|28|2|3|0|419|8.4|0.4
19|21||Igloo Jaguars|40|7|32|1|0|0|280|8.4|0.4
20|5||Delaware Ducks Maroon|38|2|35|0|1|0|340|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.78|0.00
|Avg|0.44|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-AA -o scores_10U-AA.md scores_10U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
| End Date | 2023-02-08 |
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

