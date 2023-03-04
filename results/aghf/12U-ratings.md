[<- back to the index](readme.md)
# 12U KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|5313|Playoffs|Princeton Tiger Lilies Black|18|14|0|2|1|1|619|16.8|-0.0
2|1106|Playoffs|MYHA|17|10|4|1|1|1|1273|11.8|-0.0
3|891|Playoffs|The St. James|25|13|7|3|1|1|1198|16.8|-0.0
4|709|Playoffs|Lady Islanders|19|10|6|1|1|1|1209|11.8|-0.0
5|489||WBS Lady Knights|17|11|4|1|0|1|537|12.9|0.0
6|139||Saugerties Fillies|25|12|8|0|4|1|538|12.9|0.0
7|67||NY Islanders-Twin Rinks at Eisenhower Youth - 12U AA|17|4|11|1|0|1|626|5.9|0.0
8|34||NJ Bandits|24|4|18|1|0|1|634|5.9|0.0
9|5||Princeton Tiger Lilies Orange|19|0|17|0|1|1|352|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Princeton Tiger Lilies Black|MYHA|The St. James|Lady Islanders|WBS Lady Knights|Saugerties Fillies|NY Islanders-Twin Rinks at Eisenhower Youth - 12U AA|NJ Bandits|Princeton Tiger Lilies Orange
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Princeton Tiger Lilies Black|--| 83%| 86%| 88%| 92%| 97%| 99%| 99%|100%
|MYHA| 17%|--| 55%| 61%| 69%| 89%| 94%| 97%|100%
|The St. James| 14%| 45%|--| 56%| 65%| 86%| 93%| 96%| 99%
|Lady Islanders| 12%| 39%| 44%|--| 59%| 84%| 91%| 95%| 99%
|WBS Lady Knights|  8%| 31%| 35%| 41%|--| 78%| 88%| 93%| 99%
|Saugerties Fillies|  3%| 11%| 14%| 16%| 22%|--| 67%| 80%| 97%
|NY Islanders-Twin Rinks at Eisenhower Youth - 12U AA|  1%|  6%|  7%|  9%| 12%| 33%|--| 66%| 93%
|NJ Bandits|  1%|  3%|  4%|  5%|  7%| 20%| 34%|--| 88%
|Princeton Tiger Lilies Orange|  0%|  0%|  1%|  1%|  1%|  3%|  7%| 12%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-17 |
| End Date | 2023-02-05 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

