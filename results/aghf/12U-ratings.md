[<- back to the index](readme.md)
# 12U KRACH Rankings
Rankings generated on Wed Sep 27 13:16:26 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|T|OTW|OTL|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3302|Playoffs|[STJ](https://gamesheetstats.com/seasons/3663/teams/140800/schedule)|5|5|0|0|0|0|461|5.8|-0.0
2|2853|Playoffs|[Saugerties Fillies](https://gamesheetstats.com/seasons/3663/teams/140805/schedule)|4|4|0|0|0|0|476|4.9|0.0
3|550|Playoffs|[WBS Lady Knights](https://gamesheetstats.com/seasons/3663/teams/140808/schedule)|6|2|4|0|0|0|1917|2.8|-0.0
4|249|Playoffs|[NJ Bandits](https://gamesheetstats.com/seasons/3663/teams/140807/schedule)|4|0|4|0|0|0|1915|0.9|0.0
5|164||[LVPY](https://gamesheetstats.com/seasons/3663/teams/140804/schedule)|4|0|4|0|0|0|1697|0.8|-0.0

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||STJ|Saugerties Fillies|WBS Lady Knights|NJ Bandits|LVPY
| --: | --: | --: | --: | --: | --: 
|STJ|--| 54%| 86%| 93%| 95%
|Saugerties Fillies| 46%|--| 84%| 92%| 95%
|WBS Lady Knights| 14%| 16%|--| 69%| 77%
|NJ Bandits|  7%|  8%| 31%|--| 60%
|LVPY|  5%|  5%| 23%| 40%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-09 |
| End Date | 2023-09-24 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

