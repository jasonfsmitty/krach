[<- back to the index](readme.md)
# 15U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|988|Championship|Delaware Ducks|43|33|5|3|1|1|234|36.8|-0.0
2|457|Championship|MYHA 16U AA Gold|17|10|3|1|2|1|410|11.8|-0.0
3|407|Championship|Team Philadelphia|41|24|10|4|2|1|310|28.9|0.0
4|264|Championship|Long Island Rebels|21|7|10|3|0|1|492|10.8|-0.0
5|238||Royals|41|22|11|3|4|1|283|25.9|0.0
6|47||NJ Bandits|35|11|19|1|3|1|277|12.9|0.0
7|35||Palmyra Black Knights|41|10|25|1|4|1|333|11.9|0.0
8|26||North Jersey Sportscare Kings Yellow|25|5|16|1|2|1|200|6.9|0.0
9|14||Tomorrow's Ice Selects|40|1|33|3|2|1|323|4.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Delaware Ducks|MYHA 16U AA Gold|Team Philadelphia|Long Island Rebels|Royals|NJ Bandits|Palmyra Black Knights|North Jersey Sportscare Kings Yellow|Tomorrow's Ice Selects
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Delaware Ducks|--| 68%| 71%| 79%| 81%| 95%| 97%| 97%| 99%
|MYHA 16U AA Gold| 32%|--| 53%| 63%| 66%| 91%| 93%| 95%| 97%
|Team Philadelphia| 29%| 47%|--| 61%| 63%| 90%| 92%| 94%| 97%
|Long Island Rebels| 21%| 37%| 39%|--| 53%| 85%| 88%| 91%| 95%
|Royals| 19%| 34%| 37%| 47%|--| 84%| 87%| 90%| 94%
|NJ Bandits|  5%|  9%| 10%| 15%| 16%|--| 57%| 64%| 77%
|Palmyra Black Knights|  3%|  7%|  8%| 12%| 13%| 43%|--| 58%| 71%
|North Jersey Sportscare Kings Yellow|  3%|  5%|  6%|  9%| 10%| 36%| 42%|--| 65%
|Tomorrow's Ice Selects|  1%|  3%|  3%|  5%|  6%| 23%| 29%| 35%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-02-11 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

