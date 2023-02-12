# 15U-AA KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|5053|Championship|Delaware Ducks|42|33|5|3|1|0|1634|34.8|-1.2
2|2802|Championship|MYHA 16U AA Gold|16|10|3|1|2|0|3359|10.7|-0.3
3|2332|Championship|Team Philadelphia|40|24|10|4|2|0|2083|27.8|-0.2
4|1545|Championship|Long Island Rebels|20|7|10|3|0|0|3622|9.9|-0.1
5|1475||Royals|40|22|11|3|4|0|2408|25.3|0.3
6|238||NJ Bandits|34|11|19|1|3|0|1978|12.9|0.9
7|165||Palmyra Black Knights|40|10|25|1|4|0|2169|11.7|0.7
8|116||North Jersey Sportscare Kings Yellow|24|5|16|1|2|0|1091|6.5|0.5
9|61||Tomorrow's Ice Selects|39|1|33|3|2|0|1922|4.3|0.3

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|4.37|0.80
|Avg|0.49|0.09

## Predictions
Uses KRACH ratings to predict winning percentage of each team (row) against each opponent (column).
||Delaware Ducks|MYHA 16U AA Gold|Team Philadelphia|Long Island Rebels|Royals|NJ Bandits|Palmyra Black Knights|North Jersey Sportscare Kings Yellow|Tomorrow's Ice Selects
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: 
|Delaware Ducks|--|64.3|68.4|76.6|77.4|95.5|96.8|97.8|98.8
|MYHA 16U AA Gold|35.7|--|54.6|64.5|65.5|92.2|94.4|96.0|97.9
|Team Philadelphia|31.6|45.4|--|60.2|61.3|90.7|93.4|95.3|97.5
|Long Island Rebels|23.4|35.5|39.8|--|51.2|86.6|90.3|93.0|96.2
|Royals|22.6|34.5|38.7|48.8|--|86.1|89.9|92.7|96.0
|NJ Bandits|4.5|7.8|9.3|13.4|13.9|--|59.0|67.3|79.7
|Palmyra Black Knights|3.2|5.6|6.6|9.7|10.1|41.0|--|58.8|73.2
|North Jersey Sportscare Kings Yellow|2.2|4.0|4.7|7.0|7.3|32.7|41.2|--|65.6
|Tomorrow's Ice Selects|1.2|2.1|2.5|3.8|4.0|20.3|26.8|34.4|--

## Generation Details

Generated with command line:
```
../ahf.py -f 15U-AA-filter.txt -n 15U-AA -o 15U-AA-ratings.md 15U-AA-scores.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-19 |
| End Date | 2023-02-11 |
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

