[<- back to the index](readme.md)
# 16U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2073|Championship|Dix Hills Hawks 16U|5|4|0|0|0|1|415|4.8|-0.0
2|1430|Championship|STJ 16U Gold|5|3|0|0|0|2|570|4.7|0.0
3|1214|Championship|VFC 16A Frederick|5|3|1|0|0|1|772|3.8|-0.0
4|912|Championship|Aviator Hockey Club 16U Minor|5|3|1|0|0|1|547|3.9|0.0
5|843|Gold|Team Philadelphia Black|5|3|1|0|0|1|524|3.9|0.0
6|715|Gold|Tri-City Eagles 16U White|5|3|1|0|0|1|435|3.8|-0.0
7|550|Gold|Palmyra Black Knights|5|2|1|0|0|2|499|3.7|0.0
8|473|Gold|MYHA 16U UA|5|2|2|0|0|1|570|2.9|0.0
9|463|Silver|Frederick Freeze 16U UA|4|2|1|0|0|1|452|2.8|-0.0
10|266|Silver|Haverford Hawks 16U A Black|5|1|3|0|0|1|862|1.8|-0.0
11|193|Silver|JR Black Bears16U Red|5|1|3|0|0|1|577|1.9|0.0
12|146|Silver|Grundy Senators|5|1|3|0|0|1|462|1.9|0.0
13|129||Mercer Chiefs|4|0|3|0|0|1|759|0.9|0.0
14|106||Wildcats 16U A Black|5|0|4|0|0|1|869|0.9|0.0
15|70||Igloo Jaguars 16UA Black|5|0|4|0|0|1|730|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Dix Hills Hawks 16U|STJ 16U Gold|VFC 16A Frederick|Aviator Hockey Club 16U Minor|Team Philadelphia Black|Tri-City Eagles 16U White|Palmyra Black Knights|MYHA 16U UA|Frederick Freeze 16U UA|Haverford Hawks 16U A Black|JR Black Bears16U Red|Grundy Senators|Mercer Chiefs|Wildcats 16U A Black|Igloo Jaguars 16UA Black
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Dix Hills Hawks 16U|--| 59%| 63%| 69%| 71%| 74%| 79%| 81%| 82%| 89%| 91%| 93%| 94%| 95%| 97%
|STJ 16U Gold| 41%|--| 54%| 61%| 63%| 67%| 72%| 75%| 76%| 84%| 88%| 91%| 92%| 93%| 95%
|VFC 16A Frederick| 37%| 46%|--| 57%| 59%| 63%| 69%| 72%| 72%| 82%| 86%| 89%| 90%| 92%| 95%
|Aviator Hockey Club 16U Minor| 31%| 39%| 43%|--| 52%| 56%| 62%| 66%| 66%| 77%| 83%| 86%| 88%| 90%| 93%
|Team Philadelphia Black| 29%| 37%| 41%| 48%|--| 54%| 61%| 64%| 65%| 76%| 81%| 85%| 87%| 89%| 92%
|Tri-City Eagles 16U White| 26%| 33%| 37%| 44%| 46%|--| 57%| 60%| 61%| 73%| 79%| 83%| 85%| 87%| 91%
|Palmyra Black Knights| 21%| 28%| 31%| 38%| 39%| 43%|--| 54%| 54%| 67%| 74%| 79%| 81%| 84%| 89%
|MYHA 16U UA| 19%| 25%| 28%| 34%| 36%| 40%| 46%|--| 51%| 64%| 71%| 76%| 79%| 82%| 87%
|Frederick Freeze 16U UA| 18%| 24%| 28%| 34%| 35%| 39%| 46%| 49%|--| 64%| 71%| 76%| 78%| 81%| 87%
|Haverford Hawks 16U A Black| 11%| 16%| 18%| 23%| 24%| 27%| 33%| 36%| 36%|--| 58%| 65%| 67%| 72%| 79%
|JR Black Bears16U Red|  9%| 12%| 14%| 17%| 19%| 21%| 26%| 29%| 29%| 42%|--| 57%| 60%| 65%| 73%
|Grundy Senators|  7%|  9%| 11%| 14%| 15%| 17%| 21%| 24%| 24%| 35%| 43%|--| 53%| 58%| 67%
|Mercer Chiefs|  6%|  8%| 10%| 12%| 13%| 15%| 19%| 21%| 22%| 33%| 40%| 47%|--| 55%| 65%
|Wildcats 16U A Black|  5%|  7%|  8%| 10%| 11%| 13%| 16%| 18%| 19%| 28%| 35%| 42%| 45%|--| 60%
|Igloo Jaguars 16UA Black|  3%|  5%|  5%|  7%|  8%|  9%| 11%| 13%| 13%| 21%| 27%| 33%| 35%| 40%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-08-26 |
| End Date | 2023-08-27 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

