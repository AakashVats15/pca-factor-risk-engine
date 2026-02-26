import pandas as pd
from pathlib import Path

class ReturnsLoader:
    def __init__(self, path):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"{self.path} not found")

        df = pd.read_csv(self.path, index_col=0, parse_dates=True)
        if df.empty:
            raise ValueError("returns file is empty")

        df = df.apply(pd.to_numeric, errors="coerce")
        df = df.dropna(how="all")
        df = df.fillna(method="ffill")

        if df.isna().any().any():
            df = df.fillna(0)

        return df