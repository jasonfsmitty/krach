# 10U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1792|Championship|Ashburn Xtreme 2012|16|13|2|0|1|0|686|12.2|-0.8
2|1472|Championship|MYHA 10U AA Blue|16|11|4|1|0|0|713|11.5|-0.5
3|1463|Championship|Philadelphia Blazers|38|26|6|5|1|0|552|29.6|-1.4
4|1383|Championship|Team Philadelphia|40|29|6|3|2|0|576|30.5|-1.5
5|960|Gold|The St. James Gold|16|12|3|0|1|0|501|11.7|-0.3
6|484|Gold|Long Island Rebels|16|9|6|0|1|0|628|8.9|-0.1
7|417|Gold|Lehigh Valley Phantoms|40|23|13|1|3|0|499|24.0|0.0
8|410|Gold|Wissahickon Warriors|39|20|13|3|3|0|531|23.0|-0.0
9|345|Silver|Rye Rangers|14|7|5|1|1|0|548|8.1|0.1
10|327|Silver|Hollydell Hurricanes|39|21|13|3|2|0|361|24.4|0.4
11|240|Silver|NJ Stars Black|39|19|13|3|4|0|354|22.5|0.5
12|157|Silver|MYHA 10U AA Gold|16|8|5|0|3|0|330|8.2|0.2
13|140||Valley Forge Colonials 10U AA|40|15|18|3|4|0|405|18.6|0.6
14|136||Palmyra Black Knights|40|12|24|2|2|0|625|14.2|0.2
15|107||North Jersey Skylands Kings Navy|39|14|20|4|1|0|270|18.8|0.8
16|70||PAL Blue Knights|14|4|7|2|1|0|325|6.3|0.3
17|45||North Jersey Avalanche Blue|15|5|8|1|1|0|135|6.4|0.4
18|25||Haverford Hawks|40|6|29|2|3|0|442|8.4|0.4
19|21||Igloo Jaguars|40|7|32|1|0|0|294|8.4|0.4
20|4||Delaware Ducks Maroon|39|2|36|0|1|0|348|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|9.25|-0.00
|Avg|0.46|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-AA -o scores_10U-AA.md scores_10U-AA.json
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

