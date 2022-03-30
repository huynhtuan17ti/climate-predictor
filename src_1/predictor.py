import pandas as pd
import numpy as np

class LinearModel():
    '''
        TODO: @Do
        Ax = b => x = b*A^-1
        b: (TMIN, TMAX, TACG)
    '''
    def __init__(self):
        self.weight = []
        pass

    def calc_weight(self, df: pd.DataFrame):
        pass
    
    def predict(self, features: np.ndarray):
        pass

    def save(self):
        # save model weight as pickle
        pass

    def load(self):
        # load model from pickle
        pass
