# 13U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1361|Championship|MYHA 14U UA Gold|16|11|2|1|2|0|598|11.5|-0.5
2|1356|Championship|North Jersey Avalanche|16|11|2|2|1|0|470|12.4|-0.6
3|1075|Championship|Igloo Jaguars|39|30|3|2|4|0|384|30.8|-1.2
4|590|Championship|Rockets Hockey Club Black|38|22|13|2|1|0|620|23.5|-0.5
5|570|Gold|Lehigh Valley Phantoms|40|27|12|1|0|0|461|27.7|-0.3
6|502|Gold|NJ Stars|38|24|8|1|5|0|516|24.7|-0.3
7|298|Gold|Long Island Rebels|16|12|4|0|0|0|122|12.6|0.6
8|134|Gold|Valley Forge Colonials 13U AA|40|16|20|2|2|0|388|18.5|0.5
9|119|Silver|Team Philadelphia|38|14|21|2|1|0|403|16.4|0.4
10|95|Silver|Rockets Hockey Club White|38|14|19|2|3|0|363|16.7|0.7
11|54|Silver|Ashburn Xtreme 2009|16|3|12|0|1|0|749|3.1|0.1
12|35|Silver|Delaware Ducks 13U AA|39|6|27|4|2|0|286|10.5|0.5
13|35||Metro Militia|12|4|7|1|0|0|60|5.3|0.3
14|28||Royals 2009|38|5|27|3|3|0|303|8.4|0.4
15|19||Philadelphia Blazers|36|2|28|4|2|0|275|6.3|0.3

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

