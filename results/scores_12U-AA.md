# 12U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2037|Championship|Ashburn Xtreme 2010|16|12|1|2|1|0|544|12.9|-1.1
2|1224|Championship|Philadelphia Blazers|39|30|4|3|2|0|398|31.2|-1.8
3|584|Championship|MYHA 12U AA Blue|16|7|6|3|0|0|507|9.7|-0.3
4|438|Championship|Team Philadelphia|40|25|12|2|1|0|352|26.6|-0.4
5|403|Gold|Haverford Hawks|39|24|12|0|3|0|427|23.6|-0.4
6|350|Gold|Long Island Rebels|16|5|6|3|2|0|581|7.8|-0.2
7|339|Gold|York Devils|40|24|14|0|2|0|412|23.8|-0.2
8|333|Gold|Hollydell Hurricanes|40|27|10|0|2|1|241|27.6|0.1
9|274|Silver|The St. James Gold|16|10|5|0|1|0|263|10.0|0.0
10|206|Silver|Lehigh Valley Phantoms|40|20|13|2|5|0|308|22.0|0.0
11|177|Silver|NJ Bandits|41|18|17|2|3|1|315|20.7|0.2
12|176|Silver|Palmyra Black Knights|40|19|17|2|2|0|361|21.2|0.2
13|159||PAL Blue Knights|14|7|7|0|0|0|382|7.1|0.1
14|159||North Jersey Avalanche|16|6|9|1|0|0|342|7.0|0.0
15|87||MYHA 12U AA Gold|16|8|7|1|0|0|120|9.6|0.6
16|63||Rye Rangers|16|4|8|2|2|0|234|6.2|0.2
17|55||North Jersey Skylands Kings|39|12|21|3|3|0|209|15.6|0.6
18|43||Rockets Hockey Club|39|11|25|3|0|0|204|14.7|0.7
19|21||Delaware Ducks|40|11|28|0|1|0|214|11.7|0.7
20|7||Igloo Jaguars|40|5|33|1|1|0|163|6.4|0.4
21|6||NJ Stars|35|3|29|2|1|0|209|5.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.73|-0.18
|Avg|0.42|-0.01

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 12U-AA -o scores_12U-AA.md scores_12U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
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

