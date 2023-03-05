[<- back to the index](readme.md)
# 15U Pure 07 KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1114|Super 6|Esmark Stars|13|8|4|0|0|1|726|8.8|-0.0
2|811|Super 6|Rockets Hockey Club Elite|21|16|3|0|1|1|278|16.9|0.0
3|688|Super 6|Revolution Elite|17|10|4|1|1|1|391|11.9|0.0
4|606|Super 6|Team Maryland|21|9|9|1|1|1|759|10.8|-0.0
5|533|Super 6|Jersey Hitmen|23|10|8|3|1|1|527|13.8|-0.0
6|501|Super 6|New Jersey Jets|20|13|5|0|1|1|325|13.9|0.0
7|434|Frozen 4|Mercer Chiefs|21|8|11|0|1|1|845|8.8|-0.0
8|269|Frozen 4|Westchester Express|17|5|10|1|0|1|587|6.8|-0.0
9|246|Frozen 4|PAL Jr. Islanders|20|8|10|0|1|1|594|8.8|-0.0
10|222|Frozen 4|NY Aviators|21|12|6|1|1|1|225|13.9|0.0
11|118||Woodbridge Wolfpack|21|7|9|3|1|1|214|10.9|0.0
12|62||Atlantic Coast Academy|22|7|11|0|3|1|282|7.9|0.0
13|23||CT Jr. Rangers|20|1|17|1|0|1|326|2.9|0.0
14|17||Utica Jr. Comets|24|1|21|1|0|1|308|2.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Esmark Stars|Rockets Hockey Club Elite|Revolution Elite|Team Maryland|Jersey Hitmen|New Jersey Jets|Mercer Chiefs|Westchester Express|PAL Jr. Islanders|NY Aviators|Woodbridge Wolfpack|Atlantic Coast Academy|CT Jr. Rangers|Utica Jr. Comets
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Esmark Stars|--| 58%| 62%| 65%| 68%| 69%| 72%| 81%| 82%| 83%| 90%| 95%| 98%| 99%
|Rockets Hockey Club Elite| 42%|--| 54%| 57%| 60%| 62%| 65%| 75%| 77%| 79%| 87%| 93%| 97%| 98%
|Revolution Elite| 38%| 46%|--| 53%| 56%| 58%| 61%| 72%| 74%| 76%| 85%| 92%| 97%| 98%
|Team Maryland| 35%| 43%| 47%|--| 53%| 55%| 58%| 69%| 71%| 73%| 84%| 91%| 96%| 97%
|Jersey Hitmen| 32%| 40%| 44%| 47%|--| 52%| 55%| 66%| 68%| 71%| 82%| 90%| 96%| 97%
|New Jersey Jets| 31%| 38%| 42%| 45%| 48%|--| 54%| 65%| 67%| 69%| 81%| 89%| 96%| 97%
|Mercer Chiefs| 28%| 35%| 39%| 42%| 45%| 46%|--| 62%| 64%| 66%| 79%| 88%| 95%| 96%
|Westchester Express| 19%| 25%| 28%| 31%| 34%| 35%| 38%|--| 52%| 55%| 70%| 81%| 92%| 94%
|PAL Jr. Islanders| 18%| 23%| 26%| 29%| 32%| 33%| 36%| 48%|--| 53%| 68%| 80%| 92%| 94%
|NY Aviators| 17%| 21%| 24%| 27%| 29%| 31%| 34%| 45%| 47%|--| 65%| 78%| 91%| 93%
|Woodbridge Wolfpack| 10%| 13%| 15%| 16%| 18%| 19%| 21%| 30%| 32%| 35%|--| 66%| 84%| 88%
|Atlantic Coast Academy|  5%|  7%|  8%|  9%| 10%| 11%| 12%| 19%| 20%| 22%| 34%|--| 73%| 79%
|CT Jr. Rangers|  2%|  3%|  3%|  4%|  4%|  4%|  5%|  8%|  8%|  9%| 16%| 27%|--| 58%
|Utica Jr. Comets|  1%|  2%|  2%|  3%|  3%|  3%|  4%|  6%|  6%|  7%| 12%| 21%| 42%|--

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

