import pandas as pd
import numpy as np

class ReturnsCleaner:
    def __init__(self, winsor=0.01, standardize=True, demean=True):
        self.winsor = winsor
        self.standardize = standardize
        self.demean = demean

    def winsorize(self, df):
        lower = df.quantile(self.winsor)
        upper = df.quantile(1 - self.winsor)
        return df.clip(lower, upper, axis=1)

    def zscore(self, df):
        mean = df.mean()
        std = df.std().replace(0, np.nan)
        return (df - mean) / std

    def clean(self, df):
        df = df.dropna(how="all")
        df = df.fillna(method="ffill").fillna(0)
        df = self.winsorize(df)
        if self.demean:
            df = df - df.mean()
        if self.standardize:
            df = self.zscore(df)
        df = df.replace([np.inf, -np.inf], 0)
        return df