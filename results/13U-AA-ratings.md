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
|MYHA 14U UA Gold|--|50.3|56.0|69.7|70.5|73.1|82.3|91.1|91.3|93.9|96.1|97.5|97.6|98.1|98.7
|North Jersey Avalanche|49.7|--|55.8|69.5|70.3|72.9|82.2|91.1|91.2|93.9|96.1|97.5|97.6|98.0|98.6
|Igloo Jaguars|44.0|44.2|--|64.4|65.3|68.1|78.5|89.0|89.1|92.4|95.1|96.9|97.0|97.5|98.3
|Rockets Hockey Club Black|30.3|30.5|35.6|--|51.0|54.1|66.9|81.7|81.9|87.1|91.5|94.5|94.7|95.6|97.0
|Lehigh Valley Phantoms|29.5|29.7|34.7|49.0|--|53.2|66.1|81.1|81.3|86.6|91.2|94.3|94.5|95.5|96.8
|NJ Stars|26.9|27.1|31.9|45.9|46.8|--|63.1|79.1|79.3|85.1|90.2|93.6|93.8|94.9|96.4
|Long Island Rebels|17.7|17.8|21.5|33.1|33.9|36.9|--|68.8|69.1|76.9|84.2|89.5|89.9|91.5|94.0
|Valley Forge Colonials 13U AA|8.9|8.9|11.0|18.3|18.9|20.9|31.2|--|50.3|60.1|70.8|79.4|80.1|83.0|87.7
|Team Philadelphia|8.7|8.8|10.9|18.1|18.7|20.7|30.9|49.7|--|59.8|70.5|79.2|79.9|82.8|87.6
|Rockets Hockey Club White|6.1|6.1|7.6|12.9|13.4|14.9|23.1|39.9|40.2|--|61.7|72.0|72.8|76.5|82.6
|Ashburn Xtreme 2009|3.9|3.9|4.9|8.5|8.8|9.8|15.8|29.2|29.5|38.3|--|61.5|62.4|66.9|74.7
|Metro Militia|2.5|2.5|3.1|5.5|5.7|6.4|10.5|20.6|20.8|28.0|38.5|--|51.0|55.8|64.9
|Delaware Ducks 13U AA|2.4|2.4|3.0|5.3|5.5|6.2|10.1|19.9|20.1|27.2|37.6|49.0|--|54.8|64.0
|Royals 2009|1.9|2.0|2.5|4.4|4.5|5.1|8.5|17.0|17.2|23.5|33.1|44.2|45.2|--|59.4
|Philadelphia Blazers|1.3|1.4|1.7|3.0|3.2|3.6|6.0|12.3|12.4|17.4|25.3|35.1|36.0|40.6|--

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

