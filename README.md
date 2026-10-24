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

1	pos
2	chr1:1
3	chr2:1
4	chr2:2

etc.

## Output

Output table 'out.csv' is a comma separated list where the y-axis is the CHR:POS of variants in 'list.csv' and the x-axis is the ID of a given file. A cel is True if a variant at CHR:POS appears in the file and False if it does not.

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
