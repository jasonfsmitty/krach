[<- back to the index](readme.md)
# 15U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|5053|Championship|Delaware Ducks|42|33|5|3|1|0|1634|34.8|-1.2
2|2802|Championship|MYHA 16U AA Gold|16|10|3|1|2|0|3359|10.7|-0.3
3|2332|Championship|Team Philadelphia|40|24|10|4|2|0|2083|27.8|-0.2
4|1545|Championship|Long Island Rebels|20|7|10|3|0|0|3622|9.9|-0.1
5|1475||Royals|40|22|11|3|4|0|2408|25.3|0.3
6|238||NJ Bandits|34|11|19|1|3|0|1978|12.9|0.9
7|165||Palmyra Black Knights|40|10|25|1|4|0|2169|11.7|0.7
8|116||North Jersey Sportscare Kings Yellow|24|5|16|1|2|0|1091|6.5|0.5
9|61||Tomorrow's Ice Selects|39|1|33|3|2|0|1922|4.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|4.37|0.80
|Avg|0.49|0.09

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Delaware Ducks|MYHA 16U AA Gold|Team Philadelphia|Long Island Rebels|Royals|NJ Bandits|Palmyra Black Knights|North Jersey Sportscare Kings Yellow|Tomorrow's Ice Selects
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Delaware Ducks|--| 64%| 68%| 77%| 77%| 95%| 97%| 98%| 99%
|MYHA 16U AA Gold| 36%|--| 55%| 64%| 66%| 92%| 94%| 96%| 98%
|Team Philadelphia| 32%| 45%|--| 60%| 61%| 91%| 93%| 95%| 97%
|Long Island Rebels| 23%| 36%| 40%|--| 51%| 87%| 90%| 93%| 96%
|Royals| 23%| 34%| 39%| 49%|--| 86%| 90%| 93%| 96%
|NJ Bandits|  5%|  8%|  9%| 13%| 14%|--| 59%| 67%| 80%
|Palmyra Black Knights|  3%|  6%|  7%| 10%| 10%| 41%|--| 59%| 73%
|North Jersey Sportscare Kings Yellow|  2%|  4%|  5%|  7%|  7%| 33%| 41%|--| 66%
|Tomorrow's Ice Selects|  1%|  2%|  3%|  4%|  4%| 20%| 27%| 34%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
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

