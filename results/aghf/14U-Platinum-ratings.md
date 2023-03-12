[<- back to the index](readme.md)
# 14U Platinum KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1957|Playoffs|Philadelphia Jr Flyers Sakers|17|14|2|0|0|1|462|14.8|-0.0
2|561|Playoffs|Reston Raiders|17|11|5|0|0|1|619|11.8|-0.0
3|285|Playoffs|New York Islanders|17|11|5|0|0|1|342|11.9|0.0
4|111|Playoffs|MYHA|17|6|9|0|1|1|525|6.9|0.0
5|60||NJ Bandits|26|4|20|1|0|1|607|5.9|0.0
6|33||Lehigh Valley Phantoms|17|2|14|0|0|1|375|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Philadelphia Jr Flyers Sakers|Reston Raiders|New York Islanders|MYHA|NJ Bandits|Lehigh Valley Phantoms
| --: | --: | --: | --: | --: | --: | --: 
|Philadelphia Jr Flyers Sakers|--| 78%| 87%| 95%| 97%| 98%
|Reston Raiders| 22%|--| 66%| 84%| 90%| 95%
|New York Islanders| 13%| 34%|--| 72%| 83%| 90%
|MYHA|  5%| 16%| 28%|--| 65%| 77%
|NJ Bandits|  3%| 10%| 17%| 35%|--| 65%
|Lehigh Valley Phantoms|  2%|  5%| 10%| 23%| 35%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-10 |
| End Date | 2023-02-18 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

