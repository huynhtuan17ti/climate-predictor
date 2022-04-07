from ..predictor import LinearModel
import numpy as np
from ..utils import correlation_of_two_variables

def test_linear_regression():
    input = np.array([[1, 2, 3], 
                    [2.8, 4.2, 6], 
                    [3.12, 6, 9.1],
                    [4.5, 8.5, 12],
                    [5.5, 10, 15],
                    [6.5, 12, 18],
                    [6.5, 12.3, 18],
                    [6.6, 12.2, 18],
                    [6.7, 11.9, 18]
                ])
    target = np.array([[4],[8],[12],[16],[20],[24], [24.1], [24.2], [24.01]])
    model = LinearModel()
    weight = model.calc_weight(input, target)
    result = model.predict(np.array([[6, 11, 19]], dtype = np.int64))
    assert abs(result[0][0] - 25.074840) < 1e-4

def test_correlation_function():
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    b = a * 3 + 10
    b[0] += 0.001
    b[1] -= 0.01
    b[2] += 0.02
    assert abs(correlation_of_two_variables(a, b) - 0.999508) < 1e-4