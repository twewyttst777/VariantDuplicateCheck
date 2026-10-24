#!/bin/bash


for i in {01..30}
do
	(( 16<i && i<26)) && continue
	for j in {1..7}
	do
		(( 5<j && i != 12 )) && continue
		(( i == 12 && j == 2 )) && continue
		echo ${i}_T${j}
		bcftools view -R regions.csv /data4/TimothyOkitsu/freebayes_bgzip/${i}_T${j}.vcf.gz > filtered/${i}_T${j}.vcf
	done
done


