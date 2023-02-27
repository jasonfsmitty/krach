[<- Back](../readme.md)

# AHF

This page covers the AHF-specific tweaks to the KRACH algorithm.

My code was originally written over the 2022 holiday break, using trial and error to best match the AHF rankings.  Eventually in Feb 2023 the AHF release details about their algorithm, and this tool has been updated accordingly.

## AHF Customizations to KRACH

THe AHF has an [explainer page](https://atlantichockeyfederation.com/krach-explained/) to describe how it applies the KRACH algorithm. The main takeaways are:
- Shootouts treated as normal win/loss (no partial credit).
- 200 max iterations.
- Single fake tie used to "regularize" the rankings.
  - Fake tie has a value of 0.85 per team.
- Scale to final ratings by multiplying by 10,000.

## AHF Source Code

The [explainer page](https://atlantichockeyfederation.com/krach-explained/) does not share the actual source code, but it does link to https://github.com/bjlkeng/Bradley-Terry-Model, implying it is the basis for their code.

I created a fork at https://github.com/jasonfsmitty/Bradley-Terry-Model, then modified it to use the parameters stated by the AHF.  It produces the same results as this tool.
