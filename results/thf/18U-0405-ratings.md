[<- back to the index](readme.md)
# 18U 04/05 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2606|Super 6|Esmark Stars|13|10|2|0|0|1|740|10.8|-0.0
2|891|Super 6|Mercer Chiefs Premier|23|11|6|2|3|1|916|13.8|-0.0
3|862|Super 6|PAL Jr. Islanders|21|14|5|0|1|1|455|14.8|-0.0
4|807|Super 6|Jersey Hitmen|19|11|5|1|1|1|539|12.8|-0.0
5|548|Super 6|NY Aviators|19|13|3|1|1|1|208|14.9|0.0
6|541|Super 6|Team Maryland|13|5|7|0|0|1|1235|5.8|-0.0
7|353|Frozen 4|Westchester Express|18|4|10|3|0|1|598|7.8|-0.0
8|318|Frozen 4|Philadelphia Flyers Elite|21|8|12|0|0|1|705|8.8|-0.0
9|299|Frozen 4|NJ 87s|19|7|8|2|1|1|390|9.9|0.0
10|275|Frozen 4|Philadelphia Flyers Elite Prep|17|9|7|0|0|1|295|9.9|0.0
11|265||Skipjacks Hockey Academy|17|7|8|0|1|1|433|7.8|-0.0
12|159||Rockets Hockey Club Elite|20|7|10|0|2|1|414|7.9|0.0
13|78||Mercer Chiefs Elite|17|4|12|0|0|1|352|4.9|0.0
14|48||Utica Jr. Comets|19|2|15|1|0|1|273|3.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Esmark Stars|Mercer Chiefs Premier|PAL Jr. Islanders|Jersey Hitmen|NY Aviators|Team Maryland|Westchester Express|Philadelphia Flyers Elite|NJ 87s|Philadelphia Flyers Elite Prep|Skipjacks Hockey Academy|Rockets Hockey Club Elite|Mercer Chiefs Elite|Utica Jr. Comets
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Esmark Stars|--| 75%| 75%| 76%| 83%| 83%| 88%| 89%| 90%| 90%| 91%| 94%| 97%| 98%
|Mercer Chiefs Premier| 25%|--| 51%| 52%| 62%| 62%| 72%| 74%| 75%| 76%| 77%| 85%| 92%| 95%
|PAL Jr. Islanders| 25%| 49%|--| 52%| 61%| 61%| 71%| 73%| 74%| 76%| 77%| 84%| 92%| 95%
|Jersey Hitmen| 24%| 48%| 48%|--| 60%| 60%| 70%| 72%| 73%| 75%| 75%| 84%| 91%| 94%
|NY Aviators| 17%| 38%| 39%| 40%|--| 50%| 61%| 63%| 65%| 67%| 67%| 77%| 88%| 92%
|Team Maryland| 17%| 38%| 39%| 40%| 50%|--| 61%| 63%| 64%| 66%| 67%| 77%| 87%| 92%
|Westchester Express| 12%| 28%| 29%| 30%| 39%| 39%|--| 53%| 54%| 56%| 57%| 69%| 82%| 88%
|Philadelphia Flyers Elite| 11%| 26%| 27%| 28%| 37%| 37%| 47%|--| 51%| 54%| 55%| 67%| 80%| 87%
|NJ 87s| 10%| 25%| 26%| 27%| 35%| 36%| 46%| 49%|--| 52%| 53%| 65%| 79%| 86%
|Philadelphia Flyers Elite Prep| 10%| 24%| 24%| 25%| 33%| 34%| 44%| 46%| 48%|--| 51%| 63%| 78%| 85%
|Skipjacks Hockey Academy|  9%| 23%| 23%| 25%| 33%| 33%| 43%| 45%| 47%| 49%|--| 62%| 77%| 85%
|Rockets Hockey Club Elite|  6%| 15%| 16%| 16%| 23%| 23%| 31%| 33%| 35%| 37%| 38%|--| 67%| 77%
|Mercer Chiefs Elite|  3%|  8%|  8%|  9%| 12%| 13%| 18%| 20%| 21%| 22%| 23%| 33%|--| 62%
|Utica Jr. Comets|  2%|  5%|  5%|  6%|  8%|  8%| 12%| 13%| 14%| 15%| 15%| 23%| 38%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-26 |
| End Date | 2023-02-19 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

