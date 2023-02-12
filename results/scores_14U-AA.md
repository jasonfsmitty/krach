# 14U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3346|Championship|Ashburn Xtreme 2008|16|14|0|2|0|0|460|14.2|-1.8
2|1426|Championship|North Jersey Avalanche|16|13|0|1|2|0|463|13.1|-0.9
3|647|Championship|Long Island Rebels|18|12|3|0|3|0|539|11.7|-0.3
4|612|Championship|York Devils|40|29|7|3|1|0|289|31.3|-0.7
5|478|Gold|Valley Forge Colonials|40|21|10|6|3|0|513|26.6|-0.4
6|359|Gold|Rye Rangers|16|7|6|2|1|0|583|8.8|-0.2
7|293|Gold|NJ Bandits|40|22|13|3|2|0|361|25.0|0.0
8|280|Gold|Igloo Jaguars|39|23|14|2|0|0|266|25.1|0.1
9|219|Silver|Team Philadelphia|40|22|9|2|7|0|373|24.3|0.3
10|188|Silver|Haverford Hawks|40|17|13|5|5|0|363|22.3|0.3
11|169|Silver|MYHA 14U AA|16|7|6|1|2|0|247|8.1|0.1
12|167|Silver|Rockets Hockey Club Black|41|15|21|3|2|0|402|18.1|0.1
13|105||PAL Blue Knights|16|6|7|1|2|0|218|7.1|0.1
14|89||Delaware Ducks|40|16|20|2|2|0|234|18.6|0.6
15|44||Tomorrow's Ice Selects|39|10|26|2|1|0|378|12.5|0.5
16|27||Lehigh Valley Phantoms|39|11|27|1|0|0|184|12.7|0.7
17|13||Palmyra Black Knights|40|9|28|0|3|0|211|9.7|0.7
18|12||The St. James Gold|16|2|13|1|0|0|179|3.2|0.2
19|6||Rockets Hockey Club White|38|5|32|0|1|0|255|5.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|8.46|-0.03
|Avg|0.45|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-AA -o scores_14U-AA.md scores_14U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

