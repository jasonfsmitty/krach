# 16U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4460|Championship|Team Philadelphia Black|37|28|7|2|0|0|2622|28.0|-2.0
2|3408|Championship|PAL Jr Islanders|16|11|4|1|0|0|3091|11.4|-0.6
3|3136|Championship|Atlanta MadHatters|12|9|3|0|0|0|1672|8.5|-0.5
4|2035|Championship|Ashburn Xtreme 16U AA 1|16|8|7|0|1|0|4501|7.6|-0.4
5|1949|Gold|Lehigh Valley Phantoms Black|40|26|9|3|2|0|1461|28.4|-0.6
6|1720|Gold|Jersey Shore Wildcats Black|33|25|5|0|3|0|708|24.9|-0.1
7|1649|Gold|Long Island Rebels|17|7|8|2|0|0|3040|8.6|-0.4
8|1509|Gold|MYHA 16U AA Blue|16|7|7|2|0|0|2993|8.7|-0.3
9|1217|Silver|Igloo Jaguars|39|23|14|1|1|0|1384|23.9|-0.1
10|776|Silver|Valley Forge Colonials 16U AA|40|17|17|3|3|0|1072|19.9|-0.1
11|750|Silver|Palmyra Black Knights|43|18|17|4|4|0|1091|22.0|0.0
12|723|Silver|Delaware Ducks|45|25|15|2|3|0|627|27.5|0.5
13|720|Bronze|Philadelphia Blazers|42|19|14|3|6|0|1311|22.1|0.1
14|674|Bronze|Tomorrow's Ice Selects|47|21|20|3|3|0|953|24.1|0.1
15|658|Bronze|North Jersey Skylands Kings Navy|40|19|19|2|0|0|899|21.3|0.3
16|587|Bronze|Lehigh Valley Phantoms Orange|40|21|15|3|1|0|636|24.9|0.9
17|567||Ashburn Xtreme 16U AA 2|16|6|8|2|0|0|940|8.0|0.0
18|416||The St. James Gold|14|3|9|2|0|0|1064|5.0|-0.0
19|383||NJ Bandits|34|17|13|2|2|0|506|20.0|1.0
20|375||Haverford Hawks|38|12|17|3|6|0|1003|15.2|0.2
21|335||York Devils|40|13|23|2|2|0|938|15.2|0.2
22|301||WBS Jr Knights|37|9|23|5|0|0|815|14.3|0.3
23|199||Team Philadelphia Orange|38|12|21|3|2|0|515|15.6|0.6
24|162||Jersey Shore Wildcats Red|34|11|18|1|4|0|663|12.5|0.5
25|153||North Jersey Sportscare Kings Blue|24|7|15|2|0|0|694|9.5|0.5
26|59||Jersey Shore Wildcats White|34|9|21|0|4|0|558|9.8|0.8
27|48||NJ Stars|39|6|30|1|2|0|844|7.5|0.5
28|32||Rockets Hockey Club|37|4|30|2|1|0|363|6.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.13|1.62
|Avg|0.43|0.06

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 16U-AA -o scores_16U-AA.md scores_16U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
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

