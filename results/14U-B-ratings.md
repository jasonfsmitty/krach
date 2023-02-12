# 14U-B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3067|Championship|MYHA 14U B Blue|16|14|0|1|1|0|486|14.0|-1.0
2|2572|Championship|Ashburn Xtreme|16|13|1|2|0|0|393|14.1|-0.9
3|1262|Championship|Frederick Freeze|16|12|3|1|0|0|497|12.6|-0.4
4|1006|Championship|Team Philadelphia|35|24|8|2|1|0|714|25.4|-0.6
5|494|Gold|Wissahickon Warriors|36|22|9|2|3|0|436|24.3|0.3
6|463|Gold|Palmyra Black Knights|36|21|14|1|0|0|725|22.1|0.1
7|416|Gold|Grundy Senators|36|21|9|0|6|0|690|21.1|0.1
8|134|Gold|Maryland Jr Black Bears|16|5|9|1|1|0|351|6.1|0.1
9|105|Silver|North Jersey Skylands Kings|16|5|8|2|0|1|367|7.9|0.4
10|94|Silver|Igloo Jaguars|35|13|20|0|1|1|358|14.0|0.5
11|93|Silver|North Jersey Sportscare Kings|16|2|8|4|2|0|291|6.2|0.2
12|86|Silver|Lehigh Valley Phantoms|35|9|23|2|1|0|598|11.4|0.4
13|86||Hollydell Hurricanes|34|10|21|1|2|0|448|11.4|0.4
14|59||Royals White|36|6|26|2|2|0|719|8.3|0.3
15|33||Jersey Shore Wildcats|15|3|12|0|0|0|208|3.1|0.1
16|32||NJ Bandits|16|1|10|2|3|0|327|3.1|0.1

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|5.99|-0.00
|Avg|0.37|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 14U B Blue|Ashburn Xtreme|Frederick Freeze|Team Philadelphia|Wissahickon Warriors|Palmyra Black Knights|Grundy Senators|Maryland Jr Black Bears|North Jersey Skylands Kings|Igloo Jaguars|North Jersey Sportscare Kings|Lehigh Valley Phantoms|Hollydell Hurricanes|Royals White|Jersey Shore Wildcats|NJ Bandits
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 14U B Blue|--| 54%| 71%| 75%| 86%| 87%| 88%| 96%| 97%| 97%| 97%| 97%| 97%| 98%| 99%| 99%
|Ashburn Xtreme| 46%|--| 67%| 72%| 84%| 85%| 86%| 95%| 96%| 96%| 97%| 97%| 97%| 98%| 99%| 99%
|Frederick Freeze| 29%| 33%|--| 56%| 72%| 73%| 75%| 90%| 92%| 93%| 93%| 94%| 94%| 96%| 97%| 98%
|Team Philadelphia| 25%| 28%| 44%|--| 67%| 68%| 71%| 88%| 91%| 91%| 92%| 92%| 92%| 95%| 97%| 97%
|Wissahickon Warriors| 14%| 16%| 28%| 33%|--| 52%| 54%| 79%| 82%| 84%| 84%| 85%| 85%| 89%| 94%| 94%
|Palmyra Black Knights| 13%| 15%| 27%| 32%| 48%|--| 53%| 78%| 81%| 83%| 83%| 84%| 84%| 89%| 93%| 94%
|Grundy Senators| 12%| 14%| 25%| 29%| 46%| 47%|--| 76%| 80%| 82%| 82%| 83%| 83%| 88%| 93%| 93%
|Maryland Jr Black Bears|  4%|  5%| 10%| 12%| 21%| 22%| 24%|--| 56%| 59%| 59%| 61%| 61%| 70%| 80%| 81%
|North Jersey Skylands Kings|  3%|  4%|  8%|  9%| 18%| 19%| 20%| 44%|--| 53%| 53%| 55%| 55%| 64%| 76%| 77%
|Igloo Jaguars|  3%|  4%|  7%|  9%| 16%| 17%| 18%| 41%| 47%|--| 50%| 52%| 52%| 62%| 74%| 74%
|North Jersey Sportscare Kings|  3%|  3%|  7%|  8%| 16%| 17%| 18%| 41%| 47%| 50%|--| 52%| 52%| 61%| 74%| 74%
|Lehigh Valley Phantoms|  3%|  3%|  6%|  8%| 15%| 16%| 17%| 39%| 45%| 48%| 48%|--| 50%| 60%| 73%| 73%
|Hollydell Hurricanes|  3%|  3%|  6%|  8%| 15%| 16%| 17%| 39%| 45%| 48%| 48%| 50%|--| 60%| 73%| 73%
|Royals White|  2%|  2%|  4%|  5%| 11%| 11%| 12%| 30%| 36%| 38%| 39%| 40%| 40%|--| 64%| 65%
|Jersey Shore Wildcats|  1%|  1%|  3%|  3%|  6%|  7%|  7%| 20%| 24%| 26%| 26%| 27%| 27%| 36%|--| 50%
|NJ Bandits|  1%|  1%|  2%|  3%|  6%|  6%|  7%| 19%| 23%| 26%| 26%| 27%| 27%| 35%| 50%|--

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
| Date Cutoff | 2023-02-12 |

