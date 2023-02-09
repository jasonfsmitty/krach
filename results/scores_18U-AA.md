# 18U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1631|Championship|Philadelphia Blazers|38|32|1|3|2|0|357|32.2|-2.8
2|1167|Championship|MYHA 18U AA Blue|16|9|4|3|0|0|649|11.1|-0.9
3|944|Championship|Ashburn Xtreme|16|9|4|3|0|0|527|11.3|-0.7
4|679|Championship|Team Philadelphia|38|27|9|2|0|0|390|28.0|-1.0
5|529|Gold|Long Island Rebels|15|9|5|1|0|0|420|9.8|-0.2
6|456|Gold|Igloo Jaguars Black|40|27|9|0|4|0|401|26.4|-0.6
7|233|Gold|Metro Militia|16|9|5|2|0|0|183|11.4|0.4
8|231|Gold|North Jersey Skylands Kings|19|10|8|0|1|0|462|9.9|-0.1
9|174|Silver|Lehigh Valley Phantoms|40|21|15|1|3|0|314|22.5|0.5
10|172|Silver|Valley Forge Colonials 18U AA|39|22|15|1|1|0|268|23.8|0.8
11|113|Silver|Hollydell Hurricanes|39|18|16|2|3|0|253|20.8|0.8
12|109|Silver|MYHA 18U AA Gold|16|6|8|1|1|0|382|7.2|0.2
13|73||North Jersey Sportscare Kings Blue|28|11|13|2|2|0|194|13.6|0.6
14|57||Haverford Hawks|39|16|21|1|1|0|251|18.1|1.1
15|43||York Devils|39|13|24|1|1|0|306|14.9|0.9
16|11||New Jersey Renegades|12|3|8|1|0|0|86|4.5|0.5
17|8||The St. James Gold|16|4|10|0|2|0|74|4.4|0.4
18|4||Igloo Jaguars Green|39|3|33|1|2|0|244|4.4|0.4
19|4||Rockets Hockey Club|35|2|30|1|2|0|269|3.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|13.25|0.63
|Avg|0.70|0.03

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 18U-AA -o scores_18U-AA.md scores_18U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-26 |
| End Date | 2023-02-07 |
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

