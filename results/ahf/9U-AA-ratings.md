[<- back to the index](readme.md)
# 9U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1890|Championship|MYHA 9U AA|7|5|1|0|0|1|681|5.8|-0.0
2|1454|Championship|Long Island Whalers Squirt 2014|6|4|1|0|0|1|689|4.8|-0.0
3|839|Championship|Delaware Ducks|8|4|3|0|0|1|1019|4.8|-0.0
4|766|Championship|Royals 9U AA White|8|5|1|0|0|2|324|6.7|0.0
5|526||Wilkes-Barre / Scranton Jr Knights|7|3|3|0|0|1|694|3.9|0.0
6|252||Team Philadelphia|8|2|5|0|0|1|824|2.9|0.0
7|234||Hollydell Hurricanes|8|2|4|0|0|2|473|3.7|0.0
8|89||Arrows 10u Silver|5|0|4|0|0|1|691|0.9|0.0
9|67||RHC Squirt Minor AA|6|0|5|0|0|1|715|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 9U AA|Long Island Whalers Squirt 2014|Delaware Ducks|Royals 9U AA White|Wilkes-Barre / Scranton Jr Knights|Team Philadelphia|Hollydell Hurricanes|Arrows 10u Silver|RHC Squirt Minor AA
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 9U AA|--| 57%| 69%| 71%| 78%| 88%| 89%| 96%| 97%
|Long Island Whalers Squirt 2014| 43%|--| 63%| 65%| 73%| 85%| 86%| 94%| 96%
|Delaware Ducks| 31%| 37%|--| 52%| 61%| 77%| 78%| 90%| 93%
|Royals 9U AA White| 29%| 35%| 48%|--| 59%| 75%| 77%| 90%| 92%
|Wilkes-Barre / Scranton Jr Knights| 22%| 27%| 39%| 41%|--| 68%| 69%| 86%| 89%
|Team Philadelphia| 12%| 15%| 23%| 25%| 32%|--| 52%| 74%| 79%
|Hollydell Hurricanes| 11%| 14%| 22%| 23%| 31%| 48%|--| 72%| 78%
|Arrows 10u Silver|  4%|  6%| 10%| 10%| 14%| 26%| 28%|--| 57%
|RHC Squirt Minor AA|  3%|  4%|  7%|  8%| 11%| 21%| 22%| 43%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-02 |
| End Date | 2023-09-16 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

