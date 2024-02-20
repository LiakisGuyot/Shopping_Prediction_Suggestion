import pickle
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.pipeline import Pipeline

RANDOM_STATE = 1


def load(MODEL_FILENAME):
    try:
        with open(MODEL_FILENAME, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found")


def dataFromJson(data: dict):
    return pd.DataFrame(data, index=[0])


def predict(model: Pipeline, x):
    return model.predict(x)
