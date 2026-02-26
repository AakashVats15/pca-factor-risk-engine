# Interpretation Guide

This document explains how to interpret PCA outputs, factor model results, and risk decomposition.

---

## 1. PCA Outputs

### Eigenvalues
- Large eigenvalues indicate strong common factors.
- Scree plot helps determine number of components.

### Loadings
- High magnitude → strong exposure.
- Sign indicates direction of co‑movement.

### Factor Returns
- Represent latent drivers of asset returns.
- Useful for regime detection and clustering.

---

## 2. Regression Outputs

### Betas
- Measure sensitivity of each asset to each factor.
- Stable betas indicate robust factor structure.

### Residuals
- Should be mean‑zero.
- High residual variance → asset not well explained by factors.

---

## 3. Risk Model Outputs

### Idiosyncratic Variance
- High idio variance → noisy or unique asset.
- Low idio variance → factor‑driven asset.

### Systematic vs Idiosyncratic Risk
- Systematic risk comes from common factors.
- Idiosyncratic risk is asset‑specific.

### Total Variance
- Sum of systematic and idiosyncratic components.

---

## 4. Risk Contribution

### Marginal Contribution
- How much each factor increases portfolio variance.

### Total Contribution
- Absolute contribution to portfolio risk.

### Percentage Contribution
- Normalised contributions.
- Highlights dominant risk drivers.

---

## 5. Practical Use Cases

- Portfolio construction
- Hedging and risk control
- Factor exposure monitoring
- Stress testing
- Regime analysis

---

## 6. Red Flags

- First eigenvalue too large → single dominant factor.
- Loadings unstable over time → regime shift.
- High idiosyncratic variance → unreliable regression.
- Concentrated risk contribution → poor diversification.