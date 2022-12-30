#!/bin/bash
# wrapper around 'refresh.sh' with AHF-specific settings

./refresh.sh \
	--iterations 10 \
	--min-games  12 \
	${@}

