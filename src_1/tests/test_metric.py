from ..metric import MAE, RMSE
import numpy as np

def test_MAE():
    pred = np.array([1, 1, 0, 0, 5])
    target = np.array([1, 1, 2, -1, 3])
    assert MAE(pred, target) == 1

def test_RMSE():
    pred = np.array([1, 1, 0, 0, 5])
    target = np.array([1, -2, 2, -1, 3])
    assert abs(RMSE(pred, target) - 1.897366) < 1e-4 