[<- back to the index](readme.md)
# 14U B KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|3288|Championship|MYHA 14U B Blue|17|14|0|1|1|1|420|15.8|-0.0
2|2673|Championship|Ashburn Xtreme|17|13|1|2|0|1|346|15.8|-0.0
3|1036|Championship|Frederick Freeze|17|12|3|1|0|1|463|13.9|0.0
4|945|Championship|Team Philadelphia|36|24|8|2|1|1|696|26.8|-0.0
5|411|Gold|Wissahickon Warriors|37|22|9|2|3|1|404|24.9|0.0
6|403|Gold|Palmyra Black Knights|37|21|14|1|0|1|715|22.9|0.0
7|357|Gold|Grundy Senators|37|21|9|0|6|1|667|21.9|0.0
8|124|Gold|Maryland Jr Black Bears|17|5|9|1|1|1|301|6.9|0.0
9|99|Silver|North Jersey Skylands Kings|17|5|8|2|0|2|357|8.7|0.0
10|88|Silver|North Jersey Sportscare Kings|17|2|8|4|2|1|259|6.9|0.0
11|87|Silver|Lehigh Valley Phantoms|37|10|23|2|1|1|557|12.9|0.0
12|86|Silver|Igloo Jaguars|36|13|20|0|1|2|329|14.7|0.0
13|79||Hollydell Hurricanes|37|11|22|1|2|1|380|12.9|0.0
14|57||Royals White|37|6|26|2|2|1|688|8.9|0.0
15|37||NJ Bandits|17|1|10|2|3|1|288|3.9|0.0
16|33||Jersey Shore Wildcats|17|3|13|0|0|1|178|3.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|-0.00
|Avg|0.00|-0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 14U B Blue|Ashburn Xtreme|Frederick Freeze|Team Philadelphia|Wissahickon Warriors|Palmyra Black Knights|Grundy Senators|Maryland Jr Black Bears|North Jersey Skylands Kings|North Jersey Sportscare Kings|Lehigh Valley Phantoms|Igloo Jaguars|Hollydell Hurricanes|Royals White|NJ Bandits|Jersey Shore Wildcats
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 14U B Blue|--| 55%| 76%| 78%| 89%| 89%| 90%| 96%| 97%| 97%| 97%| 97%| 98%| 98%| 99%| 99%
|Ashburn Xtreme| 45%|--| 72%| 74%| 87%| 87%| 88%| 96%| 96%| 97%| 97%| 97%| 97%| 98%| 99%| 99%
|Frederick Freeze| 24%| 28%|--| 52%| 72%| 72%| 74%| 89%| 91%| 92%| 92%| 92%| 93%| 95%| 97%| 97%
|Team Philadelphia| 22%| 26%| 48%|--| 70%| 70%| 73%| 88%| 91%| 91%| 92%| 92%| 92%| 94%| 96%| 97%
|Wissahickon Warriors| 11%| 13%| 28%| 30%|--| 51%| 53%| 77%| 81%| 82%| 82%| 83%| 84%| 88%| 92%| 93%
|Palmyra Black Knights| 11%| 13%| 28%| 30%| 49%|--| 53%| 76%| 80%| 82%| 82%| 82%| 84%| 88%| 92%| 92%
|Grundy Senators| 10%| 12%| 26%| 27%| 47%| 47%|--| 74%| 78%| 80%| 80%| 81%| 82%| 86%| 91%| 92%
|Maryland Jr Black Bears|  4%|  4%| 11%| 12%| 23%| 24%| 26%|--| 56%| 58%| 59%| 59%| 61%| 68%| 77%| 79%
|North Jersey Skylands Kings|  3%|  4%|  9%|  9%| 19%| 20%| 22%| 44%|--| 53%| 53%| 53%| 56%| 63%| 73%| 75%
|North Jersey Sportscare Kings|  3%|  3%|  8%|  9%| 18%| 18%| 20%| 42%| 47%|--| 50%| 51%| 53%| 61%| 71%| 73%
|Lehigh Valley Phantoms|  3%|  3%|  8%|  8%| 18%| 18%| 20%| 41%| 47%| 50%|--| 50%| 53%| 60%| 70%| 73%
|Igloo Jaguars|  3%|  3%|  8%|  8%| 17%| 18%| 19%| 41%| 47%| 49%| 50%|--| 52%| 60%| 70%| 72%
|Hollydell Hurricanes|  2%|  3%|  7%|  8%| 16%| 16%| 18%| 39%| 44%| 47%| 47%| 48%|--| 58%| 68%| 71%
|Royals White|  2%|  2%|  5%|  6%| 12%| 12%| 14%| 32%| 37%| 39%| 40%| 40%| 42%|--| 61%| 64%
|NJ Bandits|  1%|  1%|  3%|  4%|  8%|  8%|  9%| 23%| 27%| 29%| 30%| 30%| 32%| 39%|--| 53%
|Jersey Shore Wildcats|  1%|  1%|  3%|  3%|  7%|  8%|  8%| 21%| 25%| 27%| 27%| 28%| 29%| 36%| 47%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-28 |
| End Date | 2023-02-19 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

