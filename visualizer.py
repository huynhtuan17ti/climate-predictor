import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(df):
    valid_columns = []
    for col in df.columns:
        if 'ATTRIBUTES' not in col and col not in ['TMIN', 'TMAX', 'TAVG'] and df[col].dtype == np.float64 and not df[col].isnull().sum() == len(df[col]):
            valid_columns.append(col)
    kwargs = {'data':df, 'line_kws':{"color": "red"}}
    for valid_col in valid_columns:
        fig, axes = plt.subplots(1, 3)
        fig.set_size_inches(25.5, 8.5)
        sns.regplot(ax=axes[0], x=valid_col, y="TMIN", **kwargs)
        sns.regplot(ax=axes[1], x=valid_col, y="TMAX", **kwargs)
        sns.regplot(ax=axes[2], x=valid_col, y="TAVG", **kwargs)
        fig.suptitle(valid_col, fontsize=20)

def plot_year(df, year):
    mask = (df['DATE'] >= f'{year}-01-01') & (df['DATE'] < f'{year+1}-01-01')
    _df = df.loc[mask]
    sns.lineplot(data=_df, x="DATE", y="TAVG")