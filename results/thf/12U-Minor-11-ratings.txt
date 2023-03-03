[<- back to the index](readme.md)
# 12U Minor 11 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3167|Super 6|Mercer Chiefs|30|24|4|1|0|1|693|25.8|-0.0
2|1828|Super 6|Woodbridge Wolfpack|29|17|5|4|2|1|916|21.8|-0.0
3|1515|Super 6|MCU Elite|13|6|5|1|0|1|1664|7.8|-0.0
4|681|Super 6|PAL Jr. Islanders|23|13|7|2|0|1|633|15.9|0.0
5|629|Super 6|Utica Jr. Comets|17|9|5|1|1|1|781|10.9|0.0
6|506|Super 6|CT Jr. Rangers Elite|30|15|12|0|2|1|965|15.8|-0.0
7|404|Frozen 4|Jersey Hitmen|28|12|9|3|3|1|705|15.9|0.0
8|385|Frozen 4|New Jersey Jets|27|17|5|2|2|1|227|19.9|0.0
9|205|Frozen 4|CP Dynamo|29|8|17|1|2|1|1052|9.8|-0.0
10|162|Frozen 4|Esmark Stars|19|6|9|1|2|1|1069|7.9|0.0
11|114||NY Aviators|29|16|11|0|1|1|232|16.9|0.0
12|110||Team Maryland|29|7|16|4|1|1|480|11.9|0.0
13|41||Westchester Express|27|7|16|0|3|1|398|7.9|0.0
14|6||Revolution Elite|27|2|23|0|1|1|177|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Mercer Chiefs|Woodbridge Wolfpack|MCU Elite|PAL Jr. Islanders|Utica Jr. Comets|CT Jr. Rangers Elite|Jersey Hitmen|New Jersey Jets|CP Dynamo|Esmark Stars|NY Aviators|Team Maryland|Westchester Express|Revolution Elite
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Mercer Chiefs|--| 63%| 68%| 82%| 83%| 86%| 89%| 89%| 94%| 95%| 97%| 97%| 99%|100%
|Woodbridge Wolfpack| 37%|--| 55%| 73%| 74%| 78%| 82%| 83%| 90%| 92%| 94%| 94%| 98%|100%
|MCU Elite| 32%| 45%|--| 69%| 71%| 75%| 79%| 80%| 88%| 90%| 93%| 93%| 97%|100%
|PAL Jr. Islanders| 18%| 27%| 31%|--| 52%| 57%| 63%| 64%| 77%| 81%| 86%| 86%| 94%| 99%
|Utica Jr. Comets| 17%| 26%| 29%| 48%|--| 55%| 61%| 62%| 75%| 79%| 85%| 85%| 94%| 99%
|CT Jr. Rangers Elite| 14%| 22%| 25%| 43%| 45%|--| 56%| 57%| 71%| 76%| 82%| 82%| 93%| 99%
|Jersey Hitmen| 11%| 18%| 21%| 37%| 39%| 44%|--| 51%| 66%| 71%| 78%| 79%| 91%| 99%
|New Jersey Jets| 11%| 17%| 20%| 36%| 38%| 43%| 49%|--| 65%| 70%| 77%| 78%| 90%| 98%
|CP Dynamo|  6%| 10%| 12%| 23%| 25%| 29%| 34%| 35%|--| 56%| 64%| 65%| 83%| 97%
|Esmark Stars|  5%|  8%| 10%| 19%| 21%| 24%| 29%| 30%| 44%|--| 59%| 60%| 80%| 96%
|NY Aviators|  3%|  6%|  7%| 14%| 15%| 18%| 22%| 23%| 36%| 41%|--| 51%| 74%| 95%
|Team Maryland|  3%|  6%|  7%| 14%| 15%| 18%| 21%| 22%| 35%| 40%| 49%|--| 73%| 95%
|Westchester Express|  1%|  2%|  3%|  6%|  6%|  7%|  9%| 10%| 17%| 20%| 26%| 27%|--| 87%
|Revolution Elite|  0%|  0%|  0%|  1%|  1%|  1%|  1%|  2%|  3%|  4%|  5%|  5%| 13%|--

## Generation Details

Generated with command line:
```
./thf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
| End Date | 2023-02-25 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

