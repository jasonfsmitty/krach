[<- back to the index](readme.md)
# 9U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2872|Championship|Royals 9U AA White|5|4|0|0|0|1|494|4.8|-0.0
2|1630|Championship|Long Island Whalers Squirt 2014|5|3|1|0|0|1|901|3.9|0.0
3|1454|Championship|Delaware Ducks|5|3|1|0|0|1|851|3.9|0.0
4|1454|Championship|MYHA 9U AA|5|3|1|0|0|1|851|3.9|0.0
5|759||Wilkes-Barre / Scranton Jr Knights|5|2|2|0|0|1|1170|2.8|-0.0
6|508||Hollydell Hurricanes|5|2|2|0|0|1|918|2.8|-0.0
7|363||Team Philadelphia|5|1|3|0|0|1|1317|1.9|0.0
8|154||Arrows 10u Silver|5|0|4|0|0|1|1291|0.8|-0.0
9|121||RHC Squirt Minor AA|5|0|4|0|0|1|893|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Royals 9U AA White|Long Island Whalers Squirt 2014|Delaware Ducks|MYHA 9U AA|Wilkes-Barre / Scranton Jr Knights|Hollydell Hurricanes|Team Philadelphia|Arrows 10u Silver|RHC Squirt Minor AA
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Royals 9U AA White|--| 64%| 66%| 66%| 79%| 85%| 89%| 95%| 96%
|Long Island Whalers Squirt 2014| 36%|--| 53%| 53%| 68%| 76%| 82%| 91%| 93%
|Delaware Ducks| 34%| 47%|--| 50%| 66%| 74%| 80%| 90%| 92%
|MYHA 9U AA| 34%| 47%| 50%|--| 66%| 74%| 80%| 90%| 92%
|Wilkes-Barre / Scranton Jr Knights| 21%| 32%| 34%| 34%|--| 60%| 68%| 83%| 86%
|Hollydell Hurricanes| 15%| 24%| 26%| 26%| 40%|--| 58%| 77%| 81%
|Team Philadelphia| 11%| 18%| 20%| 20%| 32%| 42%|--| 70%| 75%
|Arrows 10u Silver|  5%|  9%| 10%| 10%| 17%| 23%| 30%|--| 56%
|RHC Squirt Minor AA|  4%|  7%|  8%|  8%| 14%| 19%| 25%| 44%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-02 |
| End Date | 2023-09-03 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

