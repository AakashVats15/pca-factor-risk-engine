import numpy as np
import pandas as pd

class PCAModel:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.loadings = None
        self.eigenvalues = None

    def fit(self, returns: pd.DataFrame):
        cov = np.cov(returns.T)
        vals, vecs = np.linalg.eigh(cov)
        idx = np.argsort(vals)[::-1]
        vals = vals[idx]
        vecs = vecs[:, idx]

        if self.n_components is not None:
            vals = vals[:self.n_components]
            vecs = vecs[:, :self.n_components]

        self.eigenvalues = vals
        self.loadings = pd.DataFrame(vecs, index=returns.columns)
        return self

    def transform(self, returns: pd.DataFrame):
        return returns.values @ self.loadings.values

    def fit_transform(self, returns: pd.DataFrame):
        self.fit(returns)
        return self.transform(returns)