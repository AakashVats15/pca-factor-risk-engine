import numpy as np
import pandas as pd
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


from src.factors.pca.pca_model import PCAModel

def test_pca_basic():
    np.random.seed(0)
    df = pd.DataFrame(np.random.normal(0, 1, size=(100, 5)))

    pca = PCAModel(n_components=3).fit(df)

    assert len(pca.eigenvalues) == 3
    assert pca.loadings.shape == (5, 3)
    assert np.all(np.diff(pca.eigenvalues) <= 0)

def test_pca_transform_dimensions():
    np.random.seed(1)
    df = pd.DataFrame(np.random.normal(0, 1, size=(50, 4)))

    pca = PCAModel(n_components=2)
    factors = pca.fit_transform(df)

    assert factors.shape == (50, 2)