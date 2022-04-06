import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Convert csv to latex format')
parser.add_argument('--file', default=None, type=str, help='csv file')
args = parser.parse_args()

df = pd.read_csv(args.file)
print(df.to_latex())