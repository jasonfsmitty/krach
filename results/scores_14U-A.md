# 14U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1561|Championship|Frederick Freeze LA|17|17|0|0|0|0|226|15.1|-1.9
2|916|Championship|Wissahickon Warriors White|34|31|2|1|0|0|204|29.4|-2.6
3|668|Championship|MYHA 14U LA Gold|16|14|1|1|0|0|126|14.1|-0.9
4|503|Championship|Philadelphia Blazers|35|28|5|1|1|0|149|27.9|-1.1
5|426|Gold|MYHA 14U UA Blue|16|10|3|3|0|0|158|12.5|-0.5
6|376|Gold|Grundy Senators Gold|34|27|3|2|2|0|100|28.3|-0.7
7|305|Gold|MYHA 14U LA Blue|16|10|4|1|1|0|227|10.7|-0.3
8|302|Gold|Valley Forge Colonials 14U A Gold|34|23|7|3|1|0|133|25.5|-0.5
9|259|Silver|North Jersey Sportscare Kings Yellow|16|11|4|1|0|0|122|12.0|0.0
10|236|Silver|Wissahickon Warriors Red|33|23|6|0|4|0|156|22.8|-0.2
11|230|Silver|Palmyra Black Knights|34|23|11|0|0|0|256|22.7|-0.3
12|221|Silver|Rye Rangers|16|8|6|2|0|0|194|9.8|-0.2
13|218|Bronze|North Jersey Sportscare Kings Blue|15|8|6|1|0|0|197|8.8|-0.2
14|209|Bronze|Haverford Hawks Dinmore|35|22|10|0|3|0|302|21.6|-0.4
15|205|Bronze|North Jersey Avalanche Blue|16|10|3|0|3|0|171|9.9|-0.1
16|204|Bronze|Maryland Jr Black Bears Red|16|12|3|1|0|0|68|13.1|0.1
17|197||NJ Bandits|16|8|4|2|2|0|223|10.0|-0.0
18|179||Team Philadelphia|35|19|13|2|1|0|282|20.9|-0.1
19|178||Southern Maryland Sabres 14U Gold|16|10|6|0|0|0|162|10.0|0.0
20|147||Maryland Jr Black Bears White|16|8|7|1|0|0|178|8.9|-0.1
21|145||North Jersey Avalanche Gold|14|9|3|0|2|0|149|9.2|0.2
22|128||North Jersey Skylands Kings Navy|16|8|8|0|0|0|192|7.9|-0.1
23|104||York Devils|36|20|11|2|3|0|135|22.6|0.6
24|90||Lancaster Firebirds Black|36|16|15|3|2|0|156|19.3|0.3
25|87||WBS Jr Knights|35|15|17|1|2|0|175|16.0|0.0
26|85||Igloo Jaguars|35|20|12|1|2|0|119|21.6|0.6
27|81||The St. James White|16|9|6|0|1|0|127|9.3|0.3
28|75||Haverford Hawks McKay|33|15|14|1|3|0|161|16.1|0.1
29|71||Lehigh Valley Phantoms|33|15|14|2|2|0|136|17.5|0.5
30|69||Maryland Jr Black Bears Black|14|5|8|1|0|0|169|6.1|0.1
31|52||Maryland Jr Black Bears Gold|16|8|5|1|2|0|54|9.5|0.5
32|41||Rockets Hockey Club|33|7|21|5|0|0|196|12.4|0.4
33|38||Valley Forge Colonials 14U A Silver Pusateri|35|9|18|4|4|0|177|13.6|0.6
34|37||Grundy Senators Silver|35|12|19|1|3|0|226|13.4|0.4
35|35||Lancaster Firebirds Orange|35|8|24|2|1|0|281|10.2|0.2
36|32||The St. James Navy|16|7|8|1|0|0|66|8.4|0.4
37|31||Royals Gold|34|14|19|0|1|0|128|14.5|0.5
38|30||Jersey Shore Wildcats Red|16|6|6|1|3|0|110|7.4|0.4
39|28||NJ Stars Green|32|8|18|4|2|0|74|12.6|0.6
40|27||Hollydell Hurricanes Black|34|11|20|2|1|0|148|13.6|0.6
41|26||NJ Stars Black|33|9|22|1|1|0|159|10.3|0.3
42|17||Tomorrow's Ice North Stars Red|16|4|11|0|1|0|100|4.1|0.1
43|16||Haverford Hawks Dolan|34|8|24|2|0|0|66|10.5|0.5
44|15||Capital City Vipers 2|34|8|23|1|2|0|129|9.4|0.4
45|15||Jersey Shore Wildcats 09|15|4|10|1|0|0|106|5.3|0.3
46|14||Hollydell Hurricanes Red|33|6|25|1|1|0|164|7.3|0.3
47|3||Hollydell Hurricanes White|34|2|30|2|0|0|112|4.3|0.3
48|3||Valley Forge Colonials 14U A Silver Kelly|34|1|31|1|1|0|202|2.1|0.1
49|3||Jersey Shore Wildcats Black|16|3|12|0|1|0|80|3.3|0.3
50|2||Capital City Vipers 1|36|2|33|0|1|0|203|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|20.25|0.05
|Avg|0.41|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-A -o scores_14U-A.md scores_14U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

