import pandas as pd

class FactorReturns:
    def __init__(self, loadings: pd.DataFrame):
        self.loadings = loadings

    def compute(self, returns: pd.DataFrame):
        f = returns.values @ self.loadings.values
        return pd.DataFrame(f, index=returns.index, columns=self.loadings.columns)