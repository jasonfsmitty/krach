[<- back to the index](readme.md)
# 12U KRACH Rankings
Rankings generated on Sat Sep 30 07:13:20 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|T|OTW|OTL|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4515|Playoffs|[STJ](https://gamesheetstats.com/seasons/3663/teams/140800/schedule)|5|5|0|0|0|0|118|5.8|-0.0
2|4030|Playoffs|[Saugerties Fillies](https://gamesheetstats.com/seasons/3663/teams/140805/schedule)|4|4|0|0|0|0|127|4.9|0.0
3|241|Playoffs|[WBS Lady Knights](https://gamesheetstats.com/seasons/3663/teams/140808/schedule)|6|2|4|0|0|0|2456|2.8|-0.0
4|63|Playoffs|[NJ Bandits](https://gamesheetstats.com/seasons/3663/teams/140807/schedule)|4|0|4|0|0|0|2002|0.9|0.0
5|36||[LVPY](https://gamesheetstats.com/seasons/3663/teams/140804/schedule)|4|0|4|0|0|0|1908|0.9|0.0

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||STJ|Saugerties Fillies|WBS Lady Knights|NJ Bandits|LVPY
| --: | --: | --: | --: | --: | --: 
|STJ|--| 53%| 95%| 99%| 99%
|Saugerties Fillies| 47%|--| 94%| 98%| 99%
|WBS Lady Knights|  5%|  6%|--| 79%| 87%
|NJ Bandits|  1%|  2%| 21%|--| 63%
|LVPY|  1%|  1%| 13%| 37%|--

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
| Tie Value | 0.50 |
| Alpha Value | 0.85 |
| Bonus Points | 0.00 |
| Fake Ties | 0 |
| Alpha Games | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

