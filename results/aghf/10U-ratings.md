[<- back to the index](readme.md)
# 10U KRACH Rankings
Rankings generated on Sun Oct  1 07:15:14 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|T|OTW|OTL|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|6441|Playoffs|[PTL](https://gamesheetstats.com/seasons/3663/teams/140791/schedule)|5|5|0|0|1|0|170|5.8|-0.0
2|2707|Playoffs|[Jr Flyers Cardillo](https://gamesheetstats.com/seasons/3663/teams/140794/schedule)|3|3|0|0|0|0|107|3.9|0.0
3|408|Playoffs|[STJ](https://gamesheetstats.com/seasons/3663/teams/140792/schedule)|4|2|2|0|0|0|2601|2.8|-0.0
4|83|Playoffs|[LVPY](https://gamesheetstats.com/seasons/3663/teams/140790/schedule)|3|0|3|0|0|0|2970|0.9|0.0
5|39||[New York Islanders](https://gamesheetstats.com/seasons/3663/teams/140793/schedule)|3|0|3|0|0|1|1778|0.9|0.0

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PTL|Jr Flyers Cardillo|STJ|LVPY|New York Islanders
| --: | --: | --: | --: | --: | --: 
|PTL|--| 70%| 94%| 99%| 99%
|Jr Flyers Cardillo| 30%|--| 87%| 97%| 99%
|STJ|  6%| 13%|--| 83%| 91%
|LVPY|  1%|  3%| 17%|--| 68%
|New York Islanders|  1%|  1%|  9%| 32%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-09-09 |
| End Date | 2023-09-30 |
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

