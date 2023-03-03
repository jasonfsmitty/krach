[<- back to the index](readme.md)
# 16U Platinum KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2159|Playoffs|York Lady Devils|26|19|2|4|0|1|282|23.8|-0.0
2|860|Playoffs|Maryland Jr Black Bears|17|11|4|0|1|1|758|11.8|-0.0
3|635|Playoffs|Lehigh Valley Phantoms|17|10|3|2|1|1|368|12.9|0.0
4|211|Playoffs|North Jersey Lady Kings|25|9|9|1|4|2|709|11.7|0.0
5|150||Philadelphia Hockey Club Belles|29|7|16|2|3|1|750|9.9|0.0
6|142||Reston Raiders|17|5|10|1|0|1|791|6.9|0.0
7|28||Rockets Hockey Club|28|1|25|0|0|2|690|2.7|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||York Lady Devils|Maryland Jr Black Bears|Lehigh Valley Phantoms|North Jersey Lady Kings|Philadelphia Hockey Club Belles|Reston Raiders|Rockets Hockey Club
| --: | --: | --: | --: | --: | --: | --: | --: 
|York Lady Devils|--| 72%| 77%| 91%| 93%| 94%| 99%
|Maryland Jr Black Bears| 28%|--| 58%| 80%| 85%| 86%| 97%
|Lehigh Valley Phantoms| 23%| 42%|--| 75%| 81%| 82%| 96%
|North Jersey Lady Kings|  9%| 20%| 25%|--| 58%| 60%| 88%
|Philadelphia Hockey Club Belles|  7%| 15%| 19%| 42%|--| 51%| 84%
|Reston Raiders|  6%| 14%| 18%| 40%| 49%|--| 84%
|Rockets Hockey Club|  1%|  3%|  4%| 12%| 16%| 16%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-11 |
| End Date | 2023-02-18 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

