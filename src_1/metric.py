import numpy as np

def MAE(pred, target):
    return np.mean(np.abs(pred - target))

def RMSE(pred, target):
    return np.sqrt(np.mean((pred - target)**2))