[<- back to the index](readme.md)
# 10U KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|6656|Playoffs|MYHA|17|16|0|0|0|1|388|16.8|-0.0
2|2116|Playoffs|Saugerties Fillies|16|13|2|0|0|1|1025|13.9|0.0
3|421|Playoffs|Princeton Tiger Lilies|15|7|6|0|1|1|1563|7.9|0.0
4|379|Playoffs|NJ Bandits|16|8|6|1|0|1|1219|9.9|0.0
5|60||NY Islaners-Twin Rinks At Eisenhower Youth - 10U|16|2|12|1|0|1|1384|3.9|0.0
6|51||Philadelphia Jr Flyers|17|3|12|0|1|1|1941|3.9|0.0
7|42||The St. James|16|2|13|0|0|1|2063|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA|Saugerties Fillies|Princeton Tiger Lilies|NJ Bandits|NY Islaners-Twin Rinks At Eisenhower Youth - 10U|Philadelphia Jr Flyers|The St. James
| --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA|--| 76%| 94%| 95%| 99%| 99%| 99%
|Saugerties Fillies| 24%|--| 83%| 85%| 97%| 98%| 98%
|Princeton Tiger Lilies|  6%| 17%|--| 53%| 88%| 89%| 91%
|NJ Bandits|  5%| 15%| 47%|--| 86%| 88%| 90%
|NY Islaners-Twin Rinks At Eisenhower Youth - 10U|  1%|  3%| 12%| 14%|--| 54%| 59%
|Philadelphia Jr Flyers|  1%|  2%| 11%| 12%| 46%|--| 55%
|The St. James|  1%|  2%|  9%| 10%| 41%| 45%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-18 |
| End Date | 2023-02-17 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

