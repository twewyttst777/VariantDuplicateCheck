import vcf
import pandas as pd
import os.path
import csv
import re, sys
import argparse

def check_positions():
    df = pd.read_csv('out.csv', index_col = 0)

    df.drop('05_T6', axis=1, inplace=True)
    df.drop('06_T6', axis=1, inplace=True)
    df.drop('12_T2', axis=1, inplace=True)

    out_df = pd.DataFrame(index=df.index)

    for i in range(1, 31):
        oi = "{:02d}".format(i)
        exists = False
        for col in df:
            if col.startswith(oi):
                exists = True

        if exists:
            try: 
                cols = df.loc[:, df.columns.str.startswith(oi)]
                cols[oi] = (~cols).all(axis=1)

                out_df[oi] = ~(cols[oi])

            except Exception as e:
                print(str(e))
                pass 

    out_df.to_csv('outyn.csv')


     


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    args = parser.parse_args()


    check_positions()
