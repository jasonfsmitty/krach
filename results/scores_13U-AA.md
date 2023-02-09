# 13U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|136|Championship|North Jersey Avalanche|16|11|2|2|1|0|47|12.4|-0.6
2|136|Championship|MYHA 14U UA Gold|16|11|2|1|2|0|60|11.5|-0.5
3|107|Championship|Igloo Jaguars|39|30|3|2|4|0|38|30.8|-1.2
4|59|Championship|Rockets Hockey Club Black|38|22|13|2|1|0|62|23.5|-0.5
5|57|Gold|Lehigh Valley Phantoms|40|27|12|1|0|0|46|27.7|-0.3
6|50|Gold|NJ Stars|38|24|8|1|5|0|52|24.7|-0.3
7|30|Gold|Long Island Rebels|16|12|4|0|0|0|12|12.6|0.6
8|13|Gold|Valley Forge Colonials 13U AA|40|16|20|2|2|0|39|18.5|0.5
9|12|Silver|Team Philadelphia|38|14|21|2|1|0|40|16.4|0.4
10|9|Silver|Rockets Hockey Club White|38|14|19|2|3|0|36|16.7|0.7
11|5|Silver|Ashburn Xtreme 2009|16|3|12|0|1|0|75|3.1|0.1
12|4|Silver|Metro Militia|12|4|7|1|0|0|6|5.3|0.3
13|3||Royals 2009|38|5|27|3|3|0|30|8.4|0.4
14|3||Delaware Ducks 13U AA|39|6|27|4|2|0|29|10.5|0.5
15|2||Philadelphia Blazers|36|2|28|4|2|0|28|6.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|7.22|0.40
|Avg|0.48|0.03

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 13U-AA -o scores_13U-AA.md scores_13U-AA.json
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

