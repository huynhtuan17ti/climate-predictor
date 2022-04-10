from statistics import mode
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from typing import List
import pandas as pd
import matplotlib.ticker as ticker


def describe_data(df: pd.DataFrame, start_year: int, end_year: int):
    mask = (df['DATE'] >= f'{start_year}-01-01') & (df['DATE'] < f'{end_year+1}-01-01')
    _df = df.loc[mask]
    print(_df[['TAVG']].mode())
    return _df[['TAVG']].describe()

def plot_year(df: pd.DataFrame, start_year: int, end_year: int, file_name: str):
    mask = (df['DATE'] >= f'{start_year}-01-01') & (df['DATE'] < f'{end_year+1}-01-01')
    _df = df.loc[mask]
    fig, ax = plt.subplots(figsize=(30, 10))
    sns.lineplot(ax=ax, data = _df,  y="TAVG", x="DATE")
    start, end = ax.get_xlim()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation = 45)

def scatterplot_year(df: pd.DataFrame, start_year: int, end_year: int, file_name: str):
    mask = (df['DATE'] >= f'{start_year}-01-01') & (df['DATE'] < f'{end_year+1}-01-01')
    _df = df.loc[mask]
    fig, ax = plt.subplots(figsize=(30, 10))
    sns.scatterplot(ax=ax, data = _df,  y="TAVG", x="DATE")
    start, end = ax.get_xlim()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation = 45)
 
