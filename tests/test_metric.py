from src_1.metric import MSE
import numpy as np

def test_MSE():
    pred = np.array([1, 1, 0, 0, 5])
    target = np.array([1, 1, 2, -1, 3])

    assert MSE(pred, target) == 1