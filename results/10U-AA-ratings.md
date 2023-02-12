# 10U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1789|Championship|Ashburn Xtreme 2012|16|13|2|0|1|0|689|12.2|-0.8
2|1496|Championship|Philadelphia Blazers|39|27|6|5|1|0|546|30.5|-1.5
3|1473|Championship|MYHA 10U AA Blue|16|11|4|1|0|0|717|11.5|-0.5
4|1377|Championship|Team Philadelphia|40|29|6|3|2|0|576|30.5|-1.5
5|957|Gold|The St. James Gold|16|12|3|0|1|0|501|11.7|-0.3
6|480|Gold|Long Island Rebels|16|9|6|0|1|0|629|8.9|-0.1
7|414|Gold|Lehigh Valley Phantoms|40|23|13|1|3|0|499|24.0|0.0
8|395|Gold|Wissahickon Warriors|40|20|14|3|3|0|555|23.0|-0.0
9|344|Silver|Hollydell Hurricanes|40|22|13|3|2|0|357|25.4|0.4
10|344|Silver|Rye Rangers|14|7|5|1|1|0|547|8.1|0.1
11|226|Silver|NJ Stars Black|40|19|14|3|4|0|355|22.6|0.6
12|158|Silver|MYHA 10U AA Gold|16|8|5|0|3|0|336|8.2|0.2
13|139||Valley Forge Colonials 10U AA|40|15|18|3|4|0|405|18.6|0.6
14|136||Palmyra Black Knights|40|12|24|2|2|0|626|14.2|0.2
15|107||North Jersey Skylands Kings Navy|39|14|20|4|1|0|271|18.8|0.8
16|70||PAL Blue Knights|14|4|7|2|1|0|323|6.3|0.3
17|45||North Jersey Avalanche Blue|15|5|8|1|1|0|133|6.4|0.4
18|25||Haverford Hawks|40|6|29|2|3|0|443|8.4|0.4
19|21||Igloo Jaguars|40|7|32|1|0|0|293|8.5|0.5
20|4||Delaware Ducks Maroon|39|2|36|0|1|0|348|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|9.40|-0.00
|Avg|0.47|-0.00

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-AA -o 10U-AA-ratings.md 10U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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

