# 18U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1623|Championship|Philadelphia Blazers|39|33|1|3|2|0|350|33.1|-2.9
2|1172|Championship|MYHA 18U AA Blue|16|9|4|3|0|0|649|11.1|-0.9
3|944|Championship|Ashburn Xtreme|16|9|4|3|0|0|527|11.3|-0.7
4|697|Championship|Team Philadelphia|39|28|9|2|0|0|383|28.9|-1.1
5|529|Gold|Long Island Rebels|15|9|5|1|0|0|421|9.8|-0.2
6|454|Gold|Igloo Jaguars Black|40|27|9|0|4|0|402|26.5|-0.5
7|231|Gold|Metro Militia|16|9|5|2|0|0|183|11.4|0.4
8|231|Gold|North Jersey Skylands Kings|19|10|8|0|1|0|462|10.0|-0.0
9|173|Silver|Lehigh Valley Phantoms|40|21|15|1|3|0|314|22.6|0.6
10|165|Silver|Valley Forge Colonials 18U AA|40|22|16|1|1|0|279|23.8|0.8
11|112|Silver|Hollydell Hurricanes|39|18|16|2|3|0|252|20.8|0.8
12|108|Silver|MYHA 18U AA Gold|16|6|8|1|1|0|382|7.2|0.2
13|72||North Jersey Sportscare Kings Blue|28|11|13|2|2|0|193|13.6|0.6
14|56||Haverford Hawks|40|16|22|1|1|0|285|18.1|1.1
15|42||York Devils|39|13|24|1|1|0|305|14.9|0.9
16|11||New Jersey Renegades|12|3|8|1|0|0|85|4.5|0.5
17|8||The St. James Gold|16|4|10|0|2|0|73|4.4|0.4
18|4||Igloo Jaguars Green|39|3|33|1|2|0|244|4.4|0.4
19|4||Rockets Hockey Club|35|2|30|1|2|0|268|3.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|13.36|0.62
|Avg|0.70|0.03

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 18U-AA -o 18U-AA-ratings.md 18U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-26 |
| End Date | 2023-02-11 |
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

