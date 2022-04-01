import pandas as pd
import numpy as np
import pickle

class LinearModel():
    '''
        Ax = b => x = b*A^-1
        b: only one feature
    '''

    def __init__(self):
        # TODO: each model [TMIN, TMAX, TAVG] should have a specific weight
        self.weight = np.array
        # 0: for TMIN
        # 1: for TMAX
        # 2: for TAVG
        pass

    # dataframe just include features that in linear with TMIN, TMAX, TAVG
    def calc_weight(self, df: pd.DataFrame):
        # TODO: @Do, the format
        '''
            input: np.ndarray (x)
            output: np.ndarray (b)
        '''
        (y_tmin, y_tmax, y_tavg) = (df['TMIN'].to_numpy(), df['TMAX'].to_numpy(), df['TAVG'].to_numpy())
        for s in ['TMIN', 'TMAX', 'TAVG']:
            df.pop(s)
        df['padding'] = [1 for i in range(0, df.shape[0])]
        array = df.to_numpy()
        res = (np.linalg.inv(array.T.dot(array)).astype(np.float64)).dot(array.T)
        self.weight = np.array([res.dot(y_tmin), res.dot(y_tmax), res.dot(y_tavg)])
        return self.weight

    def predict(self, features):
        x = np.append(features[0], 1)
        return self.weight.dot(x.T)

    def save(self, pickle_file_name):
        with open(pickle_file_name, 'wb') as handle:
            pickle.dump(self.weight, handle, protocol=pickle.HIGHEST_PROTOCOL)
        pass

    def load(self, pickle_file_name):
        with open(pickle_file_name, 'rb') as handle:
            self.weight = pickle.load(handle)