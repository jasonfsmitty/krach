[<- back to the index](readme.md)
# 19U KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2461|Playoffs|York Lady Devils|28|25|1|0|1|1|320|25.8|-0.0
2|1172|Playoffs|Rockets Hockey Club Black|25|16|5|2|1|1|763|18.8|-0.0
3|761|Playoffs|NY Islanders-Islanders Iceworks|18|13|4|0|0|1|742|13.9|0.0
4|471|Playoffs|MCU|12|5|5|1|0|1|932|6.9|0.0
5|441|Playoffs|Lehigh Valley Phantoms|29|18|9|0|1|1|746|18.9|0.0
6|197|Playoffs|Lady Bulldogs|15|6|7|0|0|2|500|7.7|0.0
7|68||Philadelphia Hockey Club Belles|29|5|19|3|1|1|783|8.9|0.0
8|59||Princeton Tiger Lilies|28|6|19|0|1|2|759|7.7|0.0
9|47||MYHA|17|3|11|1|0|2|820|5.7|0.0
10|30||Philadelphia Jr Flyers Crawford|17|1|10|1|3|2|687|3.7|0.0
11|6||Rockets Hockey Club White|15|0|14|0|0|1|303|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||York Lady Devils|Rockets Hockey Club Black|NY Islanders-Islanders Iceworks|MCU|Lehigh Valley Phantoms|Lady Bulldogs|Philadelphia Hockey Club Belles|Princeton Tiger Lilies|MYHA|Philadelphia Jr Flyers Crawford|Rockets Hockey Club White
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|York Lady Devils|--| 68%| 76%| 84%| 85%| 93%| 97%| 98%| 98%| 99%|100%
|Rockets Hockey Club Black| 32%|--| 61%| 71%| 73%| 86%| 95%| 95%| 96%| 97%| 99%
|NY Islanders-Islanders Iceworks| 24%| 39%|--| 62%| 63%| 79%| 92%| 93%| 94%| 96%| 99%
|MCU| 16%| 29%| 38%|--| 52%| 70%| 87%| 89%| 91%| 94%| 99%
|Lehigh Valley Phantoms| 15%| 27%| 37%| 48%|--| 69%| 87%| 88%| 90%| 94%| 99%
|Lady Bulldogs|  7%| 14%| 21%| 30%| 31%|--| 74%| 77%| 81%| 87%| 97%
|Philadelphia Hockey Club Belles|  3%|  5%|  8%| 13%| 13%| 26%|--| 54%| 59%| 69%| 92%
|Princeton Tiger Lilies|  2%|  5%|  7%| 11%| 12%| 23%| 46%|--| 56%| 66%| 90%
|MYHA|  2%|  4%|  6%|  9%| 10%| 19%| 41%| 44%|--| 61%| 88%
|Philadelphia Jr Flyers Crawford|  1%|  3%|  4%|  6%|  6%| 13%| 31%| 34%| 39%|--| 83%
|Rockets Hockey Club White|  0%|  1%|  1%|  1%|  1%|  3%|  8%| 10%| 12%| 17%|--

## Generation Details

Generated with command line:
```
./aghf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-09-10 |
| End Date | 2023-02-12 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

