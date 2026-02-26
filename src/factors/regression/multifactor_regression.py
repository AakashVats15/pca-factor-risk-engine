import pandas as pd
import numpy as np

class MultiFactorRegression:
    def __init__(self):
        self.betas = None
        self.residuals = None
        self.idio_var = None

    def fit(self, returns: pd.DataFrame, factors: pd.DataFrame):
        X = factors.values
        Y = returns.values

        XtX = X.T @ X
        XtY = X.T @ Y

        betas = np.linalg.pinv(XtX) @ XtY
        self.betas = pd.DataFrame(betas.T, index=returns.columns, columns=factors.columns)

        fitted = X @ betas
        res = Y - fitted
        self.residuals = pd.DataFrame(res, index=returns.index, columns=returns.columns)

        self.idio_var = self.residuals.var()
        return self

    def get_betas(self):
        return self.betas

    def get_residuals(self):
        return self.residuals

    def get_idiosyncratic_variance(self):
        return self.idio_var