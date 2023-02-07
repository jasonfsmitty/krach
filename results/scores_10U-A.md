# 10U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|922|Championship|North Jersey Sportscare Kings Blue|16|14|1|1|0|0|241|13.2|-1.3
2|789|Championship|Ashburn Xtreme 10U X|16|13|1|1|1|0|247|12.9|-1.1
3|708|Championship|NJ Bandits Grey|16|15|1|0|0|0|119|14.0|-1.0
4|673|Championship|Royals White|36|29|3|3|1|0|217|28.9|-2.1
5|439|Gold|Frederick Freeze LA|16|15|1|0|0|0|70|14.5|-0.5
6|401|Gold|York Devils|35|28|6|0|1|0|144|27.6|-0.9
7|363|Gold|NJ Bandits Black|16|11|5|0|0|0|317|10.4|-0.6
8|288|Gold|Tomorrow's Ice North Stars Red|18|13|3|0|1|1|176|13.6|-0.4
9|282|Silver|Capital City Vipers 1|34|24|8|1|1|0|148|24.5|-0.5
10|263|Silver|Southern Maryland Sabres 10U Gold|16|11|4|0|1|0|149|11.3|-0.2
11|262|Silver|Ashburn Xtreme 2013|16|11|4|0|1|0|170|11.3|-0.2
12|258|Silver|Maryland Jr Black Bears White|16|12|4|0|0|0|123|12.0|0.0
13|237|Bronze|Rockets Hockey Club Black|36|25|8|1|2|0|165|26.1|-0.4
14|235|Bronze|Jersey Shore Wildcats|16|10|5|1|0|0|265|10.1|-0.4
15|188|Bronze|The St. James Navy|16|10|6|0|0|0|189|9.8|-0.2
16|155|Bronze|MYHA 10U LA Blue|18|10|6|0|1|1|183|10.9|-0.1
17|140||Philadelphia Blazers|36|22|12|0|2|0|175|23.1|0.1
18|126||Metro Militia|17|9|6|2|0|0|213|10.0|0.0
19|112||Valley Forge Colonials 10U A Silver|35|18|14|1|2|0|210|19.6|0.1
20|108||MYHA 10U UA Blue|16|9|6|1|0|0|120|9.6|0.1
21|103||Igloo Jaguars|37|23|10|2|2|0|63|26.2|1.2
22|85||Team Philadelphia Black|35|16|16|2|1|0|153|17.6|0.1
23|70||North Jersey Avalanche Gold|12|6|5|1|0|0|115|6.6|0.1
24|56||The St. James White|16|9|5|1|1|0|34|10.8|0.8
25|49||Team Philadelphia Orange|34|16|17|0|1|0|122|17.4|0.9
26|46||Royals Blue|34|12|18|3|1|0|130|14.2|0.2
27|41||Long Island Rebels Squirt Minor|14|6|8|0|0|0|162|6.1|0.1
28|34||Haverford Hawks McDonald|35|10|22|1|2|0|152|11.6|0.1
29|33||Palmyra Black Knights Black|33|11|21|1|0|0|154|11.6|0.1
30|28||Hollydell Hurricanes White|33|10|21|1|1|0|168|11.4|0.4
31|27||Grundy Senators|34|13|19|0|2|0|71|14.8|0.8
32|26||Lehigh Valley Phantoms 1|33|8|22|1|2|0|194|9.6|0.1
33|24||Lancaster Firebirds|36|9|19|6|2|0|132|13.8|0.8
34|24||Palmyra Black Knights Red|32|9|20|3|0|0|134|11.1|0.6
35|20||Delaware Ducks Teal|35|6|26|1|2|0|236|7.7|0.2
36|19||Hollydell Hurricanes Red|34|10|23|1|0|0|135|10.7|0.2
37|16||Lehigh Valley Phantoms 2|34|11|22|0|1|0|89|12.3|0.8
38|12||Capital City Vipers 2|34|9|22|0|3|0|117|11.3|0.8
39|10||NJ Stars Green|35|3|31|1|0|0|285|3.6|0.1
40|4||North Jersey Skyland Kings White|16|3|13|0|0|0|60|3.3|0.3
41|2||NJ Stars Gold|35|3|31|0|1|0|120|3.8|0.3
42|2||MYHA 10U UA Gold|16|1|15|0|0|0|92|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|19.51|-0.30
|Avg|0.46|-0.01

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 0.5 --tie 0.5 --min-games 12 -n 10U-A -o scores_10U-A.md scores_10U-A.js
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
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

