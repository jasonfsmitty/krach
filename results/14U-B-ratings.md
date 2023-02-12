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
|MYHA 14U B Blue|--|54.4|70.8|75.3|86.1|86.9|88.1|95.8|96.7|97.0|97.1|97.3|97.3|98.1|99.0|99.0
|Ashburn Xtreme|45.6|--|67.1|71.9|83.9|84.7|86.1|95.0|96.1|96.5|96.5|96.8|96.8|97.8|98.8|98.8
|Frederick Freeze|29.2|32.9|--|55.7|71.9|73.2|75.2|90.4|92.3|93.1|93.2|93.6|93.6|95.6|97.5|97.5
|Team Philadelphia|24.7|28.1|44.3|--|67.0|68.5|70.7|88.2|90.5|91.5|91.6|92.1|92.1|94.5|96.9|96.9
|Wissahickon Warriors|13.9|16.1|28.1|33.0|--|51.6|54.3|78.6|82.4|84.1|84.2|85.2|85.2|89.4|93.8|93.9
|Palmyra Black Knights|13.1|15.3|26.8|31.5|48.4|--|52.7|77.5|81.5|83.2|83.3|84.3|84.3|88.8|93.4|93.5
|Grundy Senators|11.9|13.9|24.8|29.3|45.7|47.3|--|75.6|79.8|81.6|81.8|82.9|82.8|87.7|92.7|92.8
|Maryland Jr Black Bears|4.2|5.0|9.6|11.8|21.4|22.5|24.4|--|56.1|58.9|59.2|60.9|60.9|69.6|80.5|80.7
|North Jersey Skylands Kings|3.3|3.9|7.7|9.5|17.6|18.5|20.2|43.9|--|52.9|53.2|55.0|55.0|64.3|76.4|76.7
|Igloo Jaguars|3.0|3.5|6.9|8.5|15.9|16.8|18.4|41.1|47.1|--|50.2|52.1|52.0|61.5|74.2|74.5
|North Jersey Sportscare Kings|2.9|3.5|6.8|8.4|15.8|16.7|18.2|40.8|46.8|49.8|--|51.8|51.8|61.3|74.0|74.3
|Lehigh Valley Phantoms|2.7|3.2|6.4|7.9|14.8|15.7|17.1|39.1|45.0|47.9|48.2|--|50.0|59.5|72.6|72.9
|Hollydell Hurricanes|2.7|3.2|6.4|7.9|14.8|15.7|17.2|39.1|45.0|48.0|48.2|50.0|--|59.6|72.6|72.9
|Royals White|1.9|2.2|4.4|5.5|10.6|11.2|12.3|30.4|35.7|38.5|38.7|40.5|40.4|--|64.3|64.6
|Jersey Shore Wildcats|1.0|1.2|2.5|3.1|6.2|6.6|7.3|19.5|23.6|25.8|26.0|27.4|27.4|35.7|--|50.4
|NJ Bandits|1.0|1.2|2.5|3.1|6.1|6.5|7.2|19.3|23.3|25.5|25.7|27.1|27.1|35.4|49.6|--

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

