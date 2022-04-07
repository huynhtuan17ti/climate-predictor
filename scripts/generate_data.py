import pandas as pd
import numpy as np
import os

DATA_PATH = 'data/gsom/gsom-latest'
data_dir = sorted(os.listdir(DATA_PATH))
print("[*] Number of data:", len(data_dir))

USC_data = []
data_dict = {}
for csv_file in data_dir:
    station = csv_file[:3]
    if station not in data_dict:
        data_dict[station] = 1
    else:
        data_dict[station] += 1
    if 'USC' in csv_file:
        USC_data.append(os.path.join(DATA_PATH, csv_file))

print('[*] Data length:', len(USC_data))

USC_data = USC_data[-500:]
df = pd.concat(map(pd.read_csv, USC_data), ignore_index=True)
print('[*] Raw dataframe:', len(df))
df.dropna(subset=['TMIN', 'TMAX', 'TAVG'], inplace=True)
print('[*] Process dataframe:', len(df))
df = df[:20000]
df.to_csv('data/raw.csv', index=False)

# Deleting the rows/columns with missing data
missing_column = ['DYFG', 'DYFG', 'EVAP', 'WDMV', 'MNPN', 'MXPN', 'HN01', 'HX01', 'LN01', 'LX01', 'MN01', 'MX01', 'HN02', 'HX02', 'LN02', 'LX02', 'MN02', 'MX02']
df.drop(missing_column, axis=1, inplace=True)

# Fill with mean value
for col in df.columns:
    if 'ATTRIBUTES' in col:
        df.drop([col], axis=1, inplace=True)
        continue
    df[col].interpolate(method='bfill', inplace=True)
    df[col].interpolate(method='ffill', inplace=True)

# Convert to datetime format
df['DATE'] = df['DATE'].astype('datetime64[ns]')
df = df.sort_values(by='DATE', ascending=True)
print(df.info())

df[:15000].to_csv('data/train.csv', index=False)
df[15000:].to_csv('data/test.csv', index=False)