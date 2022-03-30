import numpy as np

def MSE(pred, target):
    return np.mean(np.abs(pred - target))