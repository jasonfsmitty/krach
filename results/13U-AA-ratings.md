[<- back to the index](readme.md)
# 13U AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1609|Championship|North Jersey Avalanche|17|11|2|2|1|1|554|13.8|-0.0
2|1579|Championship|MYHA 14U UA Gold|17|11|2|1|2|1|704|12.8|-0.0
3|1412|Championship|Igloo Jaguars|40|30|3|2|4|1|445|32.8|-0.0
4|707|Championship|Rockets Hockey Club Black|41|24|13|2|1|1|644|26.8|-0.0
5|660|Gold|Lehigh Valley Phantoms|41|27|12|1|0|1|497|28.8|-0.0
6|590|Gold|NJ Stars|40|25|8|1|5|1|546|26.8|-0.0
7|259|Gold|Long Island Rebels|17|12|4|0|0|1|147|12.9|0.0
8|151|Gold|Valley Forge Colonials 13U AA|41|16|20|2|2|1|460|18.9|0.0
9|149|Silver|Team Philadelphia|41|16|21|2|1|1|457|18.9|0.0
10|101|Silver|Rockets Hockey Club White|41|15|20|2|3|1|414|17.9|0.0
11|78|Silver|Ashburn Xtreme 2009|17|3|12|0|1|1|742|3.9|0.0
12|45|Silver|Metro Militia|13|4|7|1|0|1|81|5.9|0.0
13|40||Delaware Ducks 13U AA|41|6|28|4|2|1|333|10.9|0.0
14|32||Royals 2009|40|5|28|3|3|1|352|8.9|0.0
15|23||Philadelphia Blazers|40|2|31|4|2|1|352|6.9|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|0.00|0.00
|Avg|0.00|0.00

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||North Jersey Avalanche|MYHA 14U UA Gold|Igloo Jaguars|Rockets Hockey Club Black|Lehigh Valley Phantoms|NJ Stars|Long Island Rebels|Valley Forge Colonials 13U AA|Team Philadelphia|Rockets Hockey Club White|Ashburn Xtreme 2009|Metro Militia|Delaware Ducks 13U AA|Royals 2009|Philadelphia Blazers
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|North Jersey Avalanche|--| 50%| 53%| 69%| 71%| 73%| 86%| 91%| 92%| 94%| 95%| 97%| 98%| 98%| 99%
|MYHA 14U UA Gold| 50%|--| 53%| 69%| 71%| 73%| 86%| 91%| 91%| 94%| 95%| 97%| 98%| 98%| 99%
|Igloo Jaguars| 47%| 47%|--| 67%| 68%| 71%| 84%| 90%| 90%| 93%| 95%| 97%| 97%| 98%| 98%
|Rockets Hockey Club Black| 31%| 31%| 33%|--| 52%| 54%| 73%| 82%| 83%| 88%| 90%| 94%| 95%| 96%| 97%
|Lehigh Valley Phantoms| 29%| 29%| 32%| 48%|--| 53%| 72%| 81%| 82%| 87%| 89%| 94%| 94%| 95%| 97%
|NJ Stars| 27%| 27%| 29%| 46%| 47%|--| 69%| 80%| 80%| 85%| 88%| 93%| 94%| 95%| 96%
|Long Island Rebels| 14%| 14%| 16%| 27%| 28%| 31%|--| 63%| 64%| 72%| 77%| 85%| 87%| 89%| 92%
|Valley Forge Colonials 13U AA|  9%|  9%| 10%| 18%| 19%| 20%| 37%|--| 50%| 60%| 66%| 77%| 79%| 82%| 87%
|Team Philadelphia|  8%|  9%| 10%| 17%| 18%| 20%| 36%| 50%|--| 60%| 66%| 77%| 79%| 82%| 86%
|Rockets Hockey Club White|  6%|  6%|  7%| 12%| 13%| 15%| 28%| 40%| 40%|--| 56%| 69%| 72%| 76%| 81%
|Ashburn Xtreme 2009|  5%|  5%|  5%| 10%| 11%| 12%| 23%| 34%| 34%| 44%|--| 63%| 66%| 71%| 77%
|Metro Militia|  3%|  3%|  3%|  6%|  6%|  7%| 15%| 23%| 23%| 31%| 37%|--| 53%| 58%| 66%
|Delaware Ducks 13U AA|  2%|  2%|  3%|  5%|  6%|  6%| 13%| 21%| 21%| 28%| 34%| 47%|--| 56%| 63%
|Royals 2009|  2%|  2%|  2%|  4%|  5%|  5%| 11%| 18%| 18%| 24%| 29%| 42%| 44%|--| 58%
|Philadelphia Blazers|  1%|  1%|  2%|  3%|  3%|  4%|  8%| 13%| 14%| 19%| 23%| 34%| 37%| 42%|--

## Generation Details

Generated with command line:
```
./ahf.py update
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-27 |
| End Date | 2023-02-12 |
| Max Iterations | 200 |
| Max Ratings Diff | 1e-05 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.85 |
| Fake Ties | 1 |
| Ignore teams | __KRACH_FAKE_TEAM__ |
| Min Games Played | 12 |

