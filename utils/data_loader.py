import pandas as pd

DATA_PATH = "data/mock/aadhaar_operations.csv"

def load_operations_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    return df
