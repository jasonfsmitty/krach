# 13U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1367|Championship|MYHA 14U UA Gold|16|11|2|1|2|0|600|11.5|-0.5
2|1353|Championship|North Jersey Avalanche|16|11|2|2|1|0|471|12.4|-0.6
3|1073|Championship|Igloo Jaguars|39|30|3|2|4|0|385|30.8|-1.2
4|594|Championship|Rockets Hockey Club Black|39|23|13|2|1|0|605|24.4|-0.6
5|571|Gold|Lehigh Valley Phantoms|40|27|12|1|0|0|462|27.7|-0.3
6|503|Gold|NJ Stars|38|24|8|1|5|0|517|24.7|-0.3
7|293|Gold|Long Island Rebels|16|12|4|0|0|0|121|12.6|0.6
8|133|Gold|Valley Forge Colonials 13U AA|40|16|20|2|2|0|389|18.5|0.5
9|131|Silver|Team Philadelphia|40|16|21|2|1|0|386|18.5|0.5
10|88|Silver|Rockets Hockey Club White|39|14|20|2|3|0|357|16.7|0.7
11|55|Silver|Ashburn Xtreme 2009|16|3|12|0|1|0|750|3.1|0.1
12|34|Silver|Metro Militia|12|4|7|1|0|0|59|5.3|0.3
13|33||Delaware Ducks 13U AA|40|6|28|4|2|0|282|10.5|0.5
14|27||Royals 2009|38|5|27|3|3|0|303|8.4|0.4
15|19||Philadelphia Blazers|37|2|29|4|2|0|284|6.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|7.40|0.40
|Avg|0.49|0.03

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||MYHA 14U UA Gold|North Jersey Avalanche|Igloo Jaguars|Rockets Hockey Club Black|Lehigh Valley Phantoms|NJ Stars|Long Island Rebels|Valley Forge Colonials 13U AA|Team Philadelphia|Rockets Hockey Club White|Ashburn Xtreme 2009|Metro Militia|Delaware Ducks 13U AA|Royals 2009|Philadelphia Blazers
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|MYHA 14U UA Gold|--| 50%| 56%| 70%| 71%| 73%| 82%| 91%| 91%| 94%| 96%| 98%| 98%| 98%| 99%
|North Jersey Avalanche| 50%|--| 56%| 70%| 70%| 73%| 82%| 91%| 91%| 94%| 96%| 98%| 98%| 98%| 99%
|Igloo Jaguars| 44%| 44%|--| 64%| 65%| 68%| 79%| 89%| 89%| 92%| 95%| 97%| 97%| 98%| 98%
|Rockets Hockey Club Black| 30%| 30%| 36%|--| 51%| 54%| 67%| 82%| 82%| 87%| 92%| 95%| 95%| 96%| 97%
|Lehigh Valley Phantoms| 29%| 30%| 35%| 49%|--| 53%| 66%| 81%| 81%| 87%| 91%| 94%| 95%| 95%| 97%
|NJ Stars| 27%| 27%| 32%| 46%| 47%|--| 63%| 79%| 79%| 85%| 90%| 94%| 94%| 95%| 96%
|Long Island Rebels| 18%| 18%| 21%| 33%| 34%| 37%|--| 69%| 69%| 77%| 84%| 90%| 90%| 92%| 94%
|Valley Forge Colonials 13U AA|  9%|  9%| 11%| 18%| 19%| 21%| 31%|--| 50%| 60%| 71%| 79%| 80%| 83%| 88%
|Team Philadelphia|  9%|  9%| 11%| 18%| 19%| 21%| 31%| 50%|--| 60%| 70%| 79%| 80%| 83%| 88%
|Rockets Hockey Club White|  6%|  6%|  8%| 13%| 13%| 15%| 23%| 40%| 40%|--| 62%| 72%| 73%| 76%| 83%
|Ashburn Xtreme 2009|  4%|  4%|  5%|  8%|  9%| 10%| 16%| 29%| 30%| 38%|--| 61%| 62%| 67%| 75%
|Metro Militia|  2%|  2%|  3%|  5%|  6%|  6%| 10%| 21%| 21%| 28%| 39%|--| 51%| 56%| 65%
|Delaware Ducks 13U AA|  2%|  2%|  3%|  5%|  5%|  6%| 10%| 20%| 20%| 27%| 38%| 49%|--| 55%| 64%
|Royals 2009|  2%|  2%|  2%|  4%|  5%|  5%|  8%| 17%| 17%| 24%| 33%| 44%| 45%|--| 59%
|Philadelphia Blazers|  1%|  1%|  2%|  3%|  3%|  4%|  6%| 12%| 12%| 17%| 25%| 35%| 36%| 41%|--

## Generation Details

Generated with command line:
```
../ahf.py -f 13U-AA-filter.txt -n 13U-AA -o 13U-AA-ratings.md 13U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
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

