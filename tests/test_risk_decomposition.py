import numpy as np
import pandas as pd
from src.factors.risk.variance_decomposition import VarianceDecomposition

def test_variance_decomposition():
    np.random.seed(0)

    loadings = pd.DataFrame(np.random.normal(0, 1, size=(5, 3)))
    factor_cov = pd.DataFrame(np.eye(3))
    idio_var = pd.Series(np.abs(np.random.normal(0, 0.1, size=5)))

    vd = VarianceDecomposition(loadings, factor_cov, idio_var).compute()

    fv = vd.get_factor_variance()
    tv = vd.get_total_variance()

    assert len(fv) == 5
    assert len(tv) == 5
    assert np.all(tv >= fv)
    assert np.all(tv >= 0)