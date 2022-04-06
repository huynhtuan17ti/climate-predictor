from src_1.metric import MAPE
import numpy as np

def test_MAPE():
    pred = np.array([1, 1, 0, 0, 5])
    target = np.array([1, 1, 2, -1, 3])

    assert MAPE(pred, target) == 1