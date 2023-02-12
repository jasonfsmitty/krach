#!/bin/bash

set -e

cd results/
README="readme.md"
TIMESTAMP="$(date)"

ENABLE_DATE_RANGE=true

echo "# KRACH Ratings" > ${README}
echo "Click below to see KRACH ratings per each division." >> ${README}

if $ENABLE_DATE_RANGE
then
	echo "| Division | Season Start | Latest Game |" >> ${README}
	echo "| :------- | :--------- | :------- |" >> ${README}
fi

for x in $(ls *.json | sort -n)
do
	bname=${x//.json/}
	division=${bname}
	if [[ $division =~ ^(.*)-scores ]]
	then
		division=${BASH_REMATCH[1]}
	else
		echo "ERROR: failed to extract division: $bname"
		exit 1
	fi

	output="${division}-ratings.md"

	filterFile="${division}-filter.txt"
	[[ -f "${filterFile}" ]] || touch ${filterFile}
	filterOpts="-f ${filterFile}"

	echo "*** ${division} ***"
	../ahf.py ${@} ${filterOpts} -n "${division}" -o ${output} ${x}
	[[ ${PIPESTATUS[0]} -ne 0 ]] && exit 1
	echo "" 

	if $ENABLE_DATE_RANGE
	then
		startdate="$(jq '.[-1]."game"."date"' ${x} | tr -d '"')"
		enddate="$(jq '.[0]."game"."date"' ${x} | tr -d '"')"

		echo "| [${division}](${output}) | ${startdate} | ${enddate} |" >> ${README}
	else
		echo "* [${division}](${output})" >> ${README}
	fi
done

echo "" >> ${README}
echo "***" >> ${README}
echo "Generated on ${TIMESTAMP} using command line:" >> ${README}
echo "\`\`\`"    >> ${README}
echo "${0} ${@}" >> ${README}
echo "\`\`\`"    >> ${README}
echo "" >> ${README}
