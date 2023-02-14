# AHF KRACH Calculator

[Current Rankings](results/readme.md)

**UPDATE 2023-02-14** - Per [this post from the AHF](https://atlantichockeyfederation.com/federation-krach-update/), their source code will be released this week. I will review and update this tool accordingly once it's available.

### Table of Contents

- **[Overview](#overview)**
  - **[Quick Start](#quick-start)**
- **[AHF](#ahf)**
- **[KRACH](#krach)**
- **[References](#references)**

## Overview

This tool was written to reproduce the KRACH rankings as provided by the [AHF (Atlantic Hockey Federation)](https://atlantichockeyfederation.com/).

KRACH is a ratings system used to rank competetive teams, specifically where all teams do not play equal schedules against each other. It was originally developed for college ice hockey, but can be applied to other sports as well.

### Quick Start

For those who want to play with the code:

```
# Download latest scores for all AHF divisions
./get-scores.py
# Generate all KRACH ratings, using AHF-specific settings:
./refresh.sh

# Alternatively, generate KRACH ratings for single division:
./ahf.py [<options>...] <scores.json>
```

## AHF

For the most part, the code tries to be a general-purpose KRACH calculator. with various knobs to tweak things for specific contexts.  The `ahf.py` wrapper will default to the settings that I believe best matches the AHF rankings, but I have not been able to recreate their exact numbers.

The following sections discuss some factors about how AHF implements KRACH.

### Shootouts

In January 2023, I reached out to the AHF and they indicated that shootouts were treated as a normal win-loss for each team. However, running with that option produced results that were at odds with what the AHF was publishing.  The only way to get results close to the AHF ratings was if shootouts were treated as a tie for both teams.

Fast-forward to mid-February, when somehow the AHF discovered they really were treating shootouts as ties.  Rather than continue with this method for the last two weeks of the season, they changed the algorithm to match the original intent.

This tool has been updated to match, treating shootouts as a regular win-loss.

### Handling Undefeated Teams

Undefeated teams can cause issues with some implementations, and so some code uses measures such as "fake" tie games to avoid these conditions (see [KRACH explainer](#krach) for more info).  This tool does not have any divide-by-zero concerns, and so does not have any special handling enabled (the tool supports adding fake ties, but does not do so when calculating the AHF ratings).

In January 2023, I reached out to the AHF and they indicated they have their own method to deal with it.

### Part-Time Teams

Some teams in the AHF are part-time, and end up playing a significantly reduced schedule compared to the full-time teams.  KRACH treats the part-time teams just like any other team, and relies on the strength-of-schedule component to produce accurrate ratings.

In the AHF, part-time teams are treated identically to other teams - including being included in KRACH rankings and being eligible for playoffs.

### Showcase Teams

The AHF schedule includes multiple showcases throughout the season. A showcase is a weekend where all teams from the league converge on a single rink, and each team plays 4 games.  These games are normal regular season games, and count towards the regular season record, including KRACH ratings.

Showcases may incorporate teams that are not in the AHF, but play games in the showcase against AHF teams. For KRACH ratings, these showcase teams are treated like part-time teams, and the games are included in the KRACH calculations.  Unlike the official part-time teams, these showcase teams are not included in the KRACH rankings list, and these teams are not eligible for playoffs.

This tool has two ways to filter out the showcase teams:
* Explicitly list teams in the `results/<division>-filter.txt` file, one team per line.
* Drop teams that do not mean a minimum number of games played threshold via the `--min-games <N>` command line option.
Different divisions in the AHF have different showcase teams, and some showcase teams have been to 1-3 showcases, meaning their number of games played range from 4 to 12. When using `ahf.sh` (or `refresh.sh`) the `--min-games` option applies to all AHF divisions.

In addition, some teams are not participating in playoffs, and they are also filtered out of the current KRACH standings.

### Max Iterations

As explained below, the KRACH algorithm takes an initial set of ratings as input to generate updated ratings. It then feeds those new ratings back into the algorithm over and over until the output ratings are the same as the inputs.

When trying to match the AHF numbers, this tool stops at 10 iterations, regardless of how close the input/outputs are.  This produces numbers "close" to the AHF, but that also have a relatively large margin of error.  See the "Win Diff" column for the error calculation; ideally with an accurate KRACH rating this would be 0.0.  Negative numbers indicate the KRACH rating is too low, and positive numbers indicate the rating is too high.

This doesn't necessarily mean the AHF numbers are wrong ... will revisit once they release their source code.

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

