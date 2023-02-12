# 16U-A KRACH Rankings
Rank|KRACH|Subdivision|Team|GP|W|L|SOW|SOL|T|SoS|Exp Wins|Win Diff
---:|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:
1|1205|Championship|Lancaster Firebirds Black|36|29|3|4|0|0|253|30.9|-2.1
2|1194|Championship|Frederick Freeze|16|14|1|1|0|0|203|14.1|-0.9
3|1055|Championship|Southern Maryland Sabres 16U Gold|16|14|2|0|0|0|306|13.2|-0.8
4|753|Championship|Team Philadelphia Orange|35|25|6|4|0|0|237|28.0|-1.0
5|712|Gold|Ashburn Xtreme|16|13|3|0|0|0|269|12.5|-0.5
6|684|Gold|Wissahickon Warriors Red|36|28|4|1|3|0|310|28.0|-1.0
7|662|Gold|Delaware Ducks|36|29|4|1|2|0|200|29.2|-0.8
8|453|Gold|Frederick Freeze LA|16|13|2|0|1|0|160|12.9|-0.1
9|412|Silver|The St. James White|16|13|3|0|0|0|109|13.1|0.1
10|395|Silver|Wissahickon Warriors White|36|24|6|2|4|0|244|25.8|-0.2
11|373|Silver|MYHA 16U LA|16|9|4|2|1|0|287|10.9|-0.1
12|359|Silver|MYHA 16U UA|16|10|3|1|2|0|355|10.8|-0.2
13|226|Bronze|Igloo Jaguars Black|37|24|12|0|1|0|273|24.4|0.4
14|145|Bronze|Valley Forge Colonials 16U A Gold|36|19|15|0|2|0|329|19.4|0.4
15|139|Bronze|North Jersey Sportscare Kings|24|13|7|2|2|0|158|15.6|0.6
16|130|Bronze|Maryland Jr Black Bears White|16|5|7|3|1|0|297|8.2|0.2
17|120||Royals Gold|36|14|15|5|2|0|251|19.5|0.5
18|118||Valley Forge Colonials 16U A Silver|36|15|15|2|4|0|270|17.3|0.3
19|108||Lancaster Firebirds Orange|36|17|19|0|0|0|253|17.4|0.4
20|75||Maryland Jr Black Bears Red|16|5|9|1|1|0|334|6.1|0.1
21|74||Rockets Hockey Club|36|16|17|1|2|0|192|17.6|0.6
22|71||Haverford Hawks|36|13|20|2|1|0|307|15.4|0.4
23|64||Igloo Jaguars Green|35|11|20|3|1|0|232|14.4|0.4
24|62||Team Philadelphia Black|36|13|21|0|2|0|342|13.4|0.4
25|60||North Jersey Skylands Kings White|24|9|11|2|2|0|152|11.5|0.5
26|56||Philadelphia Blazers|35|11|22|1|1|0|282|12.3|0.3
27|50||Lehigh Valley Phantoms 1|36|9|20|4|3|0|285|13.4|0.4
28|46||Hollydell Hurricanes|35|8|24|2|1|0|276|10.2|0.2
29|41||Royals Blue|35|10|21|2|2|0|221|12.4|0.4
30|38||The St. James Navy|16|4|10|1|1|0|271|5.2|0.2
31|16||Grundy Senators|36|4|27|1|4|0|294|5.1|0.1
32|14||Lehigh Valley Phantoms 2|35|4|29|1|1|0|234|5.2|0.2
33|10||Jersey Shore Wildcats Red|16|1|14|1|0|0|151|2.1|0.1
34|9||Jersey Shore Wildcats Black|16|2|13|0|1|0|144|2.1|0.1
35|2||Capital City Vipers|35|1|34|0|0|0|322|1.0|0.0

## Actual vs Expected
Use the generated KRACH ratings to predict the expected win points per team, then compare that to the actual win points as a rough accuracy guage. Smaller is better.

||Absolute|Raw
|---:|---:|---:
|Total|14.90|-0.15
|Avg|0.43|-0.00

## Generation Details

Generated with command line:
```
../krach.py --iterations 10 --shootout-win 1.0 --tie 0.5 --min-games 12 -n 16U-A -o scores_16U-A.md scores_16U-A.json
```

| Option | Value |
| :----- | ----: |
| Start Date | 2022-08-20 |
| End Date | 2023-02-11 |
| KRACH Method | BRADLEY_TERRY |
| SoS Method | AVERAGE |
| Max Iterations | 10 |
| Max Ratings Diff | 0.0001 |
| Shootout Win Value | 1.00 |
| Shootout Loss Value | 0.00 |
| Tie Value | 0.50 |
| Fake Ties | 0 |
| Ignore teams |  |
| Min Games Played | 12 |
| Date Cutoff | 2023-02-12 |

