[<- back to the index](readme.md)
# 9U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2303|Championship|MYHA 9U AA|7|5|1|0|0|1|825|5.8|-0.0
2|1875|Championship|Long Island Whalers Squirt 2014|6|4|1|0|0|1|876|4.8|-0.0
3|1323|Championship|Royals 9U AA White|6|4|1|0|0|1|545|4.9|0.0
4|935|Championship|Delaware Ducks|7|3|3|0|0|1|1411|3.8|-0.0
5|929||Wilkes-Barre / Scranton Jr Knights|6|3|2|0|0|1|919|3.9|0.0
6|423||Team Philadelphia|6|2|3|0|0|1|920|2.9|0.0
7|287||Hollydell Hurricanes|6|2|3|0|0|1|578|2.9|0.0
8|121||Arrows 10u Silver|5|0|4|0|0|1|999|0.9|0.0
9|87||RHC Squirt Minor AA|6|0|5|0|0|1|880|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 9U AA|Long Island Whalers Squirt 2014|Royals 9U AA White|Delaware Ducks|Wilkes-Barre / Scranton Jr Knights|Team Philadelphia|Hollydell Hurricanes|Arrows 10u Silver|RHC Squirt Minor AA
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 9U AA|--| 55%| 64%| 71%| 71%| 84%| 89%| 95%| 96%
|Long Island Whalers Squirt 2014| 45%|--| 59%| 67%| 67%| 82%| 87%| 94%| 96%
|Royals 9U AA White| 36%| 41%|--| 59%| 59%| 76%| 82%| 92%| 94%
|Delaware Ducks| 29%| 33%| 41%|--| 50%| 69%| 77%| 89%| 91%
|Wilkes-Barre / Scranton Jr Knights| 29%| 33%| 41%| 50%|--| 69%| 76%| 88%| 91%
|Team Philadelphia| 16%| 18%| 24%| 31%| 31%|--| 60%| 78%| 83%
|Hollydell Hurricanes| 11%| 13%| 18%| 23%| 24%| 40%|--| 70%| 77%
|Arrows 10u Silver|  5%|  6%|  8%| 11%| 12%| 22%| 30%|--| 58%
|RHC Squirt Minor AA|  4%|  4%|  6%|  9%|  9%| 17%| 23%| 42%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-02 |
| End Date | 2023-09-10 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

