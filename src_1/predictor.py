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
        # 0: for TMIN
        # 1: for TMAX
        # 2: for TAVG
        pass

    # dataframe just include features that in linear with TMIN, TMAX, TAVG
    def calc_weight(self, df: pd.DataFrame):
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

'''
df = pd.DataFrame([(1, 2, 3, 4, 5, 6), 
                    (2.8, 4.2, 6, 8, 10, 12), 
                    (3.12, 6, 9.1, 12, 15, 18),
                    (4.5, 8.5, 12, 16, 20, 24.12),
                    (5.5, 10, 15, 20.12, 25, 30),
                    (6.5, 12, 18, 24, 30.15, 36),
                    (6.5, 12.3, 18, 24, 30.15, 36),
                    (6.6, 12.2, 18, 24, 30.15, 36),
                    (6.7, 11.9, 18, 24, 30.15, 36)
                ], 
                columns = ('TMIN', 'TMAX', 'TAVG', 'x', 'y', 'z'))
model = LinearModel()
weight = model.calc_weight(df)
for line in weight:
    print(line)
print(model.predict(np.array([[24, 30.15, 36]], dtype = np.int64)))
'''
