[<- back to the index](readme.md)
# 16U Diamond KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3551|Playoffs|NJ Bandits|25|21|2|0|1|1|720|21.8|-0.0
2|1711|Playoffs|Princeton Tiger Lilies Black|26|17|6|1|0|2|1109|19.7|-0.0
3|938|Playoffs|Princeton Tiger Lilies Orange|27|16|8|1|0|2|907|18.7|0.0
4|515|Playoffs|The St. James|24|9|13|1|0|1|1360|10.9|0.0
5|372||MYHA|16|6|8|0|1|1|952|6.9|0.0
6|60||Philadelphia Jr Flyers Binns|17|1|14|0|1|1|1236|1.9|0.0
7|54||NY Islanders-Twin Rinks at Eisenhower Youth - 16U AA|17|1|14|0|1|1|1547|1.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||NJ Bandits|Princeton Tiger Lilies Black|Princeton Tiger Lilies Orange|The St. James|MYHA|Philadelphia Jr Flyers Binns|NY Islanders-Twin Rinks at Eisenhower Youth - 16U AA
| --: | --: | --: | --: | --: | --: | --: | --: 
|NJ Bandits|--| 67%| 79%| 87%| 91%| 98%| 98%
|Princeton Tiger Lilies Black| 33%|--| 65%| 77%| 82%| 97%| 97%
|Princeton Tiger Lilies Orange| 21%| 35%|--| 65%| 72%| 94%| 95%
|The St. James| 13%| 23%| 35%|--| 58%| 90%| 90%
|MYHA|  9%| 18%| 28%| 42%|--| 86%| 87%
|Philadelphia Jr Flyers Binns|  2%|  3%|  6%| 10%| 14%|--| 53%
|NY Islanders-Twin Rinks at Eisenhower Youth - 16U AA|  2%|  3%|  5%| 10%| 13%| 47%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-10 |
| End Date | 2023-02-12 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

