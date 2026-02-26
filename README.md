# PCA‑Factor Risk Engine

A modular Python framework for building and analysing multi‑factor risk models using PCA and cross‑sectional regression. Designed to demonstrate quantitative research skills in factor construction, risk decomposition, and systematic model engineering.

---

## 📌 Overview

This project implements a full multi‑factor risk modelling workflow:

- PCA on asset returns  
- Factor loadings & factor returns  
- Multi‑factor regression  
- Idiosyncratic risk estimation  
- Variance & risk decomposition  
- Factor risk contributions  
- Visualisations & interpretation  

The architecture mirrors real quant research pipelines used in hedge funds, asset managers, and systematic trading teams.

---

## 🧠 Methodology

### **1. PCA‑Based Factor Extraction**
- Compute covariance matrix of returns  
- Extract orthogonal factors via eigen‑decomposition  
- Normalise eigenvectors to obtain factor loadings  
- Project returns onto loadings to obtain factor returns  

### **2. Multi‑Factor Regression**
- Cross‑sectional regression of asset returns on factor exposures  
- Estimation of betas, residuals, and idiosyncratic variance  
- Rolling‑window estimation for time‑varying exposures  

### **3. Risk Decomposition**
- Total variance split into:
  - Systematic (factor‑driven)
  - Idiosyncratic (asset‑specific)
- Contribution of each factor to portfolio risk  
- PCA vs. fundamental factor comparison  

---

## 🏗 Project Structure

```
src/
  data/...
  factors/...
  utils/...
  pipelines/...
tests/
docs/
data/
```

All components are modular, testable, and production‑aligned.

---

## 🚀 Pipelines

### `run_pca_pipeline.py`
End‑to‑end PCA factor extraction:
- Load returns  
- Clean & standardise  
- Compute PCA  
- Save loadings, factor returns, explained variance  

### `run_factor_model.py`
Full multi‑factor risk model:
- Estimate exposures  
- Compute factor covariance  
- Decompose risk  
- Generate plots & diagnostics  

---

## 📊 Visualisations

The project includes:
- Scree plots  
- Factor loading heatmaps  
- Factor return time‑series  
- Risk contribution bar charts  
- Idiosyncratic vs. systematic variance breakdown  

These are designed for interpretability and QR interview discussions.

---

## 🧪 Testing

Unit tests cover:
- PCA correctness  
- Factor return reconstruction  
- Risk decomposition consistency  

---

## 🎯 Purpose

This repository demonstrates:
- Strong understanding of PCA and factor modelling  
- Ability to engineer clean, modular quant research code  
- Practical knowledge of risk decomposition used in real portfolios  
- Professional documentation and reproducible pipelines  

Ideal for quant research, risk modelling, and systematic strategy roles.

---

## 📄 License

MIT License.