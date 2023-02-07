#!/bin/bash
# wrapper around 'refresh.sh' with AHF-specific settings

./refresh.sh \
	--iterations     10 \
	--shootout-win  0.5 \
	--tie           0.5 \
	--min-games      12 \
	${@}

