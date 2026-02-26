import pandas as pd
import numpy as np

class FactorLoadings:
    def __init__(self, loadings: pd.DataFrame):
        self.loadings = loadings

    def normalize(self):
        norm = np.linalg.norm(self.loadings, axis=0)
        self.loadings = self.loadings.div(norm, axis=1)
        return self.loadings

    def get(self):
        return self.loadings