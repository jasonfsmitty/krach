# 14U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1602|Championship|Frederick Freeze LA|17|17|0|0|0|0|230|15.1|-1.9
2|882|Championship|Wissahickon Warriors White|34|31|2|1|0|0|212|29.1|-2.4
3|554|Championship|MYHA 14U LA Gold|16|14|1|1|0|0|123|13.9|-0.6
4|509|Championship|Philadelphia Blazers|35|28|5|1|1|0|148|28.0|-1.0
5|393|Gold|Grundy Senators Gold|34|27|3|2|2|0|105|28.2|-0.8
6|327|Gold|Wissahickon Warriors Red|33|23|6|0|4|0|153|24.5|-0.5
7|327|Gold|MYHA 14U LA Blue|16|10|4|1|1|0|234|10.7|-0.3
8|313|Gold|North Jersey Avalanche Blue|16|10|3|0|3|0|162|11.2|-0.3
9|271|Silver|MYHA 14U UA Blue|16|10|3|3|0|0|167|11.2|-0.3
10|266|Silver|Valley Forge Colonials 14U A Gold|34|23|7|3|1|0|136|24.7|-0.3
11|261|Silver|Haverford Hawks Dinmore|35|22|10|0|3|0|303|22.9|-0.6
12|234|Silver|Palmyra Black Knights|34|23|11|0|0|0|254|22.7|-0.3
13|220|Bronze|North Jersey Sportscare Kings Yellow|16|11|4|1|0|0|122|11.6|0.1
14|195|Bronze|North Jersey Sportscare Kings Blue|15|8|6|1|0|0|204|8.4|-0.1
15|192|Bronze|NJ Bandits|16|8|4|2|2|0|232|9.9|-0.1
16|190|Bronze|North Jersey Avalanche Gold|14|9|3|0|2|0|138|10.2|0.2
17|187||Southern Maryland Sabres 14U Gold|16|10|6|0|0|0|170|10.0|-0.0
18|173||Team Philadelphia|35|19|13|2|1|0|291|20.4|-0.1
19|173||Maryland Jr Black Bears Red|16|12|3|1|0|0|77|12.7|0.2
20|165||Rye Rangers|16|8|6|2|0|0|188|8.9|-0.1
21|135||North Jersey Skylands Kings Navy|16|8|8|0|0|0|201|7.9|-0.1
22|127||Maryland Jr Black Bears White|16|8|7|1|0|0|177|8.4|-0.1
23|116||York Devils|36|20|11|2|3|0|133|23.1|0.6
24|98||WBS Jr Knights|35|15|17|1|2|0|185|16.5|-0.0
25|97||Igloo Jaguars|35|20|12|1|2|0|124|22.0|0.5
26|94||The St. James White|16|9|6|0|1|0|129|9.8|0.3
27|88||Haverford Hawks McKay|33|15|14|1|3|0|150|17.1|0.1
28|85||Lancaster Firebirds Black|36|16|15|3|2|0|162|18.8|0.3
29|71||Lehigh Valley Phantoms|33|15|14|2|2|0|137|17.5|0.5
30|64||Maryland Jr Black Bears Gold|16|8|5|1|2|0|57|10.0|0.5
31|59||Maryland Jr Black Bears Black|14|5|8|1|0|0|177|5.6|0.1
32|42||Grundy Senators Silver|35|12|19|1|3|0|230|14.4|0.4
33|37||Valley Forge Colonials 14U A Silver Pusateri|35|9|18|4|4|0|165|13.6|0.6
34|36||Royals Gold|34|14|19|0|1|0|135|15.0|0.5
35|36||Jersey Shore Wildcats Red|16|6|6|1|3|0|92|8.5|0.5
36|33||Lancaster Firebirds Orange|35|8|24|2|1|0|282|9.7|0.2
37|28||Rockets Hockey Club|33|7|21|5|0|0|202|9.9|0.4
38|28||The St. James Navy|16|7|8|1|0|0|79|7.9|0.4
39|27||NJ Stars Black|33|9|22|1|1|0|163|10.3|0.3
40|25||Hollydell Hurricanes Black|34|11|20|2|1|0|147|13.1|0.6
41|24||NJ Stars Green|32|8|18|4|2|0|76|11.6|0.6
42|21||Tomorrow's Ice North Stars Red|16|4|11|0|1|0|111|4.7|0.2
43|16||Capital City Vipers 2|34|8|23|1|2|0|132|9.9|0.4
44|15||Hollydell Hurricanes Red|33|6|25|1|1|0|157|7.2|0.2
45|13||Haverford Hawks Dolan|34|8|24|2|0|0|67|9.5|0.5
46|11||Jersey Shore Wildcats 09|15|4|10|1|0|0|116|4.8|0.3
47|4||Jersey Shore Wildcats Black|16|3|12|0|1|0|77|3.8|0.3
48|3||Valley Forge Colonials 14U A Silver Kelly|34|1|31|1|1|0|195|2.1|0.1
49|2||Hollydell Hurricanes White|34|2|30|2|0|0|120|3.2|0.2
50|2||Capital City Vipers 1|36|2|33|0|1|0|198|2.7|0.2

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|19.87|0.13
|Avg|0.40|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 14U-A -o scores_14U-A.md scores_14U-A.js
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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
| Date Cutoff | 2023-02-07 |

