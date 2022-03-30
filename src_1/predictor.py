import pandas as pd
import numpy as np
import pickle
from numpy.linalg import inv

class LinearModel():
    '''
        TODO: @Do
        Ax = b => x = b*A^-1
        b: (TMIN, TMAX, TACG)
    '''

    def __init__(self):
        self.weight = np.array
        # 0: for TMIN
        # 1: for TMAX
        # 2: for TAVG
        pass

    # dataframe just include features that in linear with TMIN, TMAX, TAVG
    def calc_weight(self, df: pd.DataFrame):
        n = len(df.columns)
        print('[*] Features: ' + str(n))
        self.weight = np.array([np.zeros(n + 1) for i in range (0, 3)])
        
        (y_tmin, y_tmax, y_tavg) = tuple(df['TMIN'], df['TMAX'], df['TAVG'])
        x_features = np.array
        for col in df.columns:
            if col not in ['TMIN', 'TMAX', 'TAVG']:
                x_features.append(df[col])

        data_len = len(df[0]) if len(df) != 0 else 0
        print('[*] rows')
        x_features.append([0 for i in range(0, data_len)])
        mul = np.multiply(inv(np.multiply(np.matrix.transpose(x_features), x_features)), np.matrix.transpose(x_features))
        
        self.weight[0] = np.multiply(mul, y_tmin)
        self.weight[1] = np.multiply(mul, y_tmax)
        self.weight[2] = np.multiply(mul, y_tavg)
    
    def predict(self, features: np.ndarray):
        features.append(1)
        return tuple(
            np.array.multiply(self.weight[0], np.matrix.transpose(features)),
            np.array.multiply(self.weight[1], np.matrix.transpose(features)),
            np.array.multiply(self.weight[2], np.matrix.transpose(features))
        )

    def save(self, pickle_file_name):
        with open(pickle_file_name, 'wb') as handle:
            pickle.dump(self.weight, handle, protocol=pickle.HIGHEST_PROTOCOL)
        pass

    def load(self, pickle_file_name):
        with open(pickle_file_name, 'rb') as handle:
            self.weight = pickle.load(handle)
