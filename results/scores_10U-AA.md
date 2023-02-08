# 10U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1948|Championship|Ashburn Xtreme 2012|16|13|2|0|1|0|596|12.7|-0.8
2|1362|Championship|The St. James Gold|14|12|2|0|0|0|344|11.6|-0.4
3|1198|Championship|Team Philadelphia|37|27|6|2|2|0|545|27.8|-1.2
4|1196|Championship|MYHA 10U AA Blue|16|11|4|1|0|0|626|11.1|-0.4
5|1143|Gold|Philadelphia Blazers|37|25|6|5|1|0|569|27.0|-1.0
6|548|Gold|Long Island Rebels|16|9|6|0|1|0|583|9.4|-0.1
7|483|Gold|Lehigh Valley Phantoms|40|23|13|1|3|0|471|24.9|-0.1
8|381|Gold|Wissahickon Warriors|36|18|12|3|3|0|518|21.0|-0.0
9|333|Silver|Hollydell Hurricanes|38|21|12|3|2|0|345|23.9|0.4
10|332|Silver|Rye Rangers|14|7|5|1|1|0|513|8.1|0.1
11|269|Silver|NJ Stars Black|38|19|12|3|4|0|325|23.0|0.5
12|268|Silver|MYHA 10U AA Gold|16|8|5|0|3|0|302|9.7|0.2
13|153||Valley Forge Colonials 10U AA|40|15|18|3|4|0|396|19.0|0.5
14|148||Palmyra Black Knights|40|12|24|2|2|0|623|14.1|0.1
15|85||North Jersey Skylands Kings Navy|38|13|20|4|1|0|283|16.2|0.7
16|55||PAL Blue Knights|14|4|7|2|1|0|326|5.8|0.3
17|44||North Jersey Avalanche Blue|15|5|8|1|1|0|131|6.4|0.4
18|29||Haverford Hawks|39|6|28|2|3|0|422|8.9|0.4
19|19||Igloo Jaguars|40|7|32|1|0|0|279|7.9|0.4
20|6||Delaware Ducks Maroon|38|2|35|0|1|0|339|2.6|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.06|-0.00
|Avg|0.40|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 10U-AA -o scores_10U-AA.md scores_10U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
| End Date | 2023-02-05 |
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

