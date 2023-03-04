[<- back to the index](readme.md)
# USPHL North 16U 06/07 - National KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3710|Frozen 4|Boston Junior Bruins|21|16|3|1|0|1|933|17.8|-0.0
2|2297|Frozen 4|Islander Hockey Club|22|15|5|1|0|1|1153|16.8|-0.0
3|1320|Frozen 4|Springfield Pics|24|15|7|0|1|1|1251|15.9|0.0
4|847|Frozen 4|Cyclones Academy|21|11|8|0|1|1|1421|11.9|0.0
5|533||Boston Advantage|12|6|5|0|0|1|789|6.9|0.0
6|109||New Hampshire Monarchs|24|4|19|0|0|1|1446|4.9|0.0
7|61||South Shore  Kings|24|2|21|0|0|1|1324|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Boston Junior Bruins|Islander Hockey Club|Springfield Pics|Cyclones Academy|Boston Advantage|New Hampshire Monarchs|South Shore  Kings
| --: | --: | --: | --: | --: | --: | --: | --: 
|Boston Junior Bruins|--| 62%| 74%| 81%| 87%| 97%| 98%
|Islander Hockey Club| 38%|--| 64%| 73%| 81%| 95%| 97%
|Springfield Pics| 26%| 36%|--| 61%| 71%| 92%| 96%
|Cyclones Academy| 19%| 27%| 39%|--| 61%| 89%| 93%
|Boston Advantage| 13%| 19%| 29%| 39%|--| 83%| 90%
|New Hampshire Monarchs|  3%|  5%|  8%| 11%| 17%|--| 64%
|South Shore  Kings|  2%|  3%|  4%|  7%| 10%| 36%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-10 |
| End Date | 2023-03-03 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

