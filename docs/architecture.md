# Architecture Overview

This document describes the architecture of the PCA Factor Risk Engine.  
The system follows a modular, production‑grade design inspired by hedge‑fund research libraries, with strict separation between data, factors, risk, utilities, and pipelines.

---

## 1. Directory Structure

```
pca-factor-risk-engine/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── src/
│   ├── data/
│   │   ├── loaders/
│   │   └── preprocess/
│   │
│   ├── factors/
│   │   ├── pca/
│   │   ├── regression/
│   │   └── risk/
│   │
│   ├── pipelines/
│   │
│   └── utils/
│
└── tests/
```

Each folder has a single responsibility, enabling clean orchestration and easy extension.

---

## 2. Data Flow

The system processes data through three stages:

### **1. Raw Data**
Unmodified external inputs:
- `prices_raw.csv`
- `returns_raw.csv`
- `universe.csv`
- `metadata.csv`

### **2. Processed Data**
Cleaned, aligned, model‑ready datasets:
- `returns.csv`
- `prices.csv`
- `universe.csv`
- `metadata.csv`

### **3. Model Inputs**
Used by PCA and factor‑risk pipelines:
- returns matrix
- PCA loadings
- factor returns
- portfolio weights

---

## 3. Core Components

### **3.1 Data Layer**
Located in `src/data/`.

- **ReturnsLoader**  
  Loads returns from CSV into a DataFrame.

- **ReturnsCleaner**  
  Performs winsorisation, demeaning, and standardisation.

This layer ensures all downstream modules receive clean, consistent inputs.

---

### **3.2 PCA Layer**
Located in `src/factors/pca/`.

- **PCAModel**  
  Computes eigenvalues and eigenvectors of the covariance matrix.

- **FactorLoadings**  
  Normalises eigenvectors into interpretable factor exposures.

- **FactorReturns**  
  Projects returns onto loadings to obtain factor time series.

This layer extracts latent structure from the return matrix.

---

### **3.3 Regression Layer**
Located in `src/factors/regression/`.

- **MultiFactorRegression**  
  Computes betas, residuals, and idiosyncratic variance using closed‑form OLS.

This layer fits a linear factor model to asset returns.

---

### **3.4 Risk Layer**
Located in `src/factors/risk/`.

- **IdiosyncraticRisk**  
  Computes idio variance, volatility, and diagonal covariance.

- **VarianceDecomposition**  
  Splits total variance into systematic and idiosyncratic components.

- **RiskContribution**  
  Computes marginal, total, and percentage factor contributions.

This layer provides the core risk analytics used in portfolio construction.

---

## 4. Pipelines

### **4.1 PCA Pipeline**
`run_pca_pipeline.py`

- loads returns  
- cleans data  
- fits PCA  
- normalises loadings  
- computes factor returns  
- saves outputs  

### **4.2 Factor Model Pipeline**
`run_factor_model.py`

- loads returns  
- computes factor returns  
- runs multi‑factor regression  
- computes idiosyncratic risk  
- performs variance decomposition  
- computes risk contributions  

Pipelines orchestrate the entire workflow end‑to‑end.

---

## 5. Utilities

Located in `src/utils/`.

- **stats.py**  
  Covariance, correlation, shrinkage, annualisation.

- **plotting.py**  
  Scree plot, loadings heatmap, risk contribution chart.

- **config.py**  
  Centralised constants (paths, parameters).

These utilities keep the core modules clean and focused.

---

## 6. Design Principles

The architecture follows five core principles:

### **1. Deterministic**
No randomness except in synthetic data generation.

### **2. Modular**
Each module has a single responsibility.

### **3. Minimal API**
Only essential public methods are exposed.

### **4. Transparent**
No hidden state; all outputs are explicit.

### **5. Production‑aligned**
Mirrors the structure used in real quant research teams.

---

## 7. Execution Flow Summary

1. Generate synthetic data.  
2. Run PCA pipeline.  
3. Save loadings and factor returns.  
4. Run factor model pipeline.  
5. Produce risk decomposition and visualisations.  
6. Export results to `data/processed/`.

This completes the full PCA → regression → risk workflow.