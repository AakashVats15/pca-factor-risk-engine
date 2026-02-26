import os

base_path = r"E:\Personal\GitHub\Python Code Repo\pca-factor-risk-engine"

folders = [
    "src/data/loaders",
    "src/data/preprocess",
    "src/factors/pca",
    "src/factors/regression",
    "src/factors/risk",
    "src/utils",
    "src/pipelines",
    "tests",
    "docs/visuals",
    "data/raw",
    "data/processed"
]

files = [
    "src/data/loaders/returns_loader.py",
    "src/data/preprocess/clean_returns.py",

    "src/factors/pca/pca_model.py",
    "src/factors/pca/factor_loadings.py",
    "src/factors/pca/factor_returns.py",

    "src/factors/regression/multifactor_regression.py",

    "src/factors/risk/idiosyncratic_risk.py",
    "src/factors/risk/variance_decomposition.py",
    "src/factors/risk/risk_contribution.py",

    "src/utils/stats.py",
    "src/utils/plotting.py",
    "src/utils/config.py",

    "src/pipelines/run_pca_pipeline.py",
    "src/pipelines/run_factor_model.py",

    "tests/test_pca.py",
    "tests/test_factor_returns.py",
    "tests/test_risk_decomposition.py",

    ".gitignore",
    "requirements.txt",
    "README.md",
    "docs/architecture.md",
    "docs/methodology.md",
    "docs/interpretation.md"
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files
for file in files:
    file_path = os.path.join(base_path, file)
    with open(file_path, "w") as f:
        f.write("")  # create empty file

print("Project structure created successfully.")