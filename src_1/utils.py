from typing import List
import pandas as pd
import numpy as np
from .predictor import LinearModel
from .metric import *
from math import sqrt

def correlation_of_two_variables(x: np.array, y: np.array) -> float:
    if x.shape != y.shape:
        return None
    
    n = x.shape[0]
    x_sum, y_sum, xy_sum, x_square_sum, y_square_sum = 0, 0, 0, 0, 0
    
    for i in range (0, n):
        x_sum += x[i]
        y_sum += y[i]
        xy_sum += x[i] * y[i]
        x_square_sum += x[i] * x[i]
        y_square_sum += y[i] * y[i]

    return (n * xy_sum - x_sum * y_sum) / (sqrt(n * x_square_sum - x_sum * x_sum) * sqrt(n * y_square_sum - y_sum * y_sum))

def check_if_column_nan(array: np.array) -> bool:
    return np.count_nonzero(np.isnan(array)) == array.shape[0]

def extract_features(df: pd.DataFrame, features: List[str]) -> np.array:
    '''
        Extract features from dataframe to numpy array
    '''
    feature_data =  df[features].to_numpy().T
    for idx, feature in enumerate(features):
        print(f'[*] {feature}: [type] {feature_data[idx].dtype} [nan] {np.count_nonzero(np.isnan(feature_data))}')
    return feature_data.T

def train(input: np.array, target: np.array) -> LinearModel:
    linear_model = LinearModel()
    linear_model.calc_weight(input, target)
    evaluate(linear_model, input, target)
    return linear_model

def evaluate(model: LinearModel, input: np.array, target: np.array) -> None:
    pred = model.predict(input)
    print('\t[*] MAE error:', MAE(pred, target.T))
    print('\t[*] RMSE error:', RMSE(pred, target.T))