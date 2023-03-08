[<- back to the index](readme.md)
# 15U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|921|Championship|Delaware Ducks|43|33|5|3|1|1|218|36.8|-0.0
2|431|Championship|MYHA 16U AA Gold|17|10|3|1|2|1|386|11.8|-0.0
3|360|Championship|Team Philadelphia|42|24|11|4|2|1|295|28.9|0.0
4|248|Championship|Long Island Rebels|21|7|10|3|0|1|461|10.8|-0.0
5|223||Royals|41|22|11|3|4|1|265|25.9|0.0
6|44||NJ Bandits|35|11|19|1|3|1|258|12.9|0.0
7|33||Palmyra Black Knights|41|10|25|1|4|1|309|11.9|0.0
8|24||North Jersey Sportscare Kings Yellow|25|5|16|1|2|1|186|6.9|0.0
9|13||Tomorrow's Ice Selects|40|1|33|3|2|1|301|4.9|0.0

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
|Delaware Ducks|--| 68%| 72%| 79%| 80%| 95%| 97%| 97%| 99%
|MYHA 16U AA Gold| 32%|--| 54%| 64%| 66%| 91%| 93%| 95%| 97%
|Team Philadelphia| 28%| 46%|--| 59%| 62%| 89%| 92%| 94%| 96%
|Long Island Rebels| 21%| 36%| 41%|--| 53%| 85%| 88%| 91%| 95%
|Royals| 20%| 34%| 38%| 47%|--| 84%| 87%| 90%| 94%
|NJ Bandits|  5%|  9%| 11%| 15%| 16%|--| 57%| 64%| 77%
|Palmyra Black Knights|  3%|  7%|  8%| 12%| 13%| 43%|--| 58%| 71%
|North Jersey Sportscare Kings Yellow|  3%|  5%|  6%|  9%| 10%| 36%| 42%|--| 65%
|Tomorrow's Ice Selects|  1%|  3%|  4%|  5%|  6%| 23%| 29%| 35%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-03-05 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

