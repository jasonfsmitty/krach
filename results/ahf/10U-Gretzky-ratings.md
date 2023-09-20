[<- back to the index](readme.md)
# 10U Gretzky KRACH Rankings
Rankings generated on Wed Sep 20 23:50:55 2023.

Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4113|Championship|Palmyra Black Knights- Rochefort|10|10|0|0|0|0|347|10.8|-0.0
2|1170|Championship|Igloo Jaguars 10UA|9|8|1|0|0|0|285|8.9|0.0
3|1163|Championship|Jersey Colts Squirt Black|6|5|1|0|0|0|792|5.8|-0.0
4|657|Championship|JR Black Bears10U White|8|5|3|0|0|0|928|5.9|0.0
5|584|Gold|Long Island Whalers Squirt Blue|6|4|2|0|0|0|877|4.9|0.0
6|252|Gold|MYHA 10U UA Blue|6|2|4|0|0|0|1570|2.9|0.0
7|228|Gold|Royals 10U A Gray|6|3|3|0|0|0|361|3.9|0.0
8|185|Gold|Southern Maryland Sabres 10U Gold|4|2|2|0|0|0|247|2.9|0.0
9|158||NJ Bandits 10A|8|4|4|0|0|0|244|4.9|0.0
10|149||Lancaster Firebirds Squirt Black|7|2|5|0|0|0|910|2.9|0.0
11|74||STJ 10U Navy|4|0|4|0|0|0|1370|0.9|0.0
12|41||Team Philadelphia|7|0|7|0|0|0|1004|0.9|0.0
13|25||RHC Squirt A|8|0|8|0|0|0|387|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Palmyra Black Knights- Rochefort|Igloo Jaguars 10UA|Jersey Colts Squirt Black|JR Black Bears10U White|Long Island Whalers Squirt Blue|MYHA 10U UA Blue|Royals 10U A Gray|Southern Maryland Sabres 10U Gold|NJ Bandits 10A|Lancaster Firebirds Squirt Black|STJ 10U Navy|Team Philadelphia|RHC Squirt A
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Palmyra Black Knights- Rochefort|--| 78%| 78%| 86%| 88%| 94%| 95%| 96%| 96%| 97%| 98%| 99%| 99%
|Igloo Jaguars 10UA| 22%|--| 50%| 64%| 67%| 82%| 84%| 86%| 88%| 89%| 94%| 97%| 98%
|Jersey Colts Squirt Black| 22%| 50%|--| 64%| 67%| 82%| 84%| 86%| 88%| 89%| 94%| 97%| 98%
|JR Black Bears10U White| 14%| 36%| 36%|--| 53%| 72%| 74%| 78%| 81%| 82%| 90%| 94%| 96%
|Long Island Whalers Squirt Blue| 12%| 33%| 33%| 47%|--| 70%| 72%| 76%| 79%| 80%| 89%| 93%| 96%
|MYHA 10U UA Blue|  6%| 18%| 18%| 28%| 30%|--| 53%| 58%| 61%| 63%| 77%| 86%| 91%
|Royals 10U A Gray|  5%| 16%| 16%| 26%| 28%| 47%|--| 55%| 59%| 60%| 75%| 85%| 90%
|Southern Maryland Sabres 10U Gold|  4%| 14%| 14%| 22%| 24%| 42%| 45%|--| 54%| 55%| 71%| 82%| 88%
|NJ Bandits 10A|  4%| 12%| 12%| 19%| 21%| 39%| 41%| 46%|--| 52%| 68%| 79%| 86%
|Lancaster Firebirds Squirt Black|  3%| 11%| 11%| 18%| 20%| 37%| 40%| 45%| 48%|--| 67%| 78%| 86%
|STJ 10U Navy|  2%|  6%|  6%| 10%| 11%| 23%| 25%| 29%| 32%| 33%|--| 64%| 75%
|Team Philadelphia|  1%|  3%|  3%|  6%|  7%| 14%| 15%| 18%| 21%| 22%| 36%|--| 62%
|RHC Squirt A|  1%|  2%|  2%|  4%|  4%|  9%| 10%| 12%| 14%| 14%| 25%| 38%|--

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

