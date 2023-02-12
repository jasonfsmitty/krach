# 16U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4510|Championship|Team Philadelphia Black|38|29|7|2|0|0|2573|28.9|-2.1
2|3398|Championship|PAL Jr Islanders|16|11|4|1|0|0|3093|11.4|-0.6
3|3137|Championship|Atlanta MadHatters|12|9|3|0|0|0|1678|8.5|-0.5
4|2037|Championship|Ashburn Xtreme 16U AA 1|16|8|7|0|1|0|4514|7.6|-0.4
5|1946|Gold|Lehigh Valley Phantoms Black|40|26|9|3|2|0|1464|28.4|-0.6
6|1719|Gold|Jersey Shore Wildcats Black|33|25|5|0|3|0|706|24.9|-0.1
7|1629|Gold|Long Island Rebels|17|7|8|2|0|0|3036|8.6|-0.4
8|1510|Gold|MYHA 16U AA Blue|16|7|7|2|0|0|2998|8.7|-0.3
9|1216|Silver|Igloo Jaguars|39|23|14|1|1|0|1386|23.9|-0.1
10|773|Silver|Valley Forge Colonials 16U AA|40|17|17|3|3|0|1072|20.0|-0.0
11|762|Silver|Palmyra Black Knights|44|19|17|4|4|0|1070|23.1|0.1
12|720|Silver|Delaware Ducks|45|25|15|2|3|0|625|27.5|0.5
13|716|Bronze|Philadelphia Blazers|42|19|14|3|6|0|1312|22.1|0.1
14|659|Bronze|Tomorrow's Ice Selects|48|21|21|3|3|0|1026|24.0|0.0
15|655|Bronze|North Jersey Skylands Kings Navy|40|19|19|2|0|0|896|21.3|0.3
16|586|Bronze|Lehigh Valley Phantoms Orange|40|21|15|3|1|0|638|24.9|0.9
17|572||Ashburn Xtreme 16U AA 2|16|6|8|2|0|0|946|8.0|0.0
18|397||Haverford Hawks|39|13|17|3|6|0|988|16.2|0.2
19|382||NJ Bandits|34|17|13|2|2|0|505|20.0|1.0
20|352||The St. James Gold|15|3|10|2|0|0|1017|5.0|-0.0
21|331||York Devils|40|13|23|2|2|0|938|15.2|0.2
22|301||WBS Jr Knights|37|9|23|5|0|0|816|14.3|0.3
23|193||Team Philadelphia Orange|39|12|22|3|2|0|521|15.6|0.6
24|162||Jersey Shore Wildcats Red|34|11|18|1|4|0|662|12.5|0.5
25|153||North Jersey Sportscare Kings Blue|24|7|15|2|0|0|696|9.5|0.5
26|58||Jersey Shore Wildcats White|34|9|21|0|4|0|556|9.8|0.8
27|48||NJ Stars|39|6|30|1|2|0|842|7.5|0.5
28|31||Rockets Hockey Club|37|4|30|2|1|0|363|6.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.19|1.61
|Avg|0.44|0.06

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 16U-AA -o scores_16U-AA.md scores_16U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
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

