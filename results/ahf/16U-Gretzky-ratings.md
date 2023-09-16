[<- back to the index](readme.md)
# 16U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|2031|Championship|Dix Hills Hawks 16U|7|6|0|0|0|1|266|6.8|-0.0
2|1538|Championship|STJ 16U Gold|5|3|0|0|0|2|606|4.7|0.0
3|955|Championship|Aviator Hockey Club 16U Minor|5|3|1|0|0|1|586|3.9|0.0
4|871|Championship|VFC 16A Frederick|9|5|2|0|0|2|613|6.7|-0.0
5|837|Gold|Team Philadelphia Black|5|3|1|0|0|1|550|3.9|0.0
6|698|Gold|Frederick Freeze 16U UA|6|4|1|0|0|1|309|4.9|0.0
7|695|Gold|Palmyra Black Knights|6|3|1|0|0|2|483|4.7|0.0
8|581|Gold|MYHA 16U UA|7|3|3|0|0|1|682|3.9|0.0
9|370|Silver|Tri-City Eagles 16U White|9|3|3|0|0|3|451|5.6|0.0
10|237|Silver|Haverford Hawks 16U A Black|9|2|4|0|0|3|599|4.6|0.0
11|189|Silver|Grundy Senators|8|3|4|0|0|1|354|3.9|0.0
12|159|Silver|Mercer Chiefs|6|1|4|0|0|1|616|1.9|0.0
13|129||JR Black Bears16U Red|6|1|4|0|0|1|452|1.9|0.0
14|115||Wildcats 16U A Black|5|0|4|0|0|1|929|0.9|0.0
15|84||Igloo Jaguars 16UA Black|9|0|7|0|0|2|943|1.7|-0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Dix Hills Hawks 16U|STJ 16U Gold|Aviator Hockey Club 16U Minor|VFC 16A Frederick|Team Philadelphia Black|Frederick Freeze 16U UA|Palmyra Black Knights|MYHA 16U UA|Tri-City Eagles 16U White|Haverford Hawks 16U A Black|Grundy Senators|Mercer Chiefs|JR Black Bears16U Red|Wildcats 16U A Black|Igloo Jaguars 16UA Black
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Dix Hills Hawks 16U|--| 57%| 68%| 70%| 71%| 74%| 75%| 78%| 85%| 90%| 91%| 93%| 94%| 95%| 96%
|STJ 16U Gold| 43%|--| 62%| 64%| 65%| 69%| 69%| 73%| 81%| 87%| 89%| 91%| 92%| 93%| 95%
|Aviator Hockey Club 16U Minor| 32%| 38%|--| 52%| 53%| 58%| 58%| 62%| 72%| 80%| 83%| 86%| 88%| 89%| 92%
|VFC 16A Frederick| 30%| 36%| 48%|--| 51%| 56%| 56%| 60%| 70%| 79%| 82%| 85%| 87%| 88%| 91%
|Team Philadelphia Black| 29%| 35%| 47%| 49%|--| 55%| 55%| 59%| 69%| 78%| 82%| 84%| 87%| 88%| 91%
|Frederick Freeze 16U UA| 26%| 31%| 42%| 44%| 45%|--| 50%| 55%| 65%| 75%| 79%| 81%| 84%| 86%| 89%
|Palmyra Black Knights| 25%| 31%| 42%| 44%| 45%| 50%|--| 54%| 65%| 75%| 79%| 81%| 84%| 86%| 89%
|MYHA 16U UA| 22%| 27%| 38%| 40%| 41%| 45%| 46%|--| 61%| 71%| 75%| 79%| 82%| 83%| 87%
|Tri-City Eagles 16U White| 15%| 19%| 28%| 30%| 31%| 35%| 35%| 39%|--| 61%| 66%| 70%| 74%| 76%| 81%
|Haverford Hawks 16U A Black| 10%| 13%| 20%| 21%| 22%| 25%| 25%| 29%| 39%|--| 56%| 60%| 65%| 67%| 74%
|Grundy Senators|  9%| 11%| 17%| 18%| 18%| 21%| 21%| 25%| 34%| 44%|--| 54%| 59%| 62%| 69%
|Mercer Chiefs|  7%|  9%| 14%| 15%| 16%| 19%| 19%| 21%| 30%| 40%| 46%|--| 55%| 58%| 65%
|JR Black Bears16U Red|  6%|  8%| 12%| 13%| 13%| 16%| 16%| 18%| 26%| 35%| 41%| 45%|--| 53%| 61%
|Wildcats 16U A Black|  5%|  7%| 11%| 12%| 12%| 14%| 14%| 17%| 24%| 33%| 38%| 42%| 47%|--| 58%
|Igloo Jaguars 16UA Black|  4%|  5%|  8%|  9%|  9%| 11%| 11%| 13%| 19%| 26%| 31%| 35%| 39%| 42%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2023-08-26 |
| End Date | 2023-09-16 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 4 |

