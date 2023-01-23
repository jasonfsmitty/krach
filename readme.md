# AHF KRACH Calculator

[Current Rankings](results/readme.md)

### Table of Contents

- **[Overview](#overview)**
  - **[Quick Start](#quick-start)**
- **[KRACH](#krach)**
- **[AHF](#ahf)**
- **[References](#references)**

## Overview

KRACH is a ratings system used to rank competetive teams, specifically where all teams do not play equal schedules against each other. It was originally developed for college ice hockey, but can be applied to other sports as well.

This tool was written to reproduce the KRACH rankings as provided by the [AHF (Atlantic Hockey Federation)](http://elynah.com/tbrw/tbrw.cgi?krach), but should be easily adaptable to other leagues.

### Quick Start

```
# Download latest scores for all AHF divisions
./get-scores.py

# Generate all KRACH ratings, using AHF-specific settings:
./ahf.sh

# Generate KRACH ratings for single division:
./krach.py [<options>...] <scores.js>
```

## KRACH

KRACH stands for Ken's Rating for American College Hockey and is commonly used to generate rankings in leagues where not all teams play each other an equal number of times. This includes schedules where teams may not play each other at all.  At a high-level, it's the win-loss ratio of a team, times the strength of schedule. See http://elynah.com/tbrw/tbrw.cgi?krach for more details.

KRACH is based on the [Bradley-Terry Model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model).  The basic algorithm to calculate the rating of a team is:

```
  P'i = Wi / ( ∑j Nij / (Pi + Pj) )

Where:
  P'i : New rating for i
  Pi  : Current rating for i
  Pj  : Current rating for j
  Wi  : Total wins (or 'win points') by i
  Nij : Number of times i and j have competed against each other.
```

The algorithm is recursive, in that in order to calculate the KRACH rating of a team, you need the KRACH rating of every other team.  To deal with this, the algorithm starts by assigning all teams the same default rating.  This is used to calculate the first set of new ratings which are normalized then fed back into the algorithm.  This is repeated until the results converge on the 'final' set of ratings.

KRACH replaces the Bradley-Terry model's simple view of wins vs losses with "win points" and "loss points" where:

```
winPoints  = wins + 0.5 * ties
lossPoints = losses + 0.5 * ties
```

These days, games may also end in an overtime win/loss or shoutout win/loss; Different leagues may decide to weigh these outcomes differently.

### Undefeated Teams

Some KRACH algorithms calculate ratings based on:

```
Ki = [ Vi / (Ni - Vi) ] * [ ∑j fij * Kj ]
```

Where `Ni - Vi` is referred to as the number of losses or rather "loss points" calculated by number of losses plus any partial credit for ties and overtime/shootout losses.  Using the above KRACH algorithm, an undefeated team would trigger a divide-by-zero error.

The _Dealing with Perfection_ section at http://elynah.com/tbrw/tbrw.cgi?krach discusses this problem. One solution is to use a fake team and pretend that it has tied every team:

> An older version of KRACH got around this by adding a "fictitious team" against which each team was assumed to have played and tied one game, which was enough to make everyone's KRACH finite. However, this had the disadvantage that it could still effect the ratings even when it was no longer needed to avoid infinities.

In contrast, http://dbaker.50webs.com/method.html suggests using 3 fictional ties per team:

> Prior to the 2011 football season, I used only one such tie game, but this tended to predict unrealistically high win percentages for unbeaten teams. The change to three fictional games tends to push down teams who have mediocre records against great schedules, as compressing the rating scale in this manner weakens more of their opponents' ratings than it improves. This mitigates one of the main criticisms of KRACH (which no longer uses the fictional game at all): a team can get to a fairly high rank purely by being in a tough conference, even if they do very poorly. This is exacerbated by the high percentage of games in conference in hockey (about 80%, compared to 65% for football or basketball).

As indicated by both sites, KRACH no longer uses the "fake" tie method. While researching for this tool, I couldn't find what is used instead.  At best, I found http://elynah.com/tbrw/tbrw.cgi?krach:

> The current version of KRACH does not include this "fictitious team", but rather checks to see if any ratios of ratings will end up needing to be infinite to produce the correct expected winning percentages. The key turns out to be related to the old game of trying to prove that the last-place team is better than the first-place team because they beat someone who beat someone who beat someone who beat the champions. If you can take any two teams and make a chain of wins or ties from one to the other, then all of the KRACH ratings will be finite.
> 
> If that's not the case, you need to work out the relationships teams have to each other. ....

The paragraph continues on, but honestly my mind has glazed over every time I read it. And having an alternative algorithm without the divide-by-zero risk means I never had to spend the time trying to fully absorb this section.

## AHF

For the most part, `krach.py` tries to be a general-purpose KRACH calculator. with all the knobs exposed as command line options.  This made it quick to try out different settings to more closely mimic the AHF rankings.  The `ahf.sh` wrapper will default to the settings that best match the AHF rankings.

The following sections discuss some unknowns about how AHF implements KRACH.

### Shootouts

The AHF website and KRACH documents do not detail how shootouts are weighted. I tried reaching out to the AHF, and according to the response I got back shootouts are treated as a normal win/loss, no partial credit for being tied through regulation.

However, if I run this tool with that setup (i.e. `--shootout-win 1.0 --shootout-loss 0.0`) the KRACH rankings that get generated are pretty far off from what the AHF publishes.  Through trial and error, this tool gets closest to the AHF results when it treats shootouts as a tie for both teams. Hence this is the default values in `krach.py` but can also be set via the command line with `--shootout-win 0.5 --shootout-loss l 0.5`.

### Handling Undefeated Teams

The algorithm implemented by `krach.py` does not have any divide-by-zero concerns; therefore it does not require using fake ties or other schemes to avoid risk of divide-by-zero.  For better comparison against algorithms that do, `krach.py` supports the `--fakes <N>` command line option; it will inject `<N>` fake ties per team.

I reached out to the AHF asking how they deal with undefeated teams in their KRACH calculations, and all they said was that they have their own method to deal with it.

### Part-Time Teams

Some teams in the AHF are part-time, and end up playing a significantly reduced schedule compared to the full-time teams.  This is another reason why a ranking system based on straight wins-losses would not be feasible.  KRACH treats the part-time teams just like any other team, and relies on the strength-of-schedule component to produce accurrate ratings.

In the AHF, part-time teams are treated identically to other teams - including being included in KRACH rankings and being eligible for playoffs.

### Showcase Teams

The AHF schedule includes multiple showcases throughout the season. A showcase is a weekend where all teams from the league converge on a single rink, and each team plays 4 games.  These games are normal regular season games, and count towards the regular season record, including KRACH ratings.

Showcases may incorporate team(s) that are not in the AHF, but play games in the showcase against AHF teams. For KRACH ratings, these showcase teams are treated like part-time teams, and the games are included in the KRACH calculations.  Unlike the official part-time teams, these showcase teams are not included in the KRACH rankings list, and these teams are not eligible for playoffs.

In `krach.py`, there are two ways to filter out the showcase teams:
* Explicitly list teams via the `--filter team1[,team2,team3...]` command line option.
* Drop teams that do not mean a minimum number of games played threshold via the `--min-games <N>` command line option.
Different divisions in the AHF have different showcase teams, and some showcase teams have been to 1-3 showcases, meaning their number of games played range from 4 to 12. When using `ahf.sh` (or `refresh.sh`) the `--min-games` option applies to all AHF divisions.

## References

Collection of references found while working on this tool; some used, some not:
* [Atlantic Hockey Federation](https://atlantichockeyfederation.com/)
* [GameSheet Stats for AHF](https://gamesheetstats.com/seasons/1654/scores) - Basic UI to the underlying AHF score data; use browser developer mode to find REST API calls for reading divisions/scores.
* [Wikipedia page on Bradley-Terry Model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model)
* https://www.mscs.dal.ca/~butler/krachexp.htm - Original KRACH website by the Ken Butler; no longer online, but many other sources still refer back to it. [Wayback link](https://web.archive.org/web/20100217160456/http://www.mscs.dal.ca/~butler/krachexp.htm).
* http://elynah.com/tbrw/tbrw.cgi?krach - a comprehensive walkthrough of KRACH, and different algorithms that may be used.
* http://dbaker.50webs.com/method.html - another comprehensive walkthrough of KRACH
* [2022-2023 NCAA Women’s Hockey KRACH Calculator](https://www.bcinterruption.com/boston-college-bc-eagles-mens-womens-hockey-ranking-calculators/23433182/2022-2023-ncaa-womens-hockey-krach-calculator) - KRACH ratings implemented within Excel (via hidden worksheets).
* https://github.com/sezenack/Bradley-Terry-Sports-Model - Python implementation of KRACH that reads/writes to Excel spreadsheets. Initially tried modifying for AHF, but the algorithm used does not support undefeated teams. Between that, and other customizations for AHF, decided to drop the fork and start from scratch with this tool.


