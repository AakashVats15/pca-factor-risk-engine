import pandas as pd
from pathlib import Path

from src.data.loaders.returns_loader import ReturnsLoader
from src.data.preprocess.clean_returns import ReturnsCleaner
from src.factors.pca.pca_model import PCAModel
from src.factors.pca.factor_loadings import FactorLoadings
from src.factors.pca.factor_returns import FactorReturns

class PCAPipeline:
    def __init__(self, returns_path, n_components=None):
        self.returns_path = returns_path
        self.n_components = n_components

    def run(self):
        loader = ReturnsLoader(self.returns_path)
        raw = loader.load()

        cleaner = ReturnsCleaner()
        clean = cleaner.clean(raw)

        pca = PCAModel(self.n_components)
        pca.fit(clean)

        loadings = FactorLoadings(pca.loadings).normalize()
        factors = FactorReturns(loadings).compute(clean)

        return {
            "clean_returns": clean,
            "loadings": loadings,
            "factor_returns": factors,
            "eigenvalues": pca.eigenvalues
        }

if __name__ == "__main__":
    path = Path("data/processed/returns.csv")
    pipeline = PCAPipeline(path, n_components=5)
    out = pipeline.run()