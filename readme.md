# AHF KRACH Calculator

[Current Rankings](results/readme.md)

### Table of Contents

- **[Overview](#overview)**
  - **[Quick Start](#quick-start)**
- **[KRACH](#krach)**
- **[AHF](#ahf)**

## Overview

KRACH is a ratings system used to rank competetive teams, specifically where all teams do not play equal schedules against each other. It was originally developed for college ice hockey, but can be applied to other sports as well.

This tool was written to reproduce the KRACH rankings as provided by the [AHF (Atlantic Hockey Federation)](http://elynah.com/tbrw/tbrw.cgi?krach), but should be easily adaptable to other leagues.

### Quick Start

```
# Download latest scores for all AHF divisions
./get-scores.py

# Regenerate KRACH ratings, using AHF-specific settings:
./ahf.sh
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

### Divergance from Bradley-Terry Model

KRACH takes into account tie games, something the Bradley-Terry model did not. In short, tie games give each team half a point.  These days it's a little more complicated; depending on the league, games may end in a tie, an overtime win/loss, or a shootout win/loss. Typically any game that is tied at the end of regulation and requires overtime/shootout wil give full credit to the winner, and partial credit to the loser.

The other difference with KRACH is that it calculates a Strength-of-Schedule for each team; this is the weighted average of the KRACH ratings for all games played by the team.  This weighted factor is already accounted for in the Bradley-Terry algorith, KRACH just extracts it out as another metric to be displayed.

### Undefeated Teams

Some KRACH algorithms calculate ratings based on:
```
Ki = [Vi/(Ni-Vi)] * [∑jfij*Kj]
```

Where `Ni - Vi` is referred to as the number of losses, or rather "loss points" calculated by number of losses, plus any partial credit for ties and overtime/shootout losses.  Using this algorithm, an undefeated team would trigger a divide-by-zero error.

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

For the most part, `krach.py` tries to be a general-purpose KRACH calculator. with all the knobs exposed as command line options.  This let me easily try different settings to more closely mimic the AHF rankings.  The `ahf.sh` wrapper will default to the settings that best match the AHF rankings.

Outstanding questions about the AHF implementation of KRACH:
- How much credit is given to shootout wins and losses?
- Any special logic for undefeated teams, such as adding 'fake' tie games?
- How are showcase teams handled?

The following sections attempt to answer these questions based on trial and error.

### Shootouts

The AHF website and KRACH documents do not detail how shootouts are weighted.  One method might be to ignore the fact that it was a shootout at all, and treat it as a normal win/loss with full or zero credit as appropriate.  Or there could be any varying levels of full/partial credit to either team.

As best I can tell through trial and error, shootouts are treated as a tie, and both teams receive half a point.  These are the default values in `krach.py` but can also be set via the commandline with `-w 0.5 -l 0.5`.

### Handling Undefeated Teams

The KRACH algorithm as implemented by `krach.py` does not have any divide-by-zero concerns, and hence does not need any special handling to deal with undefeated teams (such as the fake tie games discussed earlier).  If I find out the AHF does use fake ties, it would be easy to add into `krach.py`.

### Part-Time Teams

Some teams in the AHF are part-time, and end up playing a significantly reduced schedule compared to the full-time teams.  This is another reason why a ranking system based on straight wins-losses would not be feasible.  KRACH treats the part-time teams just like any other team, and relies on the strength-of-schedule component to produce accurrate ratings.

Other than the reduced schedule, part-time teams are treated identically to other teams, and are eligible for playoffs.

### Showcase Teams

The AHF schedule includes multiple showcases throughout the season. A showcase is a weekend where all teams from the league converge on a single rink, and each team plays 4 games.  These games are normal regular season games, and count towards the regular season record, including KRACH ratings.

Sometimes, showcases incorporate a team that isn't in our league at all; these teams are only in town to play 4 games in the showcase, and then our league will never see them again.

What's odd about this, is that the games are still treated as regular season games, and still count towards the KRACH ratings. You can see these teams in the raw standings for the league, but these showcase teams are not eligible for playoffs.  While they are part of the KRACH ratings calculations, these teams are stripped from the final rankings.

There are two ways to filter out the showcase teams; the first is to explicitly list each team name on the command line using `--filter team1[,team2,team3,...]`.  Since each division has a unique set of showcase teams, this method doesn't scale well.  Instead, you can rely on the fact that these teams play even less games than the part-time teams, and use the minimum number of games option to filter them out: `--min games <N>`.

