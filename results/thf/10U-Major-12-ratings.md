[<- back to the index](readme.md)
# 10U Major 12 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2564|Super 6|PAL Jr. Islanders|26|20|4|1|0|1|658|21.8|-0.0
2|1862|Super 6|CT Jr. Rangers Elite|18|10|4|1|2|1|1256|11.8|-0.0
3|1453|Super 6|MCU Elite|13|6|3|1|2|1|1215|7.8|-0.0
4|1150|Super 6|Woodbridge Wolfpack|30|15|7|2|5|1|1069|17.8|-0.0
5|833|Super 6|Jersey Hitmen|31|14|12|3|1|1|972|17.8|-0.0
6|603|Super 6|Westchester Express|30|12|13|4|0|1|795|16.9|0.0
7|559|Frozen 4|Revolution Elite|27|15|8|0|3|1|652|15.9|0.0
8|246|Frozen 4|NY Aviators|29|14|13|1|0|1|523|15.9|0.0
9|152|Frozen 4|Mercer Chiefs|29|11|17|0|0|1|579|11.9|0.0
10|87|Frozen 4|Utica Jr. Comets|18|6|10|1|0|1|453|7.9|0.0
11|63||Rockets Hockey Club|32|6|25|0|0|1|669|6.9|0.0
12|14||Hartford Jr. Wolfpack|17|1|14|0|1|1|155|1.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PAL Jr. Islanders|CT Jr. Rangers Elite|MCU Elite|Woodbridge Wolfpack|Jersey Hitmen|Westchester Express|Revolution Elite|NY Aviators|Mercer Chiefs|Utica Jr. Comets|Rockets Hockey Club|Hartford Jr. Wolfpack
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|PAL Jr. Islanders|--| 58%| 64%| 69%| 75%| 81%| 82%| 91%| 94%| 97%| 98%| 99%
|CT Jr. Rangers Elite| 42%|--| 56%| 62%| 69%| 76%| 77%| 88%| 92%| 96%| 97%| 99%
|MCU Elite| 36%| 44%|--| 56%| 64%| 71%| 72%| 86%| 91%| 94%| 96%| 99%
|Woodbridge Wolfpack| 31%| 38%| 44%|--| 58%| 66%| 67%| 82%| 88%| 93%| 95%| 99%
|Jersey Hitmen| 25%| 31%| 36%| 42%|--| 58%| 60%| 77%| 85%| 91%| 93%| 98%
|Westchester Express| 19%| 24%| 29%| 34%| 42%|--| 52%| 71%| 80%| 87%| 90%| 98%
|Revolution Elite| 18%| 23%| 28%| 33%| 40%| 48%|--| 69%| 79%| 87%| 90%| 98%
|NY Aviators|  9%| 12%| 14%| 18%| 23%| 29%| 31%|--| 62%| 74%| 79%| 95%
|Mercer Chiefs|  6%|  8%|  9%| 12%| 15%| 20%| 21%| 38%|--| 64%| 70%| 92%
|Utica Jr. Comets|  3%|  4%|  6%|  7%|  9%| 13%| 13%| 26%| 36%|--| 58%| 86%
|Rockets Hockey Club|  2%|  3%|  4%|  5%|  7%| 10%| 10%| 21%| 30%| 42%|--| 82%
|Hartford Jr. Wolfpack|  1%|  1%|  1%|  1%|  2%|  2%|  2%|  5%|  8%| 14%| 18%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-03 |
| End Date | 2023-02-26 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

