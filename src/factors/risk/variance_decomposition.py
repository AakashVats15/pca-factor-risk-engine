import pandas as pd
import numpy as np

class VarianceDecomposition:
    def __init__(self, loadings: pd.DataFrame, factor_cov: pd.DataFrame, idio_var: pd.Series):
        self.loadings = loadings
        self.factor_cov = factor_cov
        self.idio_var = idio_var
        self.factor_var = None
        self.total_var = None

    def compute(self):
        L = self.loadings.values
        F = self.factor_cov.values
        fv = np.sum(L @ F * L, axis=1)
        self.factor_var = pd.Series(fv, index=self.loadings.index)

        tv = self.factor_var + self.idio_var
        self.total_var = tv
        return self

    def get_factor_variance(self):
        return self.factor_var

    def get_total_variance(self):
        return self.total_var