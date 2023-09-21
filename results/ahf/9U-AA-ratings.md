[<- back to the index](readme.md)
# 9U AA KRACH Rankings
Rankings generated on Thu Sep 21 00:11:26 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1988|Championship|Ashburn Xtreme 2014|4|4|0|0|0|0|352|4.8|-0.0
2|1633|Championship|Palmyra Black Knights- Rochefort|3|3|0|0|0|0|360|3.9|0.0
3|1316|Championship|MYHA 9U AA|6|5|1|0|0|0|471|5.8|-0.0
4|1146|Championship|Long Island Whalers Squirt 2014|6|5|1|0|0|0|436|5.8|-0.0
5|649|Gold|Royals 9U AA White|7|5|1|0|0|1|270|6.7|0.0
6|513|Gold|Delaware Ducks|9|4|5|0|0|0|995|4.8|-0.0
7|436|Gold|Wilkes-Barre / Scranton Jr Knights|7|3|4|0|0|0|807|3.9|0.0
8|263|Gold|Hollydell Hurricanes|9|4|4|0|0|1|322|5.7|0.0
9|165||Team Philadelphia|9|2|7|0|0|0|906|2.9|0.0
10|81||Arrows 10u Silver|4|0|4|0|0|0|579|0.9|0.0
11|45||RHC Squirt Minor AA|7|0|7|0|0|0|599|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Ashburn Xtreme 2014|Palmyra Black Knights- Rochefort|MYHA 9U AA|Long Island Whalers Squirt 2014|Royals 9U AA White|Delaware Ducks|Wilkes-Barre / Scranton Jr Knights|Hollydell Hurricanes|Team Philadelphia|Arrows 10u Silver|RHC Squirt Minor AA
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Ashburn Xtreme 2014|--| 55%| 60%| 63%| 75%| 79%| 82%| 88%| 92%| 96%| 98%
|Palmyra Black Knights- Rochefort| 45%|--| 55%| 59%| 72%| 76%| 79%| 86%| 91%| 95%| 97%
|MYHA 9U AA| 40%| 45%|--| 53%| 67%| 72%| 75%| 83%| 89%| 94%| 97%
|Long Island Whalers Squirt 2014| 37%| 41%| 47%|--| 64%| 69%| 72%| 81%| 87%| 93%| 96%
|Royals 9U AA White| 25%| 28%| 33%| 36%|--| 56%| 60%| 71%| 80%| 89%| 94%
|Delaware Ducks| 21%| 24%| 28%| 31%| 44%|--| 54%| 66%| 76%| 86%| 92%
|Wilkes-Barre / Scranton Jr Knights| 18%| 21%| 25%| 28%| 40%| 46%|--| 62%| 73%| 84%| 91%
|Hollydell Hurricanes| 12%| 14%| 17%| 19%| 29%| 34%| 38%|--| 61%| 77%| 85%
|Team Philadelphia|  8%|  9%| 11%| 13%| 20%| 24%| 27%| 39%|--| 67%| 79%
|Arrows 10u Silver|  4%|  5%|  6%|  7%| 11%| 14%| 16%| 23%| 33%|--| 64%
|RHC Squirt Minor AA|  2%|  3%|  3%|  4%|  6%|  8%|  9%| 15%| 21%| 36%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-02 |
| End Date | 2023-09-17 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

