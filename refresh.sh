#!/bin/bash

set -e

cd results/
for x in $(ls *.js | sort -n)
do
	echo "***********************************************************************"
	../krach.py ${@} ${x} | tee ${x//.js/}.txt
	[[ ${PIPESTATUS[0]} -ne 0 ]] && exit 1

	echo ""
done

