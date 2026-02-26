import pandas as pd
import numpy as np

class Stats:
    @staticmethod
    def cov(df):
        return df.cov()

    @staticmethod
    def corr(df):
        return df.corr()

    @staticmethod
    def annualize_cov(cov, periods=252):
        return cov * periods

    @staticmethod
    def annualize_vol(vol, periods=252):
        return vol * np.sqrt(periods)

    @staticmethod
    def shrink_cov(cov, alpha=0.1):
        diag = np.diag(np.diag(cov))
        return alpha * diag + (1 - alpha) * cov