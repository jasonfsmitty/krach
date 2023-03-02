[<- back to the index](readme.md)
# 10U A Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|720|Championship|NJ Bandits Grey|17|15|1|0|0|1|97|15.9|0.0
2|310|Championship|York Devils|37|28|7|0|1|1|131|28.9|0.0
3|268|Championship|Capital City Vipers 1|37|26|8|1|1|1|125|27.9|0.0
4|188|Championship|Southern Maryland Sabres 10U Gold|17|11|4|0|1|1|129|11.9|0.0
5|179|Gold|Ashburn Xtreme 2013|17|11|4|0|1|1|145|11.9|0.0
6|160|Gold|The St. James Navy|17|10|6|0|0|1|167|10.9|0.0
7|105|Gold|MYHA 10U UA Blue|17|9|6|1|0|1|102|10.9|0.0
8|75|Gold|Team Philadelphia Black|37|16|16|2|2|1|127|18.9|0.0
9|55|Silver|Royals Blue|37|13|18|4|1|1|103|17.9|0.0
10|39|Silver|Long Island Rebels Squirt Minor|17|7|9|0|0|1|136|7.9|0.0
11|33|Silver|Haverford Hawks McDonald|37|11|22|1|2|1|126|12.9|0.0
12|31|Silver|Palmyra Black Knights Black|37|11|24|1|0|1|130|12.9|0.0
13|27||Lehigh Valley Phantoms 1|37|10|23|1|2|1|166|11.9|0.0
14|19||Hollydell Hurricanes Red|37|10|25|1|0|1|117|11.9|0.0
15|4||MYHA 10U UA Gold|17|1|15|0|0|1|79|1.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||NJ Bandits Grey|York Devils|Capital City Vipers 1|Southern Maryland Sabres 10U Gold|Ashburn Xtreme 2013|The St. James Navy|MYHA 10U UA Blue|Team Philadelphia Black|Royals Blue|Long Island Rebels Squirt Minor|Haverford Hawks McDonald|Palmyra Black Knights Black|Lehigh Valley Phantoms 1|Hollydell Hurricanes Red|MYHA 10U UA Gold
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|NJ Bandits Grey|--| 70%| 73%| 79%| 80%| 82%| 87%| 91%| 93%| 95%| 96%| 96%| 96%| 97%| 99%
|York Devils| 30%|--| 54%| 62%| 63%| 66%| 75%| 81%| 85%| 89%| 90%| 91%| 92%| 94%| 99%
|Capital City Vipers 1| 27%| 46%|--| 59%| 60%| 63%| 72%| 78%| 83%| 87%| 89%| 90%| 91%| 93%| 98%
|Southern Maryland Sabres 10U Gold| 21%| 38%| 41%|--| 51%| 54%| 64%| 71%| 77%| 83%| 85%| 86%| 88%| 91%| 98%
|Ashburn Xtreme 2013| 20%| 37%| 40%| 49%|--| 53%| 63%| 70%| 76%| 82%| 85%| 85%| 87%| 90%| 98%
|The St. James Navy| 18%| 34%| 37%| 46%| 47%|--| 60%| 68%| 74%| 80%| 83%| 84%| 86%| 89%| 97%
|MYHA 10U UA Blue| 13%| 25%| 28%| 36%| 37%| 40%|--| 58%| 66%| 73%| 76%| 77%| 80%| 84%| 96%
|Team Philadelphia Black|  9%| 19%| 22%| 29%| 30%| 32%| 42%|--| 58%| 66%| 70%| 71%| 74%| 80%| 95%
|Royals Blue|  7%| 15%| 17%| 23%| 24%| 26%| 34%| 42%|--| 59%| 63%| 64%| 67%| 74%| 93%
|Long Island Rebels Squirt Minor|  5%| 11%| 13%| 17%| 18%| 20%| 27%| 34%| 41%|--| 54%| 56%| 60%| 67%| 90%
|Haverford Hawks McDonald|  4%| 10%| 11%| 15%| 15%| 17%| 24%| 30%| 37%| 46%|--| 52%| 55%| 63%| 89%
|Palmyra Black Knights Black|  4%|  9%| 10%| 14%| 15%| 16%| 23%| 29%| 36%| 44%| 48%|--| 53%| 61%| 88%
|Lehigh Valley Phantoms 1|  4%|  8%|  9%| 12%| 13%| 14%| 20%| 26%| 33%| 40%| 45%| 47%|--| 58%| 86%
|Hollydell Hurricanes Red|  3%|  6%|  7%|  9%| 10%| 11%| 16%| 20%| 26%| 33%| 37%| 39%| 42%|--| 82%
|MYHA 10U UA Gold|  1%|  1%|  2%|  2%|  2%|  3%|  4%|  5%|  7%| 10%| 11%| 12%| 14%| 18%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
| End Date | 2023-02-12 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | NORTH JERSEY SPORTSCARE KINGS BLUE,ASHBURN XTREME 10U X,ROYALS WHITE,FREDERICK FREEZE LA,JERSEY SHORE WILDCATS,TOMORROW'S ICE NORTH STARS RED,ROCKETS HOCKEY CLUB BLACK,MARYLAND JR BLACK BEARS WHITE,METRO MILITIA,PHILADELPHIA BLAZERS,MYHA 10U LA BLUE,VALLEY FORGE COLONIALS 10U A SILVER,NORTH JERSEY AVALANCHE GOLD,IGLOO JAGUARS,THE ST. JAMES WHITE,TEAM PHILADELPHIA ORANGE,LANCASTER FIREBIRDS,HOLLYDELL HURRICANES WHITE,PALMYRA BLACK KNIGHTS RED,GRUNDY SENATORS,DELAWARE DUCKS TEAL,NJ STARS GREEN,LEHIGH VALLEY PHANTOMS 2,CAPITAL CITY VIPERS 2,NORTH JERSEY SKYLAND KINGS WHITE,NJ STARS GOLD,NJ BANDITS BLACK,__KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

