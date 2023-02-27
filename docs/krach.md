[<- Back](../readme.md)

# KRACH

KRACH is a ratings system used to rank competetive teams, specifically where all teams do not play equal schedules against each other. It was originally developed for college ice hockey, but can be applied to other sports as well. At a high-level, it's the win-loss ratio of a team, times the strength of schedule. See http://elynah.com/tbrw/tbrw.cgi?krach for more details.

KRACH is based on the [Bradley-Terry Model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model).  The basic algorithm to calculate the rating of a team is:

```
  P'i = Wi / ( ∑j ((Wij + Wji) / (Pi + Pj)) )

Where:
  P'i : New rating for i
  Pi  : Current rating for i
  Pj  : Current rating for j
  Wi  : Total wins (or 'win points') by i
  Wij : Number of wins for team i against j
  Wji : Number of wins for team j against i
```

The algorithm is recursive, in that in order to calculate the KRACH rating of a team, you need the KRACH rating of every other team.  To deal with this, the algorithm starts by assigning all teams the same default rating.  This is used to calculate the first set of new ratings which are normalized then fed back into the algorithm.  This is repeated until the results converge on the 'final' set of ratings.

KRACH replaces the Bradley-Terry model's binary view of wins vs losses with "win points" and "loss points" where:

```
winPoints  = wins + 0.5 * ties
lossPoints = losses + 0.5 * ties
```

These days, games may also be won/loss in overtime or a shootout. Different leagues may decide to weigh these differently, and `krach.py` has options for tweaking these values.

## Undefeated Teams

One weak point in the KRACH algorithm is around undefeated teams, which cause infinite KRACH ratings.

The _Dealing with Perfection_ section at http://elynah.com/tbrw/tbrw.cgi?krach discusses this problem. One solution is to use a fake team and pretend that it has tied every team:

> An older version of KRACH got around this by adding a "fictitious team" against which each team was assumed to have played and tied one game, which was enough to make everyone's KRACH finite. However, this had the disadvantage that it could still effect the ratings even when it was no longer needed to avoid infinities.

In contrast, http://dbaker.50webs.com/method.html suggests using 3 fictional ties per team:

> Prior to the 2011 football season, I used only one such tie game, but this tended to predict unrealistically high win percentages for unbeaten teams. The change to three fictional games tends to push down teams who have mediocre records against great schedules, as compressing the rating scale in this manner weakens more of their opponents' ratings than it improves. This mitigates one of the main criticisms of KRACH (which no longer uses the fictional game at all): a team can get to a fairly high rank purely by being in a tough conference, even if they do very poorly. This is exacerbated by the high percentage of games in conference in hockey (about 80%, compared to 65% for football or basketball).

As indicated by both sites, KRACH no longer uses the "fake" tie method. While researching for this tool, I couldn't find what is used instead.  At best, I found http://elynah.com/tbrw/tbrw.cgi?krach:

> The current version of KRACH does not include this "fictitious team", but rather checks to see if any ratios of ratings will end up needing to be infinite to produce the correct expected winning percentages. The key turns out to be related to the old game of trying to prove that the last-place team is better than the first-place team because they beat someone who beat someone who beat someone who beat the champions. If you can take any two teams and make a chain of wins or ties from one to the other, then all of the KRACH ratings will be finite.
> 
> If that's not the case, you need to work out the relationships teams have to each other. ....

`krach.py` has support for fake ties, but otherwise does not have any special handling for undefeated teams.

## Scaling

The KRACH algorithm outputs ratings that are small floating point numbers, which are then scaled up to integer values for human readability.  Different methods can be used for the scaling, and which is "best" comes down to the context they are being used in.  See `ScaleMethod` in `krach.py` for the available scaling methods.
