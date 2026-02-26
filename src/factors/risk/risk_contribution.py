import pandas as pd
import numpy as np

class RiskContribution:
    def __init__(self, loadings: pd.DataFrame, factor_cov: pd.DataFrame, weights: pd.Series):
        self.loadings = loadings
        self.factor_cov = factor_cov
        self.weights = weights
        self.marginal = None
        self.total = None
        self.percent = None

    def compute(self):
        b = self.loadings.T @ self.weights
        m = self.factor_cov.values @ b.values
        self.marginal = pd.Series(m, index=self.factor_cov.index)

        t = b.values * m
        self.total = pd.Series(t, index=self.factor_cov.index)

        s = self.total.sum()
        self.percent = self.total / s if s != 0 else self.total * 0
        return self

    def get_marginal(self):
        return self.marginal

    def get_total(self):
        return self.total

    def get_percent(self):
        return self.percent