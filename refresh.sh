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
	echo "| Division | Data Start | Data End |" >> ${README}
	echo "| :------- | :--------- | :------- |" >> ${README}
fi

for x in $(ls *.js | sort -n)
do
	bname=${x//.js/}
	output="${bname}.md"

	division=${bname}
	[[ $division =~ ^scores_(.*) ]] && division=${BASH_REMATCH[1]}

	echo "*** ${division} ***"
	../krach.py ${@} -n "${division}" -o ${output} ${x}
	[[ ${PIPESTATUS[0]} -ne 0 ]] && exit 1
	echo "" 

	if $ENABLE_DATE_RANGE
	then
		startdate="$(jq '."0_0"[-1]."games"[-1]."date"' ${x} | tr -d '"')"
		enddate="$(jq '."0_0"[0]."games"[0]."date"' ${x} | tr -d '"')"
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
