import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

VIS_DIR = Path("visuals")
VIS_DIR.mkdir(exist_ok=True)

def _timestamp():
    return datetime.now().strftime("%d%m%y_%H%M%S")

class Plotting:
    @staticmethod
    def scree(eigenvalues):
        plt.figure()
        plt.plot(eigenvalues, marker="o")
        plt.title("Scree Plot")
        plt.xlabel("Component")
        plt.ylabel("Eigenvalue")
        plt.tight_layout()
        filename = VIS_DIR / f"scree_{_timestamp()}.png"
        plt.savefig(filename)
        plt.show()

    @staticmethod
    def loadings_heatmap(loadings):
        plt.figure()
        plt.imshow(loadings.values, aspect="auto", cmap="viridis")
        plt.colorbar()
        plt.title("Factor Loadings")
        plt.tight_layout()
        filename = VIS_DIR / f"loadings_heatmap_{_timestamp()}.png"
        plt.savefig(filename)
        plt.show()

    @staticmethod
    def risk_contribution(rc):
        plt.figure()
        rc.plot(kind="bar")
        plt.title("Risk Contribution")
        plt.tight_layout()
        filename = VIS_DIR / f"risk_contribution_{_timestamp()}.png"
        plt.savefig(filename)
        plt.show()