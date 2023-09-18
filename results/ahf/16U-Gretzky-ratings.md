[<- back to the index](readme.md)
# 16U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1867|Championship|Dix Hills Hawks 16U|7|6|0|0|0|1|244|6.8|-0.0
2|1251|Championship|STJ 16U Gold|7|4|1|0|0|2|649|5.7|0.0
3|998|Championship|Aviator Hockey Club 16U Minor|6|4|1|0|0|1|459|4.9|0.0
4|835|Championship|Team Philadelphia Black|6|4|1|0|0|1|415|4.9|0.0
5|814|Gold|VFC 16A Frederick|9|5|2|0|0|2|577|6.7|-0.0
6|741|Gold|Frederick Freeze 16U UA|7|5|1|0|0|1|265|5.9|0.0
7|732|Gold|Palmyra Black Knights|9|4|2|0|0|3|630|6.6|0.0
8|566|Gold|MYHA 16U UA|7|3|3|0|0|1|672|3.9|0.0
9|325|Silver|Tri-City Eagles 16U White|9|3|3|0|0|3|412|5.6|0.0
10|255|Silver|Grundy Senators|10|5|4|0|0|1|307|5.9|0.0
11|168|Silver|Haverford Hawks 16U A Black|11|2|6|0|0|3|558|4.6|0.0
12|135|Silver|Mercer Chiefs|7|1|5|0|0|1|624|1.9|0.0
13|116||Wildcats 16U A Black|5|0|4|0|0|1|910|0.9|0.0
14|104||JR Black Bears16U Red|7|1|5|0|0|1|423|1.9|0.0
15|78||Igloo Jaguars 16UA Black|10|0|8|0|0|2|896|1.7|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Dix Hills Hawks 16U|STJ 16U Gold|Aviator Hockey Club 16U Minor|Team Philadelphia Black|VFC 16A Frederick|Frederick Freeze 16U UA|Palmyra Black Knights|MYHA 16U UA|Tri-City Eagles 16U White|Grundy Senators|Haverford Hawks 16U A Black|Mercer Chiefs|Wildcats 16U A Black|JR Black Bears16U Red|Igloo Jaguars 16UA Black
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Dix Hills Hawks 16U|--| 60%| 65%| 69%| 70%| 72%| 72%| 77%| 85%| 88%| 92%| 93%| 94%| 95%| 96%
|STJ 16U Gold| 40%|--| 56%| 60%| 61%| 63%| 63%| 69%| 79%| 83%| 88%| 90%| 92%| 92%| 94%
|Aviator Hockey Club 16U Minor| 35%| 44%|--| 54%| 55%| 57%| 58%| 64%| 75%| 80%| 86%| 88%| 90%| 91%| 93%
|Team Philadelphia Black| 31%| 40%| 46%|--| 51%| 53%| 53%| 60%| 72%| 77%| 83%| 86%| 88%| 89%| 91%
|VFC 16A Frederick| 30%| 39%| 45%| 49%|--| 52%| 53%| 59%| 71%| 76%| 83%| 86%| 88%| 89%| 91%
|Frederick Freeze 16U UA| 28%| 37%| 43%| 47%| 48%|--| 50%| 57%| 70%| 74%| 82%| 85%| 87%| 88%| 90%
|Palmyra Black Knights| 28%| 37%| 42%| 47%| 47%| 50%|--| 56%| 69%| 74%| 81%| 84%| 86%| 88%| 90%
|MYHA 16U UA| 23%| 31%| 36%| 40%| 41%| 43%| 44%|--| 64%| 69%| 77%| 81%| 83%| 84%| 88%
|Tri-City Eagles 16U White| 15%| 21%| 25%| 28%| 29%| 30%| 31%| 36%|--| 56%| 66%| 71%| 74%| 76%| 81%
|Grundy Senators| 12%| 17%| 20%| 23%| 24%| 26%| 26%| 31%| 44%|--| 60%| 65%| 69%| 71%| 77%
|Haverford Hawks 16U A Black|  8%| 12%| 14%| 17%| 17%| 18%| 19%| 23%| 34%| 40%|--| 55%| 59%| 62%| 68%
|Mercer Chiefs|  7%| 10%| 12%| 14%| 14%| 15%| 16%| 19%| 29%| 35%| 45%|--| 54%| 56%| 63%
|Wildcats 16U A Black|  6%|  8%| 10%| 12%| 12%| 13%| 14%| 17%| 26%| 31%| 41%| 46%|--| 53%| 60%
|JR Black Bears16U Red|  5%|  8%|  9%| 11%| 11%| 12%| 12%| 16%| 24%| 29%| 38%| 44%| 47%|--| 57%
|Igloo Jaguars 16UA Black|  4%|  6%|  7%|  9%|  9%| 10%| 10%| 12%| 19%| 23%| 32%| 37%| 40%| 43%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-08-26 |
| End Date | 2023-09-17 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

