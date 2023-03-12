[<- back to the index](readme.md)
# 16U 06/07 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|922|Super 6|Revolution Elite|20|15|2|2|0|1|190|17.8|-0.0
2|891|Super 6|Jersey Hitmen|21|13|5|2|0|1|759|15.8|-0.0
3|637|Super 6|Esmark Stars|13|7|4|1|0|1|1059|8.8|-0.0
4|580|Super 6|PAL Jr. Islanders|20|12|5|1|1|1|784|13.8|-0.0
5|556|Super 6|Atlantic Coast Academy 16U|19|16|1|1|0|1|56|17.9|0.0
6|187|Super 6|Westchester Express|14|5|5|0|3|1|770|5.8|-0.0
7|145|Frozen 4|Mercer Chiefs Premier|21|8|11|1|0|1|551|9.8|-0.0
8|98|Frozen 4|Skipjacks Hockey Academy|18|9|8|0|0|1|211|9.9|0.0
9|61|Frozen 4|Potomac Patriots|22|8|10|1|2|1|226|9.9|0.0
10|55|Frozen 4|Rockets Hockey Club Elite|20|7|10|1|1|1|276|8.9|0.0
11|49||NY Aviators|21|8|8|2|2|1|145|10.9|0.0
12|47||Team Maryland|15|0|10|1|3|1|1104|1.8|-0.0
13|43||CT Jr. Rangers Premier|19|1|15|1|1|1|517|2.8|-0.0
14|40||New Jersey Jets|20|6|10|1|2|1|239|7.9|0.0
15|17||Mercer Chiefs Elite|22|5|14|1|1|1|77|6.9|0.0
16|3||CT Jr. Rangers Elite|14|0|13|0|0|1|91|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Revolution Elite|Jersey Hitmen|Esmark Stars|PAL Jr. Islanders|Atlantic Coast Academy 16U|Westchester Express|Mercer Chiefs Premier|Skipjacks Hockey Academy|Potomac Patriots|Rockets Hockey Club Elite|NY Aviators|Team Maryland|CT Jr. Rangers Premier|New Jersey Jets|Mercer Chiefs Elite|CT Jr. Rangers Elite
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Revolution Elite|--| 51%| 59%| 61%| 62%| 83%| 86%| 90%| 94%| 94%| 95%| 95%| 96%| 96%| 98%|100%
|Jersey Hitmen| 49%|--| 58%| 61%| 62%| 83%| 86%| 90%| 94%| 94%| 95%| 95%| 95%| 96%| 98%|100%
|Esmark Stars| 41%| 42%|--| 52%| 53%| 77%| 81%| 87%| 91%| 92%| 93%| 93%| 94%| 94%| 97%|100%
|PAL Jr. Islanders| 39%| 39%| 48%|--| 51%| 76%| 80%| 86%| 90%| 91%| 92%| 93%| 93%| 93%| 97%|100%
|Atlantic Coast Academy 16U| 38%| 38%| 47%| 49%|--| 75%| 79%| 85%| 90%| 91%| 92%| 92%| 93%| 93%| 97%|100%
|Westchester Express| 17%| 17%| 23%| 24%| 25%|--| 56%| 66%| 75%| 77%| 79%| 80%| 81%| 82%| 92%| 99%
|Mercer Chiefs Premier| 14%| 14%| 19%| 20%| 21%| 44%|--| 60%| 70%| 73%| 75%| 76%| 77%| 78%| 89%| 98%
|Skipjacks Hockey Academy| 10%| 10%| 13%| 14%| 15%| 34%| 40%|--| 62%| 64%| 67%| 68%| 69%| 71%| 85%| 97%
|Potomac Patriots|  6%|  6%|  9%| 10%| 10%| 25%| 30%| 38%|--| 53%| 56%| 57%| 59%| 60%| 78%| 96%
|Rockets Hockey Club Elite|  6%|  6%|  8%|  9%|  9%| 23%| 27%| 36%| 47%|--| 53%| 54%| 56%| 58%| 76%| 96%
|NY Aviators|  5%|  5%|  7%|  8%|  8%| 21%| 25%| 33%| 44%| 47%|--| 51%| 53%| 55%| 74%| 95%
|Team Maryland|  5%|  5%|  7%|  7%|  8%| 20%| 24%| 32%| 43%| 46%| 49%|--| 52%| 54%| 73%| 95%
|CT Jr. Rangers Premier|  4%|  5%|  6%|  7%|  7%| 19%| 23%| 31%| 41%| 44%| 47%| 48%|--| 52%| 72%| 94%
|New Jersey Jets|  4%|  4%|  6%|  7%|  7%| 18%| 22%| 29%| 40%| 42%| 45%| 46%| 48%|--| 70%| 94%
|Mercer Chiefs Elite|  2%|  2%|  3%|  3%|  3%|  8%| 11%| 15%| 22%| 24%| 26%| 27%| 28%| 30%|--| 87%
|CT Jr. Rangers Elite|  0%|  0%|  0%|  0%|  0%|  1%|  2%|  3%|  4%|  4%|  5%|  5%|  6%|  6%| 13%|--

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

