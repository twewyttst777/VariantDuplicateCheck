# Variant Duplicate Checker

Author: Timothy Okitsu
Lab: Chih-Lin Hsieh
Associated Study:

## Overview

This Python script tabulates instances of specified variants over a set of VCFs.

## Usage

To add a new column to the table containing matched variants in VCF file FILE_ID.vcf,

```bash
	python3 main.py -i FILE_ID.vcf -P list.csv -C ID
```

list.csv must be formatted with header line "pos", followed by CHR:POS individual lines, as below:
```
pos
chr1:1
chr2:1
chr2:2
```

etc.

### Individual Uniqueness

Additional script 'yn.py' creates a secondary csv 'outyn.csv' that identifies if a variant shows up at least once per individual. 'ID' from before must start with a two-digit identifier of each individual. To create 'outyn.csv',

```bash
	python3 yn.py
```

## Output

Output table 'out.csv' is a comma separated list where the y-axis is the CHR:POS of variants in 'list.csv' and the x-axis is the ID of a given file. A cel is True if a variant at CHR:POS appears in the file and False if it does not.

'outyn.csv' is a comma separated list where the y-axis is the CHR:POS of variants in 'list.csv' and the x-axis is individuals. A cel is True if a variant at CHR:POS appears at least once per individual.

## Installation

It is recommended to use a Python virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Required packages (as defined in `requirements.txt`) include:
- `PyVCF`
- `pandas`
- `numpy`

---

## Batch Processing

Included script 'example.sh' automates creation and population of the output table for a given directory of vcfs.

When possible, using bcftools view with a Region File to create a VCF containing only variants in list.csv before using this tool to create the True/False table will faster.

## Notes

Matching variants from a somatic caller (like Mutect2 or Strelka2) to FreeBayes can be challenging due to differences in variant representation, calling logic, and filtering thresholds. Somatic callers are designed to detect low-frequency mutations and typically operate in tumor-normal pair mode, applying aggressive filters for artifacts and strand bias, while FreeBayes is a haplotype-based germline caller that emits variants based on population-level evidence and may report sites even if the variant is not called in the tumor sample (i.e., GT=0/0). Additionally, indels and complex variants may be left-aligned differently or split/merged in inconsistent ways across tools, making direct position-based comparison error-prone.

 

---

 

## License

This tool is licensed for academic and research use only.

© 2025 Timothy Okitsu and Chih-Lin Hsieh
