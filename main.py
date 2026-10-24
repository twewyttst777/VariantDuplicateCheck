import vcf
import pandas as pd
import os.path
import csv
import re, sys
import argparse

def ready_positions(filename):
    positions = set() 
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            positions.add(row['pos'])
    return positions

def check_positions(filename, positions_file, name):
    vcf_reader = vcf.Reader(filename=filename)
    positions = ready_positions(positions_file)
    try:
        df = pd.read_csv('out.csv', index_col = 0)
    except:
        df = pd.read_csv(positions_file, index_col = 0)

    df[name] = "FALSE"

    for record in vcf_reader:
        pos = record.POS
        chrm_pos = ':'.join([str(record.CHROM), str(record.POS)])

        if chrm_pos in positions:
            df.at[chrm_pos, name] = 'TRUE'
            print(chrm_pos)

    df.to_csv('out.csv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_file")
    parser.add_argument("-P", "--positions_file")
    parser.add_argument("-C", "--name")

    args = parser.parse_args()

    input_file = args.input_file
    positions_file = args.positions_file
    name = args.name

    check_positions(input_file, positions_file, name)
