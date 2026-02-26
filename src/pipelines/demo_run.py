import pandas as pd
from pathlib import Path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.pipelines.run_pca_pipeline import PCAPipeline
from src.pipelines.run_factor_model import FactorModelPipeline
from src.utils.plotting import Plotting
from src.utils.config import Config

def main():
    returns_path = Path(Config.RETURNS_PATH)

    pca = PCAPipeline(returns_path, n_components=5)
    pca_out = pca.run()

    loadings = pca_out["loadings"]
    factor_returns = pca_out["factor_returns"]
    eigenvalues = pca_out["eigenvalues"]

    loadings.to_csv("data/processed/loadings.csv")
    factor_returns.to_csv("data/processed/factor_returns.csv")

    Plotting.scree(eigenvalues)
    Plotting.loadings_heatmap(loadings)

    weights = pd.Series(1 / len(loadings), index=loadings.index)

    fm = FactorModelPipeline(returns_path, loadings, weights)
    fm_out = fm.run()

    rc = fm_out["risk_contribution"]
    rc.to_csv("data/processed/risk_contribution.csv")

    Plotting.risk_contribution(rc)

    print("PCA and Factor Model completed.")
    print("Eigenvalues:", eigenvalues[:5])
    print("Top 5 risk contributions:")
    print(rc.sort_values(ascending=False).head())

if __name__ == "__main__":
    main()