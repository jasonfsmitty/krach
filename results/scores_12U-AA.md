# 12U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2043|Championship|Ashburn Xtreme 2010|16|12|1|2|1|0|541|12.9|-1.1
2|1192|Championship|Philadelphia Blazers|38|29|4|3|2|0|399|30.3|-1.7
3|585|Championship|MYHA 12U AA Blue|16|7|6|3|0|0|501|9.7|-0.3
4|420|Championship|Haverford Hawks|38|24|11|0|3|0|406|23.6|-0.4
5|419|Gold|Team Philadelphia|39|25|12|1|1|0|353|25.6|-0.4
6|357|Gold|Hollydell Hurricanes|39|27|10|0|1|1|236|27.6|0.1
7|352|Gold|Long Island Rebels|16|5|6|3|2|0|577|7.8|-0.2
8|339|Gold|York Devils|40|24|14|0|2|0|411|23.8|-0.2
9|274|Silver|The St. James Gold|16|10|5|0|1|0|262|10.0|0.0
10|208|Silver|Lehigh Valley Phantoms|40|20|13|2|5|0|307|22.0|0.0
11|179|Silver|NJ Bandits|41|18|17|2|3|1|316|20.7|0.2
12|177|Silver|Palmyra Black Knights|40|19|17|2|2|0|361|21.2|0.2
13|160||North Jersey Avalanche|16|6|9|1|0|0|341|7.0|0.0
14|142||PAL Blue Knights|13|6|7|0|0|0|409|6.0|0.0
15|88||MYHA 12U AA Gold|16|8|7|1|0|0|121|9.5|0.5
16|67||Rye Rangers|14|3|8|2|1|0|263|5.1|0.1
17|58||North Jersey Skylands Kings|38|12|20|3|3|0|211|15.6|0.6
18|41||Rockets Hockey Club|37|11|24|2|0|0|211|13.7|0.7
19|21||Delaware Ducks|40|11|28|0|1|0|215|11.7|0.7
20|7||Igloo Jaguars|40|5|33|1|1|0|164|6.4|0.4
21|6||NJ Stars|35|3|29|2|1|0|209|5.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.32|-0.18
|Avg|0.40|-0.01

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 12U-AA -o scores_12U-AA.md scores_12U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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

