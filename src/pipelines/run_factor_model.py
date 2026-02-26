import pandas as pd
from pathlib import Path

from src.data.loaders.returns_loader import ReturnsLoader
from src.data.preprocess.clean_returns import ReturnsCleaner
from src.factors.pca.factor_returns import FactorReturns
from src.factors.regression.multifactor_regression import MultiFactorRegression
from src.factors.risk.idiosyncratic_risk import IdiosyncraticRisk
from src.factors.risk.variance_decomposition import VarianceDecomposition
from src.factors.risk.risk_contribution import RiskContribution

class FactorModelPipeline:
    def __init__(self, returns_path, loadings, weights):
        self.returns_path = returns_path
        self.loadings = loadings
        self.weights = weights

    def run(self):
        loader = ReturnsLoader(self.returns_path)
        raw = loader.load()

        cleaner = ReturnsCleaner()
        clean = cleaner.clean(raw)

        fr = FactorReturns(self.loadings).compute(clean)
        reg = MultiFactorRegression().fit(clean, fr)

        idio = IdiosyncraticRisk(reg.get_residuals()).compute()

        factor_cov = fr.cov()
        vd = VarianceDecomposition(self.loadings, factor_cov, idio.get_variance()).compute()

        rc = RiskContribution(self.loadings, factor_cov, self.weights).compute()

        return {
            "factor_returns": fr,
            "betas": reg.get_betas(),
            "residuals": reg.get_residuals(),
            "idiosyncratic_variance": idio.get_variance(),
            "factor_variance": vd.get_factor_variance(),
            "total_variance": vd.get_total_variance(),
            "risk_contribution": rc.get_percent()
        }

if __name__ == "__main__":
    path = Path("data/processed/returns.csv")
    loadings = pd.read_csv("data/processed/loadings.csv", index_col=0)
    weights = pd.Series(1 / len(loadings), index=loadings.index)
    pipeline = FactorModelPipeline(path, loadings, weights)
    out = pipeline.run()