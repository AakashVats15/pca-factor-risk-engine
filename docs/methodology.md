# Methodology

This document explains the mathematical and statistical foundations of the PCA Factor Risk Engine.  

---

## 1. Returns Cleaning

### Winsorisation
Extreme values are clipped at lower and upper quantiles:

  **rᵢₜ ← clip(rᵢₜ, q, 1−q)**

### Demeaning
Each asset’s return series is centered:

  **rᵢₜ ← rᵢₜ − mean(rᵢ)**

### Standardisation
Each asset is scaled to unit variance:

  **rᵢₜ ← rᵢₜ / σᵢ**

---

## 2. Principal Component Analysis (PCA)

### Covariance Matrix
Given a returns matrix **X** (T × N):

  **C = (1 / (T − 1)) · XᵀX**

### Eigen‑Decomposition
The covariance matrix is decomposed as:

  **C = V Λ Vᵀ**

Where:

- **V** = matrix of eigenvectors (factor loadings)  
- **Λ** = diagonal matrix of eigenvalues (variance explained)

### Factor Returns
Factor returns are computed by projecting returns onto loadings:

  **F = X · V**

---

## 3. Multi‑Factor Regression

For each asset:

  **rₜ = β · fₜ + εₜ**

Where:

- **β** = factor exposures  
- **fₜ** = factor returns  
- **εₜ** = residual (idiosyncratic return)

### Closed‑Form OLS Solution
Given factor matrix **F** and returns **R**:

  **β = (FᵀF)⁻¹ FᵀR**

### Residuals
  **ε = R − Fβ**

### Idiosyncratic Variance
  **σ²ᵢ = Var(εᵢ)**

---

## 4. Risk Model

### Factor Covariance
  **Σ_f = Cov(F)**

### Systematic Variance
For each asset with loadings **Lᵢ**:

  **σ²_sys,ᵢ = Lᵢ Σ_f Lᵢᵀ**

### Total Variance
  **σ²_total,ᵢ = σ²_sys,ᵢ + σ²_idio,ᵢ**

---

## 5. Risk Contribution

Given portfolio weights **w**:

### Portfolio Factor Exposure
  **b = Lᵀ w**

### Marginal Contribution to Risk
  **m = Σ_f · b**

### Total Contribution
  **RC = b ⊙ m**  
(⊙ denotes element‑wise multiplication)

### Percentage Contribution
  **RC% = RC / Σ(RC)**

---

## 6. Interpretation

- **Eigenvalues** measure factor strength.  
- **Loadings** measure how assets co‑move with each factor.  
- **Factor returns** represent latent market drivers.  
- **Idiosyncratic variance** captures unexplained risk.  
- **Risk contribution** identifies which factors dominate portfolio volatility.