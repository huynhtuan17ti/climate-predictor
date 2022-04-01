import pandas as pd
import numpy as np
import pickle

class LinearModel():
    '''
        TODO: @Do
        Ax = b => x = b*A^-1
        b: (TMIN, TMAX, TACG)
    '''

    def __init__(self):
        self.weight = np.array
        pass

    # dataframe just include features that in linear with TMIN, TMAX, TAVG
    def calc_weight(self, input: np.array, output: np.array):
        padding = np.array([[1] for i in range(0, input.shape[0])])
        array = np.append(input, padding, axis=1)
        # A.input = output -> A = inv(input_transpose x input) x input_transpose x output 
        self.weight = (np.linalg.inv(array.T.dot(array)).astype(np.float64)).dot(array.T).dot(output).T
        return self.weight

    def predict(self, features: np.array):
        x = np.array([np.append(features[0], 1)])
        return self.weight.dot(x.T)

    def save(self, pickle_file_name):
        with open(pickle_file_name, 'wb') as handle:
            pickle.dump(self.weight, handle, protocol = pickle.HIGHEST_PROTOCOL)

    def load(self, pickle_file_name):
        with open(pickle_file_name, 'rb') as handle:
            self.weight = pickle.load(handle)