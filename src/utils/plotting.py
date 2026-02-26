import pandas as pd
import matplotlib.pyplot as plt

class Plotting:
    @staticmethod
    def scree(eigenvalues):
        plt.figure()
        plt.plot(eigenvalues, marker="o")
        plt.title("Scree Plot")
        plt.xlabel("Component")
        plt.ylabel("Eigenvalue")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def loadings_heatmap(loadings):
        plt.figure()
        plt.imshow(loadings.values, aspect="auto", cmap="viridis")
        plt.colorbar()
        plt.title("Factor Loadings")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def risk_contribution(rc):
        plt.figure()
        rc.plot(kind="bar")
        plt.title("Risk Contribution")
        plt.tight_layout()
        plt.show()