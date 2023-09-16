[<- back to the index](readme.md)
# 10U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4014|Championship|Palmyra Black Knights- Rochefort|9|8|0|0|0|1|416|8.8|-0.0
2|1261|Championship|Igloo Jaguars 10UA|9|7|1|0|0|1|330|7.9|0.0
3|1222|Championship|Jersey Colts Squirt Black|7|5|1|0|0|1|785|5.8|-0.0
4|639|Championship|JR Black Bears10U White|8|4|3|0|0|1|1057|4.9|0.0
5|539|Gold|Long Island Whalers Squirt Blue|6|3|2|0|0|1|1006|3.8|-0.0
6|273|Gold|MYHA 10U UA Blue|7|2|4|0|0|1|1569|2.9|0.0
7|254|Gold|Royals 10U A Gray|7|3|3|0|0|1|380|3.9|0.0
8|209|Gold|Southern Maryland Sabres 10U Gold|5|2|2|0|0|1|259|2.9|0.0
9|189||Lancaster Firebirds Squirt Black|7|2|4|0|0|1|955|2.9|0.0
10|163||NJ Bandits 10A|7|3|3|0|0|1|231|3.9|0.0
11|80||STJ 10U Navy|5|0|4|0|0|1|1388|0.9|0.0
12|55||Team Philadelphia|5|0|4|0|0|1|492|0.9|0.0
13|31||RHC Squirt A|8|0|7|0|0|1|420|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Palmyra Black Knights- Rochefort|Igloo Jaguars 10UA|Jersey Colts Squirt Black|JR Black Bears10U White|Long Island Whalers Squirt Blue|MYHA 10U UA Blue|Royals 10U A Gray|Southern Maryland Sabres 10U Gold|Lancaster Firebirds Squirt Black|NJ Bandits 10A|STJ 10U Navy|Team Philadelphia|RHC Squirt A
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Palmyra Black Knights- Rochefort|--| 76%| 77%| 86%| 88%| 94%| 94%| 95%| 95%| 96%| 98%| 99%| 99%
|Igloo Jaguars 10UA| 24%|--| 51%| 66%| 70%| 82%| 83%| 86%| 87%| 89%| 94%| 96%| 98%
|Jersey Colts Squirt Black| 23%| 49%|--| 66%| 69%| 82%| 83%| 85%| 87%| 88%| 94%| 96%| 98%
|JR Black Bears10U White| 14%| 34%| 34%|--| 54%| 70%| 72%| 75%| 77%| 80%| 89%| 92%| 95%
|Long Island Whalers Squirt Blue| 12%| 30%| 31%| 46%|--| 66%| 68%| 72%| 74%| 77%| 87%| 91%| 95%
|MYHA 10U UA Blue|  6%| 18%| 18%| 30%| 34%|--| 52%| 57%| 59%| 63%| 77%| 83%| 90%
|Royals 10U A Gray|  6%| 17%| 17%| 28%| 32%| 48%|--| 55%| 57%| 61%| 76%| 82%| 89%
|Southern Maryland Sabres 10U Gold|  5%| 14%| 15%| 25%| 28%| 43%| 45%|--| 52%| 56%| 72%| 79%| 87%
|Lancaster Firebirds Squirt Black|  5%| 13%| 13%| 23%| 26%| 41%| 43%| 48%|--| 54%| 70%| 77%| 86%
|NJ Bandits 10A|  4%| 11%| 12%| 20%| 23%| 37%| 39%| 44%| 46%|--| 67%| 75%| 84%
|STJ 10U Navy|  2%|  6%|  6%| 11%| 13%| 23%| 24%| 28%| 30%| 33%|--| 59%| 72%
|Team Philadelphia|  1%|  4%|  4%|  8%|  9%| 17%| 18%| 21%| 23%| 25%| 41%|--| 64%
|RHC Squirt A|  1%|  2%|  2%|  5%|  5%| 10%| 11%| 13%| 14%| 16%| 28%| 36%|--

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

