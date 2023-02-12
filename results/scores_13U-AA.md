# 13U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1365|Championship|MYHA 14U UA Gold|16|11|2|1|2|0|599|11.5|-0.5
2|1353|Championship|North Jersey Avalanche|16|11|2|2|1|0|470|12.4|-0.6
3|1073|Championship|Igloo Jaguars|39|30|3|2|4|0|384|30.8|-1.2
4|593|Championship|Rockets Hockey Club Black|39|23|13|2|1|0|605|24.5|-0.5
5|570|Gold|Lehigh Valley Phantoms|40|27|12|1|0|0|462|27.7|-0.3
6|502|Gold|NJ Stars|38|24|8|1|5|0|516|24.7|-0.3
7|295|Gold|Long Island Rebels|16|12|4|0|0|0|121|12.6|0.6
8|133|Gold|Valley Forge Colonials 13U AA|40|16|20|2|2|0|388|18.5|0.5
9|127|Silver|Team Philadelphia|39|15|21|2|1|0|395|17.5|0.5
10|88|Silver|Rockets Hockey Club White|39|14|20|2|3|0|357|16.7|0.7
11|55|Silver|Ashburn Xtreme 2009|16|3|12|0|1|0|750|3.1|0.1
12|35|Silver|Metro Militia|12|4|7|1|0|0|59|5.3|0.3
13|34||Delaware Ducks 13U AA|39|6|27|4|2|0|285|10.5|0.5
14|27||Royals 2009|38|5|27|3|3|0|302|8.4|0.4
15|19||Philadelphia Blazers|37|2|29|4|2|0|283|6.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|7.33|0.40
|Avg|0.49|0.03

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 13U-AA -o scores_13U-AA.md scores_13U-AA.json
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

