[<- back to the index](readme.md)
# 12U Major 10 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2244|Super 6|Rockets Hockey Club|17|11|3|1|1|1|1060|12.8|-0.0
2|774|Super 6|Revolution Elite|31|16|9|3|2|1|742|19.8|-0.0
3|612|Super 6|Woodbridge Wolfpack|30|16|9|3|1|1|494|19.8|-0.0
4|587|Super 6|CP Dynamo|17|8|7|1|0|1|646|9.8|-0.0
5|585|Super 6|CT Jr. Rangers|28|14|9|2|2|1|655|16.8|-0.0
6|476|Super 6|Esmark Stars|17|9|4|2|1|1|302|11.8|-0.0
7|455|Frozen 4|Jersey Hitmen|31|15|7|5|3|1|308|20.9|0.0
8|441|Frozen 4|Hartford Jr. Wolfpack|17|11|2|3|0|1|87|14.9|0.0
9|262|Frozen 4|Team Maryland|30|12|13|0|4|1|563|12.8|-0.0
10|201|Frozen 4|Utica Jr. Comets|17|5|9|1|1|1|419|6.8|-0.0
11|158||NY Aviators|28|13|11|1|2|1|237|14.9|0.0
12|116||PAL Jr. Islanders|26|9|14|1|1|1|310|10.9|0.0
13|46||Westchester Express|30|6|18|0|3|3|235|8.6|0.0
14|46||Philadelphia Flyers Elite|31|5|21|0|2|3|342|7.6|0.0
15|39||Mercer Chiefs|29|3|21|1|1|3|297|6.6|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Rockets Hockey Club|Revolution Elite|Woodbridge Wolfpack|CP Dynamo|CT Jr. Rangers|Esmark Stars|Jersey Hitmen|Hartford Jr. Wolfpack|Team Maryland|Utica Jr. Comets|NY Aviators|PAL Jr. Islanders|Westchester Express|Philadelphia Flyers Elite|Mercer Chiefs
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Rockets Hockey Club|--| 74%| 79%| 79%| 79%| 83%| 83%| 84%| 90%| 92%| 93%| 95%| 98%| 98%| 98%
|Revolution Elite| 26%|--| 56%| 57%| 57%| 62%| 63%| 64%| 75%| 79%| 83%| 87%| 94%| 94%| 95%
|Woodbridge Wolfpack| 21%| 44%|--| 51%| 51%| 56%| 57%| 58%| 70%| 75%| 79%| 84%| 93%| 93%| 94%
|CP Dynamo| 21%| 43%| 49%|--| 50%| 55%| 56%| 57%| 69%| 75%| 79%| 84%| 93%| 93%| 94%
|CT Jr. Rangers| 21%| 43%| 49%| 50%|--| 55%| 56%| 57%| 69%| 74%| 79%| 84%| 93%| 93%| 94%
|Esmark Stars| 17%| 38%| 44%| 45%| 45%|--| 51%| 52%| 64%| 70%| 75%| 80%| 91%| 91%| 92%
|Jersey Hitmen| 17%| 37%| 43%| 44%| 44%| 49%|--| 51%| 63%| 69%| 74%| 80%| 91%| 91%| 92%
|Hartford Jr. Wolfpack| 16%| 36%| 42%| 43%| 43%| 48%| 49%|--| 63%| 69%| 74%| 79%| 91%| 91%| 92%
|Team Maryland| 10%| 25%| 30%| 31%| 31%| 36%| 37%| 37%|--| 57%| 62%| 69%| 85%| 85%| 87%
|Utica Jr. Comets|  8%| 21%| 25%| 25%| 26%| 30%| 31%| 31%| 43%|--| 56%| 63%| 81%| 81%| 84%
|NY Aviators|  7%| 17%| 21%| 21%| 21%| 25%| 26%| 26%| 38%| 44%|--| 58%| 77%| 78%| 80%
|PAL Jr. Islanders|  5%| 13%| 16%| 16%| 16%| 20%| 20%| 21%| 31%| 37%| 42%|--| 71%| 72%| 75%
|Westchester Express|  2%|  6%|  7%|  7%|  7%|  9%|  9%|  9%| 15%| 19%| 23%| 29%|--| 50%| 54%
|Philadelphia Flyers Elite|  2%|  6%|  7%|  7%|  7%|  9%|  9%|  9%| 15%| 19%| 22%| 28%| 50%|--| 54%
|Mercer Chiefs|  2%|  5%|  6%|  6%|  6%|  8%|  8%|  8%| 13%| 16%| 20%| 25%| 46%| 46%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
| End Date | 2023-02-11 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

