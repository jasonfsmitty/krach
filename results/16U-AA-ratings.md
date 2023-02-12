# 16U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4502|Championship|Team Philadelphia Black|39|30|7|2|0|0|2513|29.9|-2.1
2|3396|Championship|PAL Jr Islanders|16|11|4|1|0|0|3089|11.4|-0.6
3|3135|Championship|Atlanta MadHatters|12|9|3|0|0|0|1675|8.5|-0.5
4|2036|Championship|Ashburn Xtreme 16U AA 1|16|8|7|0|1|0|4514|7.6|-0.4
5|1942|Gold|Lehigh Valley Phantoms Black|40|26|9|3|2|0|1461|28.4|-0.6
6|1708|Gold|Jersey Shore Wildcats Black|33|25|5|0|3|0|703|24.9|-0.1
7|1631|Gold|Long Island Rebels|18|8|8|2|0|0|2874|9.6|-0.4
8|1504|Gold|MYHA 16U AA Blue|16|7|7|2|0|0|2996|8.7|-0.3
9|1210|Silver|Igloo Jaguars|39|23|14|1|1|0|1382|23.9|-0.1
10|772|Silver|Valley Forge Colonials 16U AA|40|17|17|3|3|0|1069|20.0|-0.0
11|763|Silver|Palmyra Black Knights|44|19|17|4|4|0|1069|23.1|0.1
12|714|Silver|Delaware Ducks|45|25|15|2|3|0|621|27.6|0.6
13|714|Bronze|Philadelphia Blazers|42|19|14|3|6|0|1310|22.2|0.2
14|658|Bronze|Tomorrow's Ice Selects|48|21|21|3|3|0|1024|24.0|0.0
15|653|Bronze|North Jersey Skylands Kings Navy|40|19|19|2|0|0|894|21.3|0.3
16|582|Bronze|Lehigh Valley Phantoms Orange|40|21|15|3|1|0|636|24.9|0.9
17|566||Ashburn Xtreme 16U AA 2|16|6|8|2|0|0|941|8.0|0.0
18|410||The St. James Gold|16|4|10|2|0|0|977|6.0|0.0
19|379||NJ Bandits|34|17|13|2|2|0|501|20.0|1.0
20|374||Haverford Hawks|40|13|18|3|6|0|972|16.2|0.2
21|331||York Devils|40|13|23|2|2|0|936|15.2|0.2
22|295||WBS Jr Knights|38|9|24|5|0|0|909|14.3|0.3
23|191||Team Philadelphia Orange|39|12|22|3|2|0|517|15.6|0.6
24|160||Jersey Shore Wildcats Red|34|11|18|1|4|0|659|12.5|0.5
25|151||North Jersey Sportscare Kings Blue|24|7|15|2|0|0|691|9.5|0.5
26|58||Jersey Shore Wildcats White|34|9|21|0|4|0|553|9.8|0.8
27|47||NJ Stars|39|6|30|1|2|0|840|7.5|0.5
28|31||Rockets Hockey Club|38|4|31|2|1|0|393|6.4|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|12.30|1.60
|Avg|0.44|0.06

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 16U-AA -o 16U-AA-ratings.md 16U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
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

