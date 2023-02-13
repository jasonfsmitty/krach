# 14U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3060|Championship|MYHA 14U B Blue|16|14|0|1|1|0|487|14.0|-1.0
2|2569|Championship|Ashburn Xtreme|16|13|1|2|0|0|393|14.1|-0.9
3|1266|Championship|Frederick Freeze|16|12|3|1|0|0|497|12.6|-0.4
4|1007|Championship|Team Philadelphia|35|24|8|2|1|0|714|25.3|-0.7
5|495|Gold|Wissahickon Warriors|36|22|9|2|3|0|437|24.3|0.3
6|463|Gold|Palmyra Black Knights|36|21|14|1|0|0|724|22.1|0.1
7|417|Gold|Grundy Senators|36|21|9|0|6|0|690|21.1|0.1
8|135|Gold|Maryland Jr Black Bears|16|5|9|1|1|0|352|6.1|0.1
9|104|Silver|North Jersey Skylands Kings|16|5|8|2|0|1|366|7.9|0.4
10|94|Silver|North Jersey Sportscare Kings|16|2|8|4|2|0|292|6.2|0.2
11|93|Silver|Igloo Jaguars|35|13|20|0|1|1|358|14.0|0.5
12|90|Silver|Hollydell Hurricanes|35|11|21|1|2|0|436|12.4|0.4
13|86||Lehigh Valley Phantoms|35|9|23|2|1|0|598|11.4|0.4
14|58||Royals White|36|6|26|2|2|0|719|8.3|0.3
15|32||NJ Bandits|16|1|10|2|3|0|328|3.1|0.1
16|29||Jersey Shore Wildcats|16|3|13|0|0|0|201|3.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|6.03|-0.00
|Avg|0.38|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 14U B Blue|Ashburn Xtreme|Frederick Freeze|Team Philadelphia|Wissahickon Warriors|Palmyra Black Knights|Grundy Senators|Maryland Jr Black Bears|North Jersey Skylands Kings|North Jersey Sportscare Kings|Igloo Jaguars|Hollydell Hurricanes|Lehigh Valley Phantoms|Royals White|NJ Bandits|Jersey Shore Wildcats
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 14U B Blue|--| 54%| 71%| 75%| 86%| 87%| 88%| 96%| 97%| 97%| 97%| 97%| 97%| 98%| 99%| 99%
|Ashburn Xtreme| 46%|--| 67%| 72%| 84%| 85%| 86%| 95%| 96%| 96%| 96%| 97%| 97%| 98%| 99%| 99%
|Frederick Freeze| 29%| 33%|--| 56%| 72%| 73%| 75%| 90%| 92%| 93%| 93%| 93%| 94%| 96%| 98%| 98%
|Team Philadelphia| 25%| 28%| 44%|--| 67%| 68%| 71%| 88%| 91%| 91%| 92%| 92%| 92%| 95%| 97%| 97%
|Wissahickon Warriors| 14%| 16%| 28%| 33%|--| 52%| 54%| 79%| 83%| 84%| 84%| 85%| 85%| 89%| 94%| 94%
|Palmyra Black Knights| 13%| 15%| 27%| 32%| 48%|--| 53%| 77%| 82%| 83%| 83%| 84%| 84%| 89%| 93%| 94%
|Grundy Senators| 12%| 14%| 25%| 29%| 46%| 47%|--| 76%| 80%| 82%| 82%| 82%| 83%| 88%| 93%| 93%
|Maryland Jr Black Bears|  4%|  5%| 10%| 12%| 21%| 23%| 24%|--| 56%| 59%| 59%| 60%| 61%| 70%| 81%| 82%
|North Jersey Skylands Kings|  3%|  4%|  8%|  9%| 17%| 18%| 20%| 44%|--| 53%| 53%| 54%| 55%| 64%| 76%| 78%
|North Jersey Sportscare Kings|  3%|  4%|  7%|  9%| 16%| 17%| 18%| 41%| 47%|--| 50%| 51%| 52%| 62%| 74%| 76%
|Igloo Jaguars|  3%|  4%|  7%|  8%| 16%| 17%| 18%| 41%| 47%| 50%|--| 51%| 52%| 62%| 74%| 76%
|Hollydell Hurricanes|  3%|  3%|  7%|  8%| 15%| 16%| 18%| 40%| 46%| 49%| 49%|--| 51%| 61%| 74%| 75%
|Lehigh Valley Phantoms|  3%|  3%|  6%|  8%| 15%| 16%| 17%| 39%| 45%| 48%| 48%| 49%|--| 60%| 73%| 75%
|Royals White|  2%|  2%|  4%|  5%| 11%| 11%| 12%| 30%| 36%| 38%| 38%| 39%| 40%|--| 64%| 67%
|NJ Bandits|  1%|  1%|  2%|  3%|  6%|  7%|  7%| 19%| 24%| 26%| 26%| 26%| 27%| 36%|--| 52%
|Jersey Shore Wildcats|  1%|  1%|  2%|  3%|  6%|  6%|  7%| 18%| 22%| 24%| 24%| 25%| 25%| 33%| 48%|--

## Generation Details

Generated with command line:
```
../ahf.py -f 14U-B-filter.txt -n 14U-B -o 14U-B-ratings.md 14U-B-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
| End Date | 2023-02-12 |
| KRACH Method | BRADLEY_TERRY |
| SoS Method | AVERAGE |
| Max Iterations | 10 |
| Max Ratings Diff | 1e-07 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.50 |
| Fake Ties | 0 |
| Ignore teams |  |
| Min Games Played | 12 |
| Date Cutoff | 2023-02-13 |

