# 10U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1116|Championship|North Jersey Sportscare Kings Blue|16|14|1|1|0|0|257|13.5|-1.5
2|821|Championship|Ashburn Xtreme 10U X|16|13|1|1|1|0|275|12.8|-1.2
3|781|Championship|Royals White|36|29|3|3|1|0|227|29.6|-2.4
4|693|Championship|NJ Bandits Grey|16|15|1|0|0|0|114|14.0|-1.0
5|432|Gold|Frederick Freeze LA|16|15|1|0|0|0|74|14.5|-0.5
6|370|Gold|York Devils|35|28|6|0|1|0|141|27.2|-0.8
7|360|Gold|NJ Bandits Black|16|11|5|0|0|0|341|10.4|-0.6
8|285|Gold|Jersey Shore Wildcats|16|10|5|1|0|0|288|10.5|-0.5
9|281|Silver|Capital City Vipers 1|34|24|8|1|1|0|143|24.5|-0.5
10|259|Silver|Maryland Jr Black Bears White|16|12|4|0|0|0|130|12.0|0.0
11|243|Silver|Tomorrow's Ice North Stars Red|18|13|3|0|1|1|198|13.2|-0.3
12|229|Silver|Southern Maryland Sabres 10U Gold|16|11|4|0|1|0|147|10.9|-0.1
13|225|Bronze|Rockets Hockey Club Black|36|25|8|1|2|0|185|25.6|-0.4
14|224|Bronze|Ashburn Xtreme 2013|16|11|4|0|1|0|166|10.8|-0.2
15|191|Bronze|The St. James Navy|16|10|6|0|0|0|186|9.8|-0.2
16|170|Bronze|Metro Militia|17|9|6|2|0|0|229|10.9|-0.1
17|136||MYHA 10U LA Blue|18|10|6|0|1|1|193|10.4|-0.1
18|130||MYHA 10U UA Blue|16|9|6|1|0|0|118|10.0|0.0
19|115||Philadelphia Blazers|36|22|12|0|2|0|182|22.3|0.3
20|103||Valley Forge Colonials 10U A Silver|35|18|14|1|2|0|223|19.2|0.2
21|100||Igloo Jaguars|37|23|10|2|2|0|63|26.3|1.3
22|93||Team Philadelphia Black|35|16|16|2|1|0|148|18.0|0.0
23|89||North Jersey Avalanche Gold|12|6|5|1|0|0|116|7.1|0.1
24|55||The St. James White|16|9|5|1|1|0|33|10.8|0.8
25|54||Royals Blue|34|12|18|3|1|0|124|15.1|0.1
26|43||Team Philadelphia Orange|34|16|17|0|1|0|124|17.0|1.0
27|42||Long Island Rebels Squirt Minor|14|6|8|0|0|0|161|6.1|0.1
28|38||Palmyra Black Knights Black|33|11|21|1|0|0|150|12.1|0.1
29|33||Haverford Hawks McDonald|35|10|22|1|2|0|148|11.1|0.1
30|30||Lancaster Firebirds|36|9|19|6|2|0|138|15.9|0.9
31|30||Palmyra Black Knights Red|32|9|20|3|0|0|130|12.7|0.7
32|26||Hollydell Hurricanes White|33|10|21|1|1|0|180|11.5|0.5
33|25||Lehigh Valley Phantoms 1|33|8|22|1|2|0|191|9.1|0.1
34|22||Grundy Senators|34|13|19|0|2|0|69|13.8|0.8
35|22||Hollydell Hurricanes Red|34|10|23|1|0|0|132|11.2|0.2
36|18||Delaware Ducks Teal|35|6|26|1|2|0|245|7.2|0.2
37|14||Lehigh Valley Phantoms 2|34|11|22|0|1|0|88|11.8|0.8
38|13||NJ Stars Green|35|3|31|1|0|0|314|4.1|0.1
39|7||Capital City Vipers 2|34|9|22|0|3|0|109|9.8|0.8
40|3||North Jersey Skyland Kings White|16|3|13|0|0|0|56|3.3|0.3
41|2||NJ Stars Gold|35|3|31|0|1|0|120|3.3|0.3
42|2||MYHA 10U UA Gold|16|1|15|0|0|0|91|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|20.41|-0.36
|Avg|0.49|-0.01

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-A -o scores_10U-A.md scores_10U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

