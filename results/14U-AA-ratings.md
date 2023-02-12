# 14U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3369|Championship|Ashburn Xtreme 2008|16|14|0|2|0|0|461|14.2|-1.8
2|1424|Championship|North Jersey Avalanche|16|13|0|1|2|0|463|13.1|-0.9
3|644|Championship|Long Island Rebels|18|12|3|0|3|0|539|11.7|-0.3
4|616|Championship|York Devils|40|29|7|3|1|0|289|31.3|-0.7
5|481|Gold|Valley Forge Colonials|40|21|10|6|3|0|515|26.6|-0.4
6|356|Gold|Rye Rangers|16|7|6|2|1|0|582|8.9|-0.1
7|294|Gold|NJ Bandits|40|22|13|3|2|0|361|25.0|0.0
8|254|Gold|Igloo Jaguars|40|23|14|2|1|0|261|25.2|0.2
9|221|Silver|Team Philadelphia|40|22|9|2|7|0|373|24.3|0.3
10|190|Silver|Haverford Hawks|40|17|13|5|5|0|363|22.3|0.3
11|172|Silver|MYHA 14U AA|16|7|6|1|2|0|250|8.1|0.1
12|167|Silver|Rockets Hockey Club Black|41|15|21|3|2|0|402|18.1|0.1
13|106||PAL Blue Knights|16|6|7|1|2|0|217|7.1|0.1
14|90||Delaware Ducks|40|16|20|2|2|0|234|18.6|0.6
15|51||Tomorrow's Ice Selects|40|10|26|3|1|0|376|13.5|0.5
16|28||Lehigh Valley Phantoms|39|11|27|1|0|0|185|12.7|0.7
17|14||Palmyra Black Knights|40|9|28|0|3|0|211|9.6|0.6
18|13||The St. James Gold|16|2|13|1|0|0|178|3.2|0.2
19|6||Rockets Hockey Club White|38|5|32|0|1|0|254|5.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.39|-0.02
|Avg|0.44|-0.00

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-AA -o 14U-AA-ratings.md 14U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

