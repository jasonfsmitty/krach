# AHF KRACH Calculator

This tool was written to reproduce the KRACH rankings as provided by the [AHF (Atlantic Hockey Federation)](https://atlantichockeyfederation.com/).

**[Current AHF Rankings are available here.](results/readme.md)**

For information on KRACH itself, see the [KRACH Overview](docs/krach.md).

For information on the AHFs usage of KRACH, see the [AHF Overview](docs/ahf.md).

## Quick Start

```
# Download latest scores for all AHF divisions
./ahf.py download

# Generate all KRACH ratings, using AHF-specific settings:
./ahf.py update

# Alternatively, generate KRACH ratings for single division:
./ahf.py update -d "<division>"
```

## References

Collection of references found while working on this tool:
* [Atlantic Hockey Federation](https://atlantichockeyfederation.com/)
* [GameSheet Stats for AHF](https://gamesheetstats.com/seasons/1654/scores) - Basic UI to the underlying AHF score data; use browser developer mode to find REST API calls for reading divisions/scores.
* [Wikipedia page on Bradley-Terry Model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model)
* https://www.mscs.dal.ca/~butler/krachexp.htm - Original KRACH website by the Ken Butler; no longer online, but many other sources still refer back to it. [Wayback link](https://web.archive.org/web/20100217160456/http://www.mscs.dal.ca/~butler/krachexp.htm).
* http://elynah.com/tbrw/tbrw.cgi?krach - a comprehensive walkthrough of KRACH, and different algorithms that may be used.
* http://dbaker.50webs.com/method.html - another comprehensive walkthrough of KRACH
* [2022-2023 NCAA Women’s Hockey KRACH Calculator](https://www.bcinterruption.com/boston-college-bc-eagles-mens-womens-hockey-ranking-calculators/23433182/2022-2023-ncaa-womens-hockey-krach-calculator) - KRACH ratings implemented within Excel (via hidden worksheets).
* https://github.com/sezenack/Bradley-Terry-Sports-Model - Python implementation of KRACH that reads/writes to Excel spreadsheets. Initially tried modifying for AHF, but the algorithm used does not support undefeated teams. Between that, and other customizations for AHF, decided to start from scratch with this tool.
* https://github.com/bjlkeng/Bradley-Terry-Model - Python tool used as basis of AHF calculations.

