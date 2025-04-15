import pandas
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description='A simple program to replace a column row-wise with a dictionary. Don\'t need to be sorted', prog='trcol')
    parser.add_argument('-t', '--tcolumn', help='column name in the original table', required=True)
    parser.add_argument('table', help='original table to translate')
    parser.add_argument('dictionary', help='dictionary table to translate. The value to search in the original table must be in the first column')

    args = parser.parse_args()

    with open(args.dictionary) as dict_file:
        translate_dict = { l.strip().split('\t')[0]: l.strip().split('\t')[1] for l in dict_file}

    table_df = pandas.read_csv(args.table, sep=';')

    table_df[args.tcolumn] = table_df[args.tcolumn].apply(lambda s: "" if s not in translate_dict else translate_dict[s])
    table_df.to_csv(sys.stdout, sep='\t', index=False)
