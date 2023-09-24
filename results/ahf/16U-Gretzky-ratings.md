[<- back to the index](readme.md)
# 16U Gretzky KRACH Rankings
Rankings generated on Sun Sep 24 18:45:42 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2010|Championship|Dix Hills Hawks 16U|6|6|0|0|0|0|268|6.8|-0.0
2|1223|Championship|STJ 16U Gold|6|4|1|0|0|1|638|5.7|0.0
3|993|Championship|Aviator Hockey Club 16U Minor|5|4|1|0|0|0|459|4.9|0.0
4|939|Championship|VFC 16A Frederick|9|6|2|0|0|1|581|7.7|-0.0
5|780|Gold|Team Philadelphia Black|7|5|2|0|0|0|469|5.9|0.0
6|746|Gold|Palmyra Black Knights|10|5|3|0|0|2|654|7.6|0.0
7|605|Gold|MYHA 16U UA|8|4|4|0|0|0|712|4.9|0.0
8|540|Gold|Frederick Freeze 16U UA|7|5|2|0|0|0|336|5.9|0.0
9|313|Silver|Grundy Senators|11|6|4|0|0|1|301|7.7|0.0
10|276|Silver|Tri-City Eagles 16U White|10|3|4|0|0|3|427|6.4|0.0
11|160|Silver|Haverford Hawks 16U A Black|10|2|6|0|0|2|527|4.6|0.0
12|140|Silver|Wildcats 16U A Black|6|1|4|0|0|1|660|2.7|0.0
13|114||JR Black Bears16U Red|6|1|5|0|0|0|455|1.9|0.0
14|91||Igloo Jaguars 16UA Black|10|0|8|0|0|2|854|2.5|-0.0
15|87||Mercer Chiefs|7|1|6|0|0|0|530|1.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Dix Hills Hawks 16U|STJ 16U Gold|Aviator Hockey Club 16U Minor|VFC 16A Frederick|Team Philadelphia Black|Palmyra Black Knights|MYHA 16U UA|Frederick Freeze 16U UA|Grundy Senators|Tri-City Eagles 16U White|Haverford Hawks 16U A Black|Wildcats 16U A Black|JR Black Bears16U Red|Igloo Jaguars 16UA Black|Mercer Chiefs
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Dix Hills Hawks 16U|--| 62%| 67%| 68%| 72%| 73%| 77%| 79%| 87%| 88%| 93%| 93%| 95%| 96%| 96%
|STJ 16U Gold| 38%|--| 55%| 57%| 61%| 62%| 67%| 69%| 80%| 82%| 88%| 90%| 91%| 93%| 93%
|Aviator Hockey Club 16U Minor| 33%| 45%|--| 51%| 56%| 57%| 62%| 65%| 76%| 78%| 86%| 88%| 90%| 92%| 92%
|VFC 16A Frederick| 32%| 43%| 49%|--| 55%| 56%| 61%| 63%| 75%| 77%| 85%| 87%| 89%| 91%| 91%
|Team Philadelphia Black| 28%| 39%| 44%| 45%|--| 51%| 56%| 59%| 71%| 74%| 83%| 85%| 87%| 90%| 90%
|Palmyra Black Knights| 27%| 38%| 43%| 44%| 49%|--| 55%| 58%| 70%| 73%| 82%| 84%| 87%| 89%| 90%
|MYHA 16U UA| 23%| 33%| 38%| 39%| 44%| 45%|--| 53%| 66%| 69%| 79%| 81%| 84%| 87%| 87%
|Frederick Freeze 16U UA| 21%| 31%| 35%| 37%| 41%| 42%| 47%|--| 63%| 66%| 77%| 79%| 83%| 86%| 86%
|Grundy Senators| 13%| 20%| 24%| 25%| 29%| 30%| 34%| 37%|--| 53%| 66%| 69%| 73%| 78%| 78%
|Tri-City Eagles 16U White| 12%| 18%| 22%| 23%| 26%| 27%| 31%| 34%| 47%|--| 63%| 66%| 71%| 75%| 76%
|Haverford Hawks 16U A Black|  7%| 12%| 14%| 15%| 17%| 18%| 21%| 23%| 34%| 37%|--| 53%| 58%| 64%| 65%
|Wildcats 16U A Black|  7%| 10%| 12%| 13%| 15%| 16%| 19%| 21%| 31%| 34%| 47%|--| 55%| 61%| 62%
|JR Black Bears16U Red|  5%|  9%| 10%| 11%| 13%| 13%| 16%| 17%| 27%| 29%| 42%| 45%|--| 56%| 57%
|Igloo Jaguars 16UA Black|  4%|  7%|  8%|  9%| 10%| 11%| 13%| 14%| 22%| 25%| 36%| 39%| 44%|--| 51%
|Mercer Chiefs|  4%|  7%|  8%|  9%| 10%| 10%| 13%| 14%| 22%| 24%| 35%| 38%| 43%| 49%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-08-26 |
| End Date | 2023-09-24 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

