# 18U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1743|Championship|Philadelphia Blazers|38|32|1|3|2|0|370|32.0|-2.5
2|889|Championship|MYHA 18U AA Blue|16|9|4|3|0|0|717|9.9|-0.6
3|728|Championship|Ashburn Xtreme|16|9|4|3|0|0|594|10.0|-0.5
4|695|Championship|Team Philadelphia|38|27|9|2|0|0|413|27.2|-0.8
5|678|Gold|Igloo Jaguars Black|40|27|9|0|4|0|411|28.2|-0.8
6|544|Gold|Long Island Rebels|15|9|5|1|0|0|467|9.3|-0.2
7|315|Gold|North Jersey Skylands Kings|19|10|8|0|1|0|488|10.4|-0.1
8|239|Gold|Lehigh Valley Phantoms|40|21|15|1|3|0|338|23.4|0.4
9|209|Silver|Valley Forge Colonials 18U AA|39|22|15|1|1|0|295|23.6|0.6
10|204|Silver|Metro Militia|16|9|5|2|0|0|211|10.4|0.4
11|157|Silver|Hollydell Hurricanes|39|18|16|2|3|0|296|21.2|0.7
12|134|Silver|MYHA 18U AA Gold|16|6|8|1|1|0|431|7.2|0.2
13|92||North Jersey Sportscare Kings Blue|28|11|13|2|2|0|225|13.5|0.5
14|72||Haverford Hawks|39|16|21|1|1|0|271|18.0|1.0
15|56||York Devils|39|13|24|1|1|0|333|14.7|0.7
16|19||The St. James Gold|16|4|10|0|2|0|92|5.4|0.4
17|11||New Jersey Renegades|12|3|8|1|0|0|117|3.8|0.3
18|7||Igloo Jaguars Green|39|3|33|1|2|0|258|4.9|0.4
19|6||Rockets Hockey Club|35|2|30|1|2|0|297|3.8|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|11.31|0.42
|Avg|0.60|0.02

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 18U-AA -o scores_18U-AA.md scores_18U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-26 |
| End Date | 2023-02-07 |
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
| Date Cutoff | 2023-02-08 |

