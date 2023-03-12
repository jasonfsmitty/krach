[<- back to the index](readme.md)
# 14U Diamond KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|7595|Playoffs|Princeton Tiger Lilies Black|27|26|0|0|0|1|261|26.8|-0.0
2|1122|Playoffs|South Pittsburgh Rebellion|17|12|4|0|0|1|1887|12.8|-0.0
3|270|Playoffs|The St. James|27|16|9|1|0|1|1026|17.9|0.0
4|182|Playoffs|MCU|12|7|4|0|0|1|1325|7.9|0.0
5|110|Playoffs|NJ Bandits|30|12|14|1|2|1|958|13.9|0.0
6|108|Playoffs|MYHA Blue|18|6|9|1|1|1|1428|7.9|0.0
7|85||Stateline Hawks|27|7|16|2|1|1|1370|9.9|0.0
8|73||Princeton Tiger Lilies Orange|30|15|13|0|1|1|98|15.9|0.0
9|66||NY Islanders-Twin Rinks at Eisenhower Youth - 14U AA|16|6|8|1|0|1|557|7.9|0.0
10|42||Lady Bulldogs|14|3|10|0|0|1|1700|3.9|0.0
11|25||Lady Islanders White|15|3|11|0|0|1|671|3.9|0.0
12|19||MYHA Gold|17|3|13|0|0|1|532|3.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Princeton Tiger Lilies Black|South Pittsburgh Rebellion|The St. James|MCU|NJ Bandits|MYHA Blue|Stateline Hawks|Princeton Tiger Lilies Orange|NY Islanders-Twin Rinks at Eisenhower Youth - 14U AA|Lady Bulldogs|Lady Islanders White|MYHA Gold
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Princeton Tiger Lilies Black|--| 87%| 97%| 98%| 99%| 99%| 99%| 99%| 99%| 99%|100%|100%
|South Pittsburgh Rebellion| 13%|--| 81%| 86%| 91%| 91%| 93%| 94%| 94%| 96%| 98%| 98%
|The St. James|  3%| 19%|--| 60%| 71%| 71%| 76%| 79%| 80%| 86%| 91%| 93%
|MCU|  2%| 14%| 40%|--| 62%| 63%| 68%| 72%| 73%| 81%| 88%| 90%
|NJ Bandits|  1%|  9%| 29%| 38%|--| 51%| 56%| 60%| 62%| 72%| 81%| 85%
|MYHA Blue|  1%|  9%| 29%| 37%| 49%|--| 56%| 60%| 62%| 72%| 81%| 85%
|Stateline Hawks|  1%|  7%| 24%| 32%| 44%| 44%|--| 54%| 56%| 67%| 77%| 82%
|Princeton Tiger Lilies Orange|  1%|  6%| 21%| 28%| 40%| 40%| 46%|--| 52%| 63%| 74%| 79%
|NY Islanders-Twin Rinks at Eisenhower Youth - 14U AA|  1%|  6%| 20%| 27%| 38%| 38%| 44%| 48%|--| 61%| 72%| 77%
|Lady Bulldogs|  1%|  4%| 14%| 19%| 28%| 28%| 33%| 37%| 39%|--| 63%| 69%
|Lady Islanders White|  0%|  2%|  9%| 12%| 19%| 19%| 23%| 26%| 28%| 37%|--| 57%
|MYHA Gold|  0%|  2%|  7%| 10%| 15%| 15%| 18%| 21%| 23%| 31%| 43%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-17 |
| End Date | 2023-02-18 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

