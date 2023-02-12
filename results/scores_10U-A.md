# 10U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1119|Championship|North Jersey Sportscare Kings Blue|16|14|1|1|0|0|259|13.5|-1.5
2|825|Championship|Ashburn Xtreme 10U X|16|13|1|1|1|0|276|12.8|-1.2
3|784|Championship|Royals White|36|29|3|3|1|0|228|29.5|-2.5
4|688|Championship|NJ Bandits Grey|16|15|1|0|0|0|112|14.0|-1.0
5|434|Gold|Frederick Freeze LA|16|15|1|0|0|0|75|14.5|-0.5
6|360|Gold|NJ Bandits Black|16|11|5|0|0|0|343|10.3|-0.7
7|342|Gold|York Devils|36|28|7|0|1|0|147|27.2|-0.8
8|302|Gold|Capital City Vipers 1|35|25|8|1|1|0|146|25.4|-0.6
9|286|Silver|Jersey Shore Wildcats|16|10|5|1|0|0|290|10.5|-0.5
10|262|Silver|Maryland Jr Black Bears White|16|12|4|0|0|0|131|12.0|0.0
11|244|Silver|Tomorrow's Ice North Stars Red|18|13|3|0|1|1|199|13.2|-0.3
12|233|Silver|Southern Maryland Sabres 10U Gold|16|11|4|0|1|0|150|10.8|-0.2
13|226|Bronze|Rockets Hockey Club Black|36|25|8|1|2|0|186|25.6|-0.4
14|221|Bronze|Ashburn Xtreme 2013|16|11|4|0|1|0|162|10.8|-0.2
15|192|Bronze|The St. James Navy|16|10|6|0|0|0|187|9.8|-0.2
16|171|Bronze|Metro Militia|17|9|6|2|0|0|230|10.9|-0.1
17|137||MYHA 10U LA Blue|18|10|6|0|1|1|195|10.4|-0.1
18|130||MYHA 10U UA Blue|16|9|6|1|0|0|117|10.0|0.0
19|117||Philadelphia Blazers|36|22|12|0|2|0|184|22.3|0.3
20|108||Valley Forge Colonials 10U A Silver|36|19|14|1|2|0|219|20.2|0.2
21|102||Igloo Jaguars|37|23|10|2|2|0|64|26.2|1.2
22|93||Team Philadelphia Black|35|16|16|2|1|0|147|18.0|0.0
23|89||North Jersey Avalanche Gold|12|6|5|1|0|0|117|7.1|0.1
24|58||Royals Blue|35|13|18|3|1|0|121|16.2|0.2
25|56||The St. James White|16|9|5|1|1|0|34|10.8|0.8
26|45||Team Philadelphia Orange|35|16|17|1|1|0|122|18.1|1.1
27|41||Long Island Rebels Squirt Minor|16|7|9|0|0|0|143|7.1|0.1
28|35||Haverford Hawks McDonald|36|11|22|1|2|0|144|12.1|0.1
29|33||Palmyra Black Knights Black|35|11|23|1|0|0|144|12.1|0.1
30|30||Lancaster Firebirds|36|9|19|6|2|0|139|15.9|0.9
31|29||Palmyra Black Knights Red|34|10|21|3|0|0|125|13.8|0.8
32|28||Hollydell Hurricanes White|34|11|21|1|1|0|176|12.5|0.5
33|26||Lehigh Valley Phantoms 1|35|9|23|1|2|0|182|10.1|0.1
34|24||Grundy Senators|35|14|19|0|2|0|69|14.9|0.9
35|21||Hollydell Hurricanes Red|35|10|24|1|0|0|131|11.2|0.2
36|18||Delaware Ducks Teal|35|6|26|1|2|0|247|7.2|0.2
37|13||Lehigh Valley Phantoms 2|35|11|23|0|1|0|88|11.8|0.8
38|12||NJ Stars Green|36|3|32|1|0|0|307|4.1|0.1
39|7||Capital City Vipers 2|35|9|22|0|4|0|108|9.8|0.8
40|3||North Jersey Skyland Kings White|16|3|13|0|0|0|56|3.3|0.3
41|2||NJ Stars Gold|35|3|31|0|1|0|120|3.3|0.3
42|2||MYHA 10U UA Gold|16|1|15|0|0|0|88|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|20.75|-0.34
|Avg|0.49|-0.01

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 10U-A -o scores_10U-A.md scores_10U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

