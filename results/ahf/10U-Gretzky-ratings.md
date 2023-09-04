[<- back to the index](readme.md)
# 10U Gretzky KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3054|Championship|Palmyra Black Knights- Rochefort|5|4|0|0|0|1|582|4.8|-0.0
2|2106|Championship|Igloo Jaguars 10UA|5|4|0|0|0|1|372|4.9|0.0
3|992|Championship|Long Island Whalers Squirt Blue|5|3|1|0|0|1|850|3.8|-0.0
4|870|Championship|Jersey Colts Squirt Black|5|3|1|0|0|1|817|3.8|-0.0
5|527|Gold|JR Black Bears10U White|5|2|2|0|0|1|1181|2.9|0.0
6|431|Gold|MYHA 10U UA Blue|5|2|2|0|0|1|744|2.9|0.0
7|380|Gold|Lancaster Firebirds Squirt Black|5|2|2|0|0|1|658|2.9|0.0
8|354|Gold|Royals 10U A Gray|5|2|2|0|0|1|442|2.9|0.0
9|350||Southern Maryland Sabres 10U Gold|5|2|2|0|0|1|442|2.9|0.0
10|263||NJ Bandits 10A|5|2|2|0|0|1|312|2.9|0.0
11|110||STJ 10U Navy|5|0|4|0|0|1|1341|0.9|0.0
12|80||Team Philadelphia|5|0|4|0|0|1|578|0.9|0.0
13|72||RHC Squirt A|5|0|4|0|0|1|420|0.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Palmyra Black Knights- Rochefort|Igloo Jaguars 10UA|Long Island Whalers Squirt Blue|Jersey Colts Squirt Black|JR Black Bears10U White|MYHA 10U UA Blue|Lancaster Firebirds Squirt Black|Royals 10U A Gray|Southern Maryland Sabres 10U Gold|NJ Bandits 10A|STJ 10U Navy|Team Philadelphia|RHC Squirt A
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Palmyra Black Knights- Rochefort|--| 59%| 75%| 78%| 85%| 88%| 89%| 90%| 90%| 92%| 97%| 97%| 98%
|Igloo Jaguars 10UA| 41%|--| 68%| 71%| 80%| 83%| 85%| 86%| 86%| 89%| 95%| 96%| 97%
|Long Island Whalers Squirt Blue| 25%| 32%|--| 53%| 65%| 70%| 72%| 74%| 74%| 79%| 90%| 93%| 93%
|Jersey Colts Squirt Black| 22%| 29%| 47%|--| 62%| 67%| 70%| 71%| 71%| 77%| 89%| 92%| 92%
|JR Black Bears10U White| 15%| 20%| 35%| 38%|--| 55%| 58%| 60%| 60%| 67%| 83%| 87%| 88%
|MYHA 10U UA Blue| 12%| 17%| 30%| 33%| 45%|--| 53%| 55%| 55%| 62%| 80%| 84%| 86%
|Lancaster Firebirds Squirt Black| 11%| 15%| 28%| 30%| 42%| 47%|--| 52%| 52%| 59%| 78%| 83%| 84%
|Royals 10U A Gray| 10%| 14%| 26%| 29%| 40%| 45%| 48%|--| 50%| 57%| 76%| 82%| 83%
|Southern Maryland Sabres 10U Gold| 10%| 14%| 26%| 29%| 40%| 45%| 48%| 50%|--| 57%| 76%| 81%| 83%
|NJ Bandits 10A|  8%| 11%| 21%| 23%| 33%| 38%| 41%| 43%| 43%|--| 71%| 77%| 78%
|STJ 10U Navy|  3%|  5%| 10%| 11%| 17%| 20%| 22%| 24%| 24%| 29%|--| 58%| 60%
|Team Philadelphia|  3%|  4%|  7%|  8%| 13%| 16%| 17%| 18%| 19%| 23%| 42%|--| 52%
|RHC Squirt A|  2%|  3%|  7%|  8%| 12%| 14%| 16%| 17%| 17%| 22%| 40%| 48%|--

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

