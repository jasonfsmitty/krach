[<- back to the index](readme.md)
# 10U Minor 13 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3213|Super 6|MCU Elite|13|9|2|1|0|1|1138|10.8|-0.0
2|2752|Super 6|Jersey Hitmen|15|10|2|1|1|1|1256|11.8|-0.0
3|1300|Super 6|Utica Jr. Comets|17|15|0|0|1|1|156|15.9|0.0
4|1163|Super 6|Woodbridge Wolfpack|25|17|4|1|2|1|834|18.8|-0.0
5|322|Super 6|Revolution Elite|29|15|8|2|3|1|345|17.9|0.0
6|250|Super 6|Westchester Express|29|13|12|0|3|1|677|13.9|0.0
7|239|Frozen 4|Rockets Hockey Club|30|14|12|1|2|1|622|15.9|0.0
8|214|Frozen 4|CP Dynamo|29|8|15|5|0|1|571|13.9|0.0
9|91|Frozen 4|NY Aviators|30|10|18|1|0|1|348|11.9|0.0
10|60|Frozen 4|CT Jr. Rangers|28|5|19|3|0|1|605|8.9|0.0
11|44||PAL Jr. Islanders|23|4|13|1|4|1|402|5.9|0.0
12|5||Hartford Jr. Wolfpack|16|0|14|0|1|1|241|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MCU Elite|Jersey Hitmen|Utica Jr. Comets|Woodbridge Wolfpack|Revolution Elite|Westchester Express|Rockets Hockey Club|CP Dynamo|NY Aviators|CT Jr. Rangers|PAL Jr. Islanders|Hartford Jr. Wolfpack
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MCU Elite|--| 54%| 71%| 73%| 91%| 93%| 93%| 94%| 97%| 98%| 99%|100%
|Jersey Hitmen| 46%|--| 68%| 70%| 90%| 92%| 92%| 93%| 97%| 98%| 98%|100%
|Utica Jr. Comets| 29%| 32%|--| 53%| 80%| 84%| 84%| 86%| 93%| 96%| 97%|100%
|Woodbridge Wolfpack| 27%| 30%| 47%|--| 78%| 82%| 83%| 84%| 93%| 95%| 96%|100%
|Revolution Elite|  9%| 10%| 20%| 22%|--| 56%| 57%| 60%| 78%| 84%| 88%| 99%
|Westchester Express|  7%|  8%| 16%| 18%| 44%|--| 51%| 54%| 73%| 81%| 85%| 98%
|Rockets Hockey Club|  7%|  8%| 16%| 17%| 43%| 49%|--| 53%| 72%| 80%| 85%| 98%
|CP Dynamo|  6%|  7%| 14%| 16%| 40%| 46%| 47%|--| 70%| 78%| 83%| 98%
|NY Aviators|  3%|  3%|  7%|  7%| 22%| 27%| 28%| 30%|--| 60%| 68%| 95%
|CT Jr. Rangers|  2%|  2%|  4%|  5%| 16%| 19%| 20%| 22%| 40%|--| 58%| 93%
|PAL Jr. Islanders|  1%|  2%|  3%|  4%| 12%| 15%| 15%| 17%| 32%| 42%|--| 90%
|Hartford Jr. Wolfpack|  0%|  0%|  0%|  0%|  1%|  2%|  2%|  2%|  5%|  7%| 10%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-17 |
| End Date | 2023-02-26 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

