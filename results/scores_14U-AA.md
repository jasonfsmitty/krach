# 14U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3333|Championship|Ashburn Xtreme 2008|16|14|0|2|0|0|461|14.2|-1.8
2|1422|Championship|North Jersey Avalanche|16|13|0|1|2|0|463|13.1|-0.9
3|646|Championship|Long Island Rebels|18|12|3|0|3|0|540|11.7|-0.3
4|606|Championship|York Devils|38|27|7|3|1|0|303|29.4|-0.6
5|495|Gold|Valley Forge Colonials|38|21|9|5|3|0|527|25.5|-0.5
6|360|Gold|Rye Rangers|16|7|6|2|1|0|584|8.8|-0.2
7|306|Gold|Igloo Jaguars|38|23|13|2|0|0|269|25.1|0.1
8|290|Gold|NJ Bandits|40|22|13|3|2|0|361|25.0|0.0
9|207|Silver|Team Philadelphia|38|21|9|2|6|0|367|23.4|0.4
10|184|Silver|Haverford Hawks|39|16|13|5|5|0|372|21.3|0.3
11|165|Silver|MYHA 14U AA|16|7|6|1|2|0|246|8.1|0.1
12|162|Silver|Rockets Hockey Club Black|40|14|21|3|2|0|411|17.1|0.1
13|103||PAL Blue Knights|16|6|7|1|2|0|215|7.2|0.2
14|78||Delaware Ducks|39|15|20|2|2|0|233|17.6|0.6
15|43||Tomorrow's Ice Selects|39|10|26|2|1|0|378|12.5|0.5
16|26||Lehigh Valley Phantoms|38|10|27|1|0|0|188|11.7|0.7
17|13||Palmyra Black Knights|39|9|27|0|3|0|212|9.7|0.7
18|12||The St. James Gold|14|2|11|1|0|0|117|3.2|0.2
19|7||Rockets Hockey Club White|36|5|30|0|1|0|262|5.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.61|-0.02
|Avg|0.45|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-AA -o scores_14U-AA.md scores_14U-AA.json
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

