[<- back to the index](readme.md)
# 14U Minor 09 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3699|Super 6|PAL Jr. Islanders|23|17|3|2|0|1|755|19.8|-0.0
2|1093|Super 6|Rockets Hockey Club|25|15|7|1|1|1|986|16.8|-0.0
3|1000|Super 6|CT Jr. Rangers Elite|23|12|8|1|1|1|1140|13.8|-0.0
4|983|Super 6|CP Dynamo|17|8|7|1|0|1|1368|9.8|-0.0
5|734|Super 6|Hartford Jr. Wolfpack Elite|17|14|1|1|0|1|85|15.9|0.0
6|613|Super 6|Westchester Express|17|7|7|1|1|1|1302|8.8|-0.0
7|528|Frozen 4|Team Maryland|17|6|7|2|1|1|991|8.8|-0.0
8|184|Frozen 4|NY Aviators|29|16|9|1|2|1|262|17.9|0.0
9|152|Frozen 4|Esmark Stars|17|5|9|0|2|1|498|5.8|-0.0
10|125|Frozen 4|Revolution Elite|25|11|11|1|1|1|288|12.9|0.0
11|108||Mercer Chiefs|27|10|13|2|1|1|313|12.9|0.0
12|76||Utica Jr. Comets|19|7|8|1|2|1|266|8.9|0.0
13|59||Woodbridge Wolfpack|29|11|16|1|0|1|180|12.9|0.0
14|23||Jersey Hitmen|29|5|19|2|2|1|180|7.9|0.0
15|3||Hartford Jr. Wolfpack Red|17|0|16|0|0|1|90|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||PAL Jr. Islanders|Rockets Hockey Club|CT Jr. Rangers Elite|CP Dynamo|Hartford Jr. Wolfpack Elite|Westchester Express|Team Maryland|NY Aviators|Esmark Stars|Revolution Elite|Mercer Chiefs|Utica Jr. Comets|Woodbridge Wolfpack|Jersey Hitmen|Hartford Jr. Wolfpack Red
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|PAL Jr. Islanders|--| 77%| 79%| 79%| 83%| 86%| 88%| 95%| 96%| 97%| 97%| 98%| 98%| 99%|100%
|Rockets Hockey Club| 23%|--| 52%| 53%| 60%| 64%| 67%| 86%| 88%| 90%| 91%| 93%| 95%| 98%|100%
|CT Jr. Rangers Elite| 21%| 48%|--| 50%| 58%| 62%| 65%| 84%| 87%| 89%| 90%| 93%| 94%| 98%|100%
|CP Dynamo| 21%| 47%| 50%|--| 57%| 62%| 65%| 84%| 87%| 89%| 90%| 93%| 94%| 98%|100%
|Hartford Jr. Wolfpack Elite| 17%| 40%| 42%| 43%|--| 55%| 58%| 80%| 83%| 85%| 87%| 91%| 93%| 97%|100%
|Westchester Express| 14%| 36%| 38%| 38%| 45%|--| 54%| 77%| 80%| 83%| 85%| 89%| 91%| 96%|100%
|Team Maryland| 12%| 33%| 35%| 35%| 42%| 46%|--| 74%| 78%| 81%| 83%| 87%| 90%| 96%| 99%
|NY Aviators|  5%| 14%| 16%| 16%| 20%| 23%| 26%|--| 55%| 60%| 63%| 71%| 76%| 89%| 98%
|Esmark Stars|  4%| 12%| 13%| 13%| 17%| 20%| 22%| 45%|--| 55%| 58%| 67%| 72%| 87%| 98%
|Revolution Elite|  3%| 10%| 11%| 11%| 15%| 17%| 19%| 40%| 45%|--| 54%| 62%| 68%| 85%| 98%
|Mercer Chiefs|  3%|  9%| 10%| 10%| 13%| 15%| 17%| 37%| 42%| 46%|--| 59%| 65%| 83%| 97%
|Utica Jr. Comets|  2%|  7%|  7%|  7%|  9%| 11%| 13%| 29%| 33%| 38%| 41%|--| 57%| 77%| 96%
|Woodbridge Wolfpack|  2%|  5%|  6%|  6%|  7%|  9%| 10%| 24%| 28%| 32%| 35%| 43%|--| 72%| 95%
|Jersey Hitmen|  1%|  2%|  2%|  2%|  3%|  4%|  4%| 11%| 13%| 15%| 17%| 23%| 28%|--| 89%
|Hartford Jr. Wolfpack Red|  0%|  0%|  0%|  0%|  0%|  0%|  1%|  2%|  2%|  2%|  3%|  4%|  5%| 11%|--

## Generation Details

Generated with command line:
```
./thf.py update
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

