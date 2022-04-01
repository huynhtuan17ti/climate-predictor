from src_1.predictor import LinearModel
import pandas as pd
import numpy as np

def test_linear_regression():
    # TODO: @Do, also update a unit-test for linear model
    dfi = np.array([[1, 2, 3], 
                    [2.8, 4.2, 6], 
                    [3.12, 6, 9.1],
                    [4.5, 8.5, 12],
                    [5.5, 10, 15],
                    [6.5, 12, 18],
                    [6.5, 12.3, 18],
                    [6.6, 12.2, 18],
                    [6.7, 11.9, 18]
                ])
    dfo = np.array([[4],[8],[12],[16],[20],[24], [24.1], [24.2], [24.01]])
    model = LinearModel()
    weight = model.calc_weight(dfi, dfo)
    print('weight: ', weight)
    print('predict for ', np.array([[6, 11, 19]]), '\nresult: ' ,model.predict(np.array([[6, 11, 19]], dtype = np.int64)))