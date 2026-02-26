import pandas as pd
import numpy as np

class IdiosyncraticRisk:
    def __init__(self, residuals: pd.DataFrame):
        self.residuals = residuals
        self.var = None
        self.vol = None
        self.cov = None

    def compute(self):
        self.var = self.residuals.var()
        self.vol = np.sqrt(self.var)
        self.cov = np.diag(self.var.values)
        return self

    def get_variance(self):
        return self.var

    def get_volatility(self):
        return self.vol

    def get_covariance_matrix(self):
        return self.cov