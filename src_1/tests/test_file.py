import os

def test_data():
    assert os.path.exists('data/train.csv')
    assert os.path.exists('data/test.csv')