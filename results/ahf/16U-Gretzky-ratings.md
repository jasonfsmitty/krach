[<- back to the index](readme.md)
# 16U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1892|Championship|Dix Hills Hawks 16U|5|4|0|0|0|1|358|4.8|-0.0
2|1573|Championship|STJ 16U Gold|5|3|0|0|0|2|624|4.7|0.0
3|982|Championship|Aviator Hockey Club 16U Minor|5|3|1|0|0|1|603|3.9|0.0
4|903|Championship|VFC 16A Frederick|7|4|2|0|0|1|660|4.8|-0.0
5|893|Gold|Team Philadelphia Black|5|3|1|0|0|1|574|3.9|0.0
6|693|Gold|Palmyra Black Knights|6|3|1|0|0|2|488|4.7|0.0
7|597|Gold|MYHA 16U UA|7|3|3|0|0|1|704|3.9|0.0
8|557|Gold|Frederick Freeze 16U UA|5|3|1|0|0|1|332|3.9|0.0
9|391|Silver|Tri-City Eagles 16U White|7|3|2|0|0|2|355|4.7|0.0
10|288|Silver|Haverford Hawks 16U A Black|8|2|3|0|0|3|590|4.6|0.0
11|192|Silver|JR Black Bears16U Red|5|1|3|0|0|1|528|1.9|0.0
12|159|Silver|Grundy Senators|7|2|4|0|0|1|404|2.9|0.0
13|158||Mercer Chiefs|6|1|4|0|0|1|607|1.9|0.0
14|112||Wildcats 16U A Black|5|0|4|0|0|1|886|0.9|0.0
15|87||Igloo Jaguars 16UA Black|7|0|5|0|0|2|592|1.7|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Dix Hills Hawks 16U|STJ 16U Gold|Aviator Hockey Club 16U Minor|VFC 16A Frederick|Team Philadelphia Black|Palmyra Black Knights|MYHA 16U UA|Frederick Freeze 16U UA|Tri-City Eagles 16U White|Haverford Hawks 16U A Black|JR Black Bears16U Red|Grundy Senators|Mercer Chiefs|Wildcats 16U A Black|Igloo Jaguars 16UA Black
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Dix Hills Hawks 16U|--| 55%| 66%| 68%| 68%| 73%| 76%| 77%| 83%| 87%| 91%| 92%| 92%| 94%| 96%
|STJ 16U Gold| 45%|--| 62%| 64%| 64%| 69%| 72%| 74%| 80%| 85%| 89%| 91%| 91%| 93%| 95%
|Aviator Hockey Club 16U Minor| 34%| 38%|--| 52%| 52%| 59%| 62%| 64%| 71%| 77%| 84%| 86%| 86%| 90%| 92%
|VFC 16A Frederick| 32%| 36%| 48%|--| 50%| 57%| 60%| 62%| 70%| 76%| 83%| 85%| 85%| 89%| 91%
|Team Philadelphia Black| 32%| 36%| 48%| 50%|--| 56%| 60%| 62%| 70%| 76%| 82%| 85%| 85%| 89%| 91%
|Palmyra Black Knights| 27%| 31%| 41%| 43%| 44%|--| 54%| 55%| 64%| 71%| 78%| 81%| 81%| 86%| 89%
|MYHA 16U UA| 24%| 28%| 38%| 40%| 40%| 46%|--| 52%| 60%| 67%| 76%| 79%| 79%| 84%| 87%
|Frederick Freeze 16U UA| 23%| 26%| 36%| 38%| 38%| 45%| 48%|--| 59%| 66%| 74%| 78%| 78%| 83%| 86%
|Tri-City Eagles 16U White| 17%| 20%| 29%| 30%| 30%| 36%| 40%| 41%|--| 58%| 67%| 71%| 71%| 78%| 82%
|Haverford Hawks 16U A Black| 13%| 15%| 23%| 24%| 24%| 29%| 33%| 34%| 42%|--| 60%| 64%| 65%| 72%| 77%
|JR Black Bears16U Red|  9%| 11%| 16%| 17%| 18%| 22%| 24%| 26%| 33%| 40%|--| 55%| 55%| 63%| 69%
|Grundy Senators|  8%|  9%| 14%| 15%| 15%| 19%| 21%| 22%| 29%| 36%| 45%|--| 50%| 59%| 65%
|Mercer Chiefs|  8%|  9%| 14%| 15%| 15%| 19%| 21%| 22%| 29%| 35%| 45%| 50%|--| 58%| 64%
|Wildcats 16U A Black|  6%|  7%| 10%| 11%| 11%| 14%| 16%| 17%| 22%| 28%| 37%| 41%| 42%|--| 56%
|Igloo Jaguars 16UA Black|  4%|  5%|  8%|  9%|  9%| 11%| 13%| 14%| 18%| 23%| 31%| 35%| 36%| 44%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-08-26 |
| End Date | 2023-09-10 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

