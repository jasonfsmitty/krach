#!/usr/bin/env python3

from enum import Enum

#----------------------------------------------------------------------------
# Hardcoded for 2023-24 season
AHF_SeasonId = 3659
AGHF_SeasonId = 3663
THF_SeasonId = 3664

#----------------------------------------------------------------------------
THF_DivisionsIgnore = {
	'THF West',
	'USPHL',
}

AHF_DivisionsIgnore = {'8U Beginner', '8U Intermediate', '8U Advanced'}

AGHF_DivisionsIgnore = {}

#----------------------------------------------------------------------------
# Default settings to mimic AHF results

DEFAULT_ITERATIONS     = 200
DEFAULT_MAX_DIFF       = 0.00001
DEFAULT_SHOOTOUT_VALUE = 1.0
DEFAULT_FAKES          = 1
DEFAULT_TIE_VALUE      = 0.85
DEFAULT_MIN_GAMES      = 4
DEFAULT_SCALE_FACTOR   = 10000

#----------------------------------------------------------------------------
class League(Enum):
    AHF = 1
    AGHF = 2
    THF = 3
    
def getSubDivision(league, numbertOfTeams, teamRank):
	NO_SUBDIVISION = ""
	match league:
		case League.AHF:
			# Only the top 4 teams of each subdivision compete in the playoffs;
			# THe AHF KRACH rankings list other teams as being in the lowest
			# subdivision, but this makes it clearer who is in/out of playoff
			# contention.

			SUBDIVISIONS = [
				'Championship',
				'Gold',
				'Silver',
				'Bronze',
			]

			if numbertOfTeams <= 10:
				if teamRank <=  4: return SUBDIVISIONS[0]
			elif numbertOfTeams >= 11 and numbertOfTeams <= 14:
				if teamRank <=  4: return SUBDIVISIONS[0]
				if teamRank <=  8: return SUBDIVISIONS[1]
			elif numbertOfTeams >= 15 and numbertOfTeams <= 26:
				if teamRank <=  4: return SUBDIVISIONS[0]
				if teamRank <=  8: return SUBDIVISIONS[1]
				if teamRank <= 12: return SUBDIVISIONS[2]
			else:
				if teamRank <=  4: return SUBDIVISIONS[0]
				if teamRank <=  8: return SUBDIVISIONS[1]
				if teamRank <= 12: return SUBDIVISIONS[2]
				if teamRank <= 16: return SUBDIVISIONS[3]
			return NO_SUBDIVISION
		case League.AGHF:
			SUBDIVISIONS = [
				'Playoffs',
			]

			if numbertOfTeams <= 9:
				if teamRank <=  4: return SUBDIVISIONS[0]
			elif numbertOfTeams >= 10:
				if teamRank <=  6: return SUBDIVISIONS[0]
			return NO_SUBDIVISION
		
		case League.THF:
			SUBDIVISIONS = [
				'Super 6',
				'Frozen 4',
			]

			if numbertOfTeams <= 9:
				if teamRank <=  4: return SUBDIVISIONS[1]
			elif numbertOfTeams >= 11:
				if teamRank <=  6: return SUBDIVISIONS[0]
				if teamRank >=  7 and teamRank <= 10: return SUBDIVISIONS[1]
				if teamRank > 10: return NO_SUBDIVISION
			return NO_SUBDIVISION
		case _:
			raise RuntimeError("Invalid league")

def getLeagueAbbreviation(league):
	match league:
		case League.AHF: return "AHF"
		case League.AGHF: return "AGHF"
		case League.THF: return "THF"
		case _:
			raise RuntimeError("Invalid league")
