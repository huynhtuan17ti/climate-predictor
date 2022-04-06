from src_1.metric import MAE
import numpy as np

def test_MAE():
    pred = np.array([1, 1, 0, 0, 5])
    target = np.array([1, 1, 2, -1, 3])

    assert MAE(pred, target) == 1