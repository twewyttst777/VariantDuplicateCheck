#!/bin/bash

cp chrPOS.csv out.csv

for i in {01..30}
do
	(( 16<i && i<26)) && continue
	for j in {1..7}
	do
		(( 5<j && i != 12 )) && continue
		echo ${i}_T${j}
		python3 main.py -i filtered/${i}_T${j}.vcf -P chrPOS.csv -C ${i}_T${j}
	done
done


