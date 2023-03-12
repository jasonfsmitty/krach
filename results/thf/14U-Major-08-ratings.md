[<- back to the index](readme.md)
# 14U Major 08 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1303|Super 6|PAL Jr. Islanders|20|17|2|0|0|1|211|17.9|0.0
2|339|Super 6|Mercer Chiefs Premier|20|9|8|1|0|2|554|11.7|-0.0
3|328|Super 6|NY Aviators|14|8|3|1|1|1|195|9.9|0.0
4|297|Super 6|Revolution Elite|18|8|5|2|2|1|315|10.9|0.0
5|293|Super 6|Philadelphia Flyers Elite|16|6|7|1|1|1|1125|7.8|-0.0
6|262|Super 6|New Jersey Jets|17|9|6|1|0|1|197|10.9|0.0
7|216|Frozen 4|Jersey Hitmen|19|8|8|1|1|1|410|9.9|0.0
8|186|Frozen 4|Esmark Stars|13|4|7|1|0|1|380|5.9|0.0
9|182|Frozen 4|Team Maryland|21|9|7|1|3|1|202|10.9|0.0
10|169|Frozen 4|Westchester Express Nolan|15|4|9|0|0|2|520|5.7|0.0
11|113||CT Jr. Rangers Elite|17|4|9|1|2|1|456|5.9|0.0
12|31||Westchester Express Thornton|16|1|12|0|2|1|519|1.9|0.0
13|27||Mercer Chiefs Elite|17|2|14|0|0|1|241|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PAL Jr. Islanders|Mercer Chiefs Premier|NY Aviators|Revolution Elite|Philadelphia Flyers Elite|New Jersey Jets|Jersey Hitmen|Esmark Stars|Team Maryland|Westchester Express Nolan|CT Jr. Rangers Elite|Westchester Express Thornton|Mercer Chiefs Elite
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|PAL Jr. Islanders|--| 79%| 80%| 81%| 82%| 83%| 86%| 88%| 88%| 89%| 92%| 98%| 98%
|Mercer Chiefs Premier| 21%|--| 51%| 53%| 54%| 56%| 61%| 65%| 65%| 67%| 75%| 92%| 93%
|NY Aviators| 20%| 49%|--| 53%| 53%| 56%| 60%| 64%| 64%| 66%| 74%| 91%| 92%
|Revolution Elite| 19%| 47%| 47%|--| 50%| 53%| 58%| 61%| 62%| 64%| 72%| 90%| 92%
|Philadelphia Flyers Elite| 18%| 46%| 47%| 50%|--| 53%| 58%| 61%| 62%| 63%| 72%| 90%| 91%
|New Jersey Jets| 17%| 44%| 44%| 47%| 47%|--| 55%| 59%| 59%| 61%| 70%| 89%| 91%
|Jersey Hitmen| 14%| 39%| 40%| 42%| 42%| 45%|--| 54%| 54%| 56%| 66%| 87%| 89%
|Esmark Stars| 12%| 35%| 36%| 39%| 39%| 41%| 46%|--| 51%| 52%| 62%| 86%| 87%
|Team Maryland| 12%| 35%| 36%| 38%| 38%| 41%| 46%| 49%|--| 52%| 62%| 85%| 87%
|Westchester Express Nolan| 11%| 33%| 34%| 36%| 37%| 39%| 44%| 48%| 48%|--| 60%| 84%| 86%
|CT Jr. Rangers Elite|  8%| 25%| 26%| 28%| 28%| 30%| 34%| 38%| 38%| 40%|--| 78%| 81%
|Westchester Express Thornton|  2%|  8%|  9%| 10%| 10%| 11%| 13%| 14%| 15%| 16%| 22%|--| 54%
|Mercer Chiefs Elite|  2%|  7%|  8%|  8%|  9%|  9%| 11%| 13%| 13%| 14%| 19%| 46%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-03 |
| End Date | 2023-02-19 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

