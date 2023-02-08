# 16U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|389|Championship|Team Philadelphia Black|37|28|7|2|0|0|255|27.3|-1.7
2|301|Championship|Atlanta MadHatters|12|9|3|0|0|0|155|8.5|-0.5
3|293|Championship|PAL Jr Islanders|16|11|4|1|0|0|300|11.0|-0.5
4|233|Championship|Jersey Shore Wildcats Black|33|25|5|0|3|0|77|26.0|-0.5
5|233|Gold|Ashburn Xtreme 16U AA 1|16|8|7|0|1|0|434|8.0|-0.5
6|180|Gold|Lehigh Valley Phantoms Black|40|26|9|3|2|0|140|28.0|-0.5
7|136|Gold|Long Island Rebels|17|7|8|2|0|0|304|7.7|-0.3
8|128|Gold|Igloo Jaguars|39|23|14|1|1|0|137|23.9|-0.1
9|113|Silver|MYHA 16U AA Blue|16|7|7|2|0|0|280|7.8|-0.2
10|88|Silver|Philadelphia Blazers|42|19|14|3|6|0|129|23.6|0.1
11|80|Silver|Delaware Ducks|45|25|15|2|3|0|65|28.0|0.5
12|76|Silver|Valley Forge Colonials 16U AA|40|17|17|3|3|0|106|20.0|-0.0
13|73|Bronze|Palmyra Black Knights|43|18|17|4|4|0|104|22.1|0.1
14|70|Bronze|Tomorrow's Ice Selects|47|21|20|3|3|0|94|24.1|0.1
15|58|Bronze|North Jersey Skylands Kings Navy|40|19|19|2|0|0|90|20.3|0.3
16|52|Bronze|Lehigh Valley Phantoms Orange|40|21|15|3|1|0|63|23.9|0.9
17|45||Haverford Hawks|38|12|17|3|6|0|98|16.7|0.2
18|45||Ashburn Xtreme 16U AA 2|16|6|8|2|0|0|90|7.1|0.1
19|40||NJ Bandits|34|17|13|2|2|0|53|20.0|1.0
20|33||York Devils|40|13|23|2|2|0|88|15.2|0.2
21|31||The St. James Gold|14|3|9|2|0|0|110|4.0|-0.0
22|21||WBS Jr Knights|37|9|23|5|0|0|85|11.8|0.3
23|21||Jersey Shore Wildcats Red|34|11|18|1|4|0|64|14.0|0.5
24|20||Team Philadelphia Orange|38|12|21|3|2|0|57|15.1|0.6
25|14||North Jersey Sportscare Kings Blue|24|7|15|2|0|0|76|8.4|0.4
26|8||Jersey Shore Wildcats White|34|9|21|0|4|0|62|11.9|0.9
27|6||NJ Stars|39|6|30|1|2|0|91|8.0|0.5
28|3||Rockets Hockey Club|37|4|30|2|1|0|38|5.9|0.4

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|11.55|1.81
|Avg|0.41|0.06

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 16U-AA -o scores_16U-AA.md scores_16U-AA.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
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

