from src_1.predictor import LinearModel
import pandas as pd
import numpy as np

def test_linear_regression():
    # TODO: @Do, also update a unit-test for linear model
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
    dfi = df.copy()
    for i in ['TMIN', 'TMAX', 'TAVG']:
        dfi.pop(i)

    weight = model.calc_weight(dfi, df['TMIN'])
    print(weight)
    print(model.predict(np.array([[24, 30.15, 36]], dtype = np.int64)))