#!/usr/bin/env python3

import logging

import blackbear_common as bb
import commands

#----------------------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args = commands.parseCommandLine()
    args.func(args, bb.AHF_SeasonId, bb.League.AHF)