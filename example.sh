#!/bin/bash


for FILE in [your_path]/*.vcf; 
do
	date -u
	PREFIX=${FILE%%.*}
	NOPATH="${PREFIX##*/}"
	[[ $NOPATH =~ _(T[0-9])_ ]]
	CRYPT="${i}_${BASH_REMATCH[1]}"
	echo $CRYPT
	FILE_FREEBAYES="${PREFIX}.freebayes_All.snpEff.vcf"
	python3 main.py -i $FILE_FREEBAYES -P long_ins_3880.csv -C $CRYPT 
done


