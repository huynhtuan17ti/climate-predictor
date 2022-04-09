from statistics import mode
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from typing import List
import pandas as pd
from src_1.predictor import LinearModel
from src_1.utils import *
import matplotlib.ticker as ticker

def plot_graph(df: pd.DataFrame):
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
 

def df_prediction(df: pd.DataFrame, feature_list: List[str], model_path: str):
    model = LinearModel()
    model.load(model_path)
    data = extract_features(df, feature_list)
    predict = model.predict(data)
    df['pred'] = predict
    return df

def plot_missingdata(df:pd.DataFrame, title:str, xlabel:str, ylabel:str):
    ''' This function takes a data frame as input plots the list of columns with corresponding total number of missing values'''
    # Let us see what columns have missing values
    # Total number of entries (rows X columns) in the dataset
    total= df.size
    #Number of missing values per column
    missingCount = df.isnull().sum()
    #Total number of missing values
    missing_tot = missingCount.sum()
    # Calculate percentage of missing values
    print("The dataset contains", round(((missing_tot/total) * 100), 2), "%", "missing values")

    # keeping only the columns with missing values>0 
    missing = missingCount[missingCount > 0] 
    print(missing)
    # sorting in order of missing values and making the change to original missing series
    missing.sort_values(inplace=True) 
    missing.plot.bar()
    plt.title(title, size=15,loc='left')
    plt.xticks(fontsize=11,rotation=45)
    plt.yticks(fontsize=11)
    plt.xlabel(xlabel, fontsize=13)
    plt.ylabel(ylabel, fontsize=13)
    plt.show()