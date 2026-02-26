import numpy as np
import pandas as pd
from src.factors.pca.factor_returns import FactorReturns

def test_factor_returns_computation():
    np.random.seed(0)
    returns = pd.DataFrame(np.random.normal(0, 1, size=(20, 4)))
    loadings = pd.DataFrame(np.random.normal(0, 1, size=(4, 2)))

    fr = FactorReturns(loadings).compute(returns)

    assert fr.shape == (20, 2)
    assert not fr.isna().any().any()