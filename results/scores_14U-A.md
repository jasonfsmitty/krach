# 14U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1570|Championship|Frederick Freeze LA|17|17|0|0|0|0|228|15.1|-1.9
2|931|Championship|Wissahickon Warriors White|34|31|2|1|0|0|207|29.4|-2.6
3|666|Championship|MYHA 14U LA Gold|16|14|1|1|0|0|125|14.1|-0.9
4|505|Championship|Philadelphia Blazers|35|28|5|1|1|0|150|27.9|-1.1
5|422|Gold|MYHA 14U UA Blue|16|10|3|3|0|0|157|12.5|-0.5
6|390|Gold|Grundy Senators Gold|35|28|3|2|2|0|100|29.2|-0.8
7|311|Gold|MYHA 14U LA Blue|16|10|4|1|1|0|231|10.7|-0.3
8|305|Gold|Valley Forge Colonials 14U A Gold|35|24|7|3|1|0|129|26.5|-0.5
9|258|Silver|North Jersey Sportscare Kings Yellow|16|11|4|1|0|0|121|12.0|0.0
10|244|Silver|Wissahickon Warriors Red|34|24|6|0|4|0|153|23.8|-0.2
11|219|Silver|Rye Rangers|16|8|6|2|0|0|192|9.8|-0.2
12|216|Silver|Haverford Hawks Dinmore|36|23|10|0|3|0|297|22.6|-0.4
13|208|Bronze|Palmyra Black Knights|35|23|11|0|1|0|254|22.8|-0.2
14|207|Bronze|North Jersey Avalanche Blue|16|10|3|0|3|0|169|9.9|-0.1
15|206|Bronze|Maryland Jr Black Bears Red|16|12|3|1|0|0|70|13.1|0.1
16|195|Bronze|NJ Bandits|16|8|4|2|2|0|225|10.0|-0.0
17|188||Team Philadelphia|36|20|13|2|1|0|278|21.8|-0.2
18|182||North Jersey Sportscare Kings Blue|16|8|7|1|0|0|193|8.9|-0.1
19|181||Southern Maryland Sabres 14U Gold|16|10|6|0|0|0|164|10.0|0.0
20|145||Maryland Jr Black Bears White|16|8|7|1|0|0|176|8.9|-0.1
21|142||North Jersey Avalanche Gold|14|9|3|0|2|0|146|9.2|0.2
22|133||North Jersey Skylands Kings Navy|16|8|8|0|0|0|196|7.9|-0.1
23|108||York Devils|36|20|11|2|3|0|136|22.6|0.6
24|95||WBS Jr Knights|36|16|17|1|2|0|175|17.0|-0.0
25|91||Lancaster Firebirds Black|36|16|15|3|2|0|158|19.2|0.2
26|82||Igloo Jaguars|36|20|13|1|2|0|127|21.5|0.5
27|82||The St. James White|16|9|6|0|1|0|131|9.3|0.3
28|81||Lehigh Valley Phantoms|35|17|14|2|2|0|132|19.5|0.5
29|73||Maryland Jr Black Bears Black|14|5|8|1|0|0|173|6.1|0.1
30|64||Haverford Hawks McKay|35|15|16|1|3|0|161|16.2|0.2
31|54||Maryland Jr Black Bears Gold|16|8|5|1|2|0|56|9.5|0.5
32|42||Lancaster Firebirds Orange|36|8|24|3|1|0|282|11.2|0.2
33|41||Valley Forge Colonials 14U A Silver Pusateri|36|10|18|4|4|0|173|14.6|0.6
34|37||Rockets Hockey Club|35|7|23|5|0|0|188|12.4|0.4
35|36||Grundy Senators Silver|36|12|20|1|3|0|228|13.3|0.3
36|34||The St. James Navy|16|7|8|1|0|0|69|8.4|0.4
37|32||Royals Gold|35|14|20|0|1|0|135|14.5|0.5
38|29||Jersey Shore Wildcats Red|16|6|6|1|3|0|109|7.4|0.4
39|28||NJ Stars Black|35|11|22|1|1|0|149|12.4|0.4
40|27||NJ Stars Green|34|9|19|4|2|0|71|13.7|0.7
41|26||Hollydell Hurricanes Black|35|11|21|2|1|0|150|13.6|0.6
42|18||Tomorrow's Ice North Stars Red|16|4|11|0|1|0|100|4.1|0.1
43|18||Hollydell Hurricanes Red|34|7|25|1|1|0|162|8.3|0.3
44|17||Capital City Vipers 2|35|9|23|1|2|0|128|10.4|0.4
45|15||Haverford Hawks Dolan|35|8|25|2|0|0|65|10.5|0.5
46|15||Jersey Shore Wildcats 09|15|4|10|1|0|0|107|5.3|0.3
47|3||Hollydell Hurricanes White|36|2|32|2|0|0|110|4.3|0.3
48|3||Valley Forge Colonials 14U A Silver Kelly|35|1|32|1|1|0|199|2.1|0.1
49|3||Jersey Shore Wildcats Black|16|3|12|0|1|0|80|3.3|0.3
50|2||Capital City Vipers 1|36|2|33|0|1|0|204|2.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|20.29|0.05
|Avg|0.41|0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 14U-A -o scores_14U-A.md scores_14U-A.json
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

