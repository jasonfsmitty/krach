# 10U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1120|Championship|North Jersey Sportscare Kings Blue|16|14|1|1|0|0|260|13.5|-1.5
2|824|Championship|Ashburn Xtreme 10U X|16|13|1|1|1|0|277|12.8|-1.2
3|788|Championship|Royals White|36|29|3|3|1|0|229|29.5|-2.5
4|688|Championship|NJ Bandits Grey|16|15|1|0|0|0|112|14.0|-1.0
5|434|Gold|Frederick Freeze LA|16|15|1|0|0|0|75|14.5|-0.5
6|361|Gold|NJ Bandits Black|16|11|5|0|0|0|343|10.3|-0.7
7|341|Gold|York Devils|36|28|7|0|1|0|147|27.2|-0.8
8|304|Gold|Capital City Vipers 1|36|26|8|1|1|0|143|26.4|-0.6
9|288|Silver|Jersey Shore Wildcats|16|10|5|1|0|0|291|10.5|-0.5
10|258|Silver|Maryland Jr Black Bears White|16|12|4|0|0|0|130|12.0|0.0
11|246|Silver|Tomorrow's Ice North Stars Red|18|13|3|0|1|1|200|13.2|-0.3
12|232|Silver|Southern Maryland Sabres 10U Gold|16|11|4|0|1|0|150|10.8|-0.2
13|227|Bronze|Rockets Hockey Club Black|36|25|8|1|2|0|186|25.6|-0.4
14|220|Bronze|Ashburn Xtreme 2013|16|11|4|0|1|0|161|10.8|-0.2
15|192|Bronze|The St. James Navy|16|10|6|0|0|0|188|9.8|-0.2
16|169|Bronze|Metro Militia|17|9|6|2|0|0|229|10.9|-0.1
17|138||MYHA 10U LA Blue|18|10|6|0|1|1|196|10.4|-0.1
18|129||MYHA 10U UA Blue|16|9|6|1|0|0|117|10.0|0.0
19|120||Philadelphia Blazers|37|23|12|0|2|0|180|23.3|0.3
20|109||Valley Forge Colonials 10U A Silver|36|19|14|1|2|0|220|20.2|0.2
21|93||Team Philadelphia Black|35|16|16|2|1|0|147|18.0|0.0
22|91||Igloo Jaguars|38|23|11|2|2|0|62|26.3|1.3
23|89||North Jersey Avalanche Gold|12|6|5|1|0|0|116|7.1|0.1
24|57||Royals Blue|35|13|18|3|1|0|121|16.2|0.2
25|56||The St. James White|16|9|5|1|1|0|33|10.8|0.8
26|46||Team Philadelphia Orange|35|16|17|1|1|0|121|18.0|1.0
27|41||Long Island Rebels Squirt Minor|16|7|9|0|0|0|143|7.1|0.1
28|35||Haverford Hawks McDonald|36|11|22|1|2|0|144|12.1|0.1
29|32||Hollydell Hurricanes White|36|13|21|1|1|0|168|14.6|0.6
30|32||Palmyra Black Knights Black|36|11|24|1|0|0|148|12.1|0.1
31|31||Lancaster Firebirds|36|9|19|6|2|0|140|15.9|0.9
32|29||Palmyra Black Knights Red|34|10|21|3|0|0|124|13.8|0.8
33|27||Lehigh Valley Phantoms 1|36|10|23|1|2|0|177|11.1|0.1
34|23||Grundy Senators|37|14|20|0|2|1|66|15.4|0.9
35|19||Hollydell Hurricanes Red|36|10|25|1|0|0|129|11.2|0.2
36|17||Delaware Ducks Teal|36|6|27|1|2|0|242|7.2|0.2
37|16||Lehigh Valley Phantoms 2|36|12|23|0|1|0|88|12.8|0.8
38|12||NJ Stars Green|36|3|32|1|0|0|308|4.1|0.1
39|8||Capital City Vipers 2|37|9|23|0|4|1|106|10.3|0.8
40|3||North Jersey Skyland Kings White|16|3|13|0|0|0|56|3.3|0.3
41|2||NJ Stars Gold|35|3|31|0|1|0|120|3.3|0.3
42|2||MYHA 10U UA Gold|16|1|15|0|0|0|88|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|21.00|-0.34
|Avg|0.50|-0.01

## Generation Details

Generated with command line:
```
../ahf.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-A -o 10U-A-ratings.md 10U-A-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

