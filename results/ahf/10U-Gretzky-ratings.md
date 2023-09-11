[<- back to the index](readme.md)
# 10U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|4096|Championship|Palmyra Black Knights- Rochefort|8|7|0|0|0|1|482|7.8|-0.0
2|1369|Championship|Jersey Colts Squirt Black|7|5|1|0|0|1|827|5.8|-0.0
3|1286|Championship|Igloo Jaguars 10UA|8|6|1|0|0|1|369|6.9|0.0
4|617|Championship|Long Island Whalers Squirt Blue|6|3|2|0|0|1|1067|3.8|-0.0
5|582|Gold|JR Black Bears10U White|7|3|3|0|0|1|1214|3.9|0.0
6|306|Gold|MYHA 10U UA Blue|7|2|4|0|0|1|1628|2.9|0.0
7|300|Gold|Royals 10U A Gray|7|3|3|0|0|1|439|3.9|0.0
8|266|Gold|Lancaster Firebirds Squirt Black|6|2|3|0|0|1|1050|2.9|0.0
9|254||Southern Maryland Sabres 10U Gold|5|2|2|0|0|1|309|2.9|0.0
10|184||NJ Bandits 10A|7|3|3|0|0|1|243|3.9|0.0
11|90||STJ 10U Navy|5|0|4|0|0|1|1451|0.9|0.0
12|63||Team Philadelphia|5|0|4|0|0|1|558|0.9|0.0
13|42||RHC Squirt A|6|0|5|0|0|1|319|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Palmyra Black Knights- Rochefort|Jersey Colts Squirt Black|Igloo Jaguars 10UA|Long Island Whalers Squirt Blue|JR Black Bears10U White|MYHA 10U UA Blue|Royals 10U A Gray|Lancaster Firebirds Squirt Black|Southern Maryland Sabres 10U Gold|NJ Bandits 10A|STJ 10U Navy|Team Philadelphia|RHC Squirt A
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Palmyra Black Knights- Rochefort|--| 75%| 76%| 87%| 88%| 93%| 93%| 94%| 94%| 96%| 98%| 98%| 99%
|Jersey Colts Squirt Black| 25%|--| 52%| 69%| 70%| 82%| 82%| 84%| 84%| 88%| 94%| 96%| 97%
|Igloo Jaguars 10UA| 24%| 48%|--| 68%| 69%| 81%| 81%| 83%| 84%| 87%| 93%| 95%| 97%
|Long Island Whalers Squirt Blue| 13%| 31%| 32%|--| 51%| 67%| 67%| 70%| 71%| 77%| 87%| 91%| 94%
|JR Black Bears10U White| 12%| 30%| 31%| 49%|--| 66%| 66%| 69%| 70%| 76%| 87%| 90%| 93%
|MYHA 10U UA Blue|  7%| 18%| 19%| 33%| 34%|--| 50%| 54%| 55%| 62%| 77%| 83%| 88%
|Royals 10U A Gray|  7%| 18%| 19%| 33%| 34%| 50%|--| 53%| 54%| 62%| 77%| 83%| 88%
|Lancaster Firebirds Squirt Black|  6%| 16%| 17%| 30%| 31%| 46%| 47%|--| 51%| 59%| 75%| 81%| 86%
|Southern Maryland Sabres 10U Gold|  6%| 16%| 16%| 29%| 30%| 45%| 46%| 49%|--| 58%| 74%| 80%| 86%
|NJ Bandits 10A|  4%| 12%| 13%| 23%| 24%| 38%| 38%| 41%| 42%|--| 67%| 74%| 81%
|STJ 10U Navy|  2%|  6%|  7%| 13%| 13%| 23%| 23%| 25%| 26%| 33%|--| 59%| 68%
|Team Philadelphia|  2%|  4%|  5%|  9%| 10%| 17%| 17%| 19%| 20%| 26%| 41%|--| 60%
|RHC Squirt A|  1%|  3%|  3%|  6%|  7%| 12%| 12%| 14%| 14%| 19%| 32%| 40%|--

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

