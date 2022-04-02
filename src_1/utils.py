from typing import List
import pandas as pd
import numpy as np
from .predictor import LinearModel
from .metric import MSE

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
    print('[*] MSE error:', MSE(pred, target.T))