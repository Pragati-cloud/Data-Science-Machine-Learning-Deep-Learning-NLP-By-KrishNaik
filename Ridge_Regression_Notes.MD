# 🔒 Ridge Regression (L2 Regularization)

## Why Ridge Regression?

Linear Regression can **overfit** when:
- There are too many features
- Features are highly correlated (multicollinearity)
- The model memorizes training data instead of learning patterns

**Ridge Regression** adds a penalty to prevent large weights, forcing the model to stay simple.

---

## Key Idea — Regularization

> Regularization = adding a penalty term to the cost function to reduce overfitting.

---

## Cost Function

### Linear Regression (plain):
```
Cost = MSE = (1/n) * Σ (yᵢ - ŷᵢ)²
```

### Ridge Regression (L2 penalty added):
```
Cost = MSE + λ * Σ wⱼ²
```

| Symbol | Meaning |
|--------|---------|
| `λ` (lambda) | Regularization strength (hyperparameter) |
| `Σ wⱼ²` | Sum of squared weights (L2 norm) |

- **λ = 0** → same as Linear Regression (no penalty)
- **λ → ∞** → all weights shrink toward 0 (underfitting)
- **Best λ** → found via cross-validation

---

## Effect on Weights

| Condition | Effect |
|-----------|--------|
| High λ | Weights are pushed closer to 0 → simpler model |
| Low λ | Weights can be large → similar to Linear Regression |
| Ridge | **Shrinks** weights but never makes them exactly 0 |

> 📌 Ridge does **not** perform feature selection (weights ≠ 0).  
> For feature selection, use **Lasso (L1)** instead.

---

## Ridge vs Lasso vs ElasticNet

| Method | Penalty | Feature Selection? | Use When |
|--------|---------|-------------------|----------|
| **Ridge** | L2: `λΣw²` | ❌ No | All features useful, multicollinearity |
| **Lasso** | L1: `λΣ|w|` | ✅ Yes | Some features are irrelevant |
| **ElasticNet** | L1 + L2 | ✅ Partial | Mix of both situations |

---

## Python Implementation

```python
import numpy as np
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Sample data
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=100, n_features=10, noise=10, random_state=42)

# Always scale features before Ridge!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Ridge with a fixed lambda (alpha)
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))
print("Coefficients:", model.coef_)

# Auto-select best lambda using cross-validation
ridge_cv = RidgeCV(alphas=[0.01, 0.1, 1, 10, 100], cv=5)
ridge_cv.fit(X_train, y_train)
print("Best alpha:", ridge_cv.alpha_)
```

---

## Important: Feature Scaling

> ⚠️ **Always scale features before Ridge Regression!**

Ridge penalizes large weights, but if features have different scales, the penalty is unfair.  
Use `StandardScaler` (mean=0, std=1) before fitting.

---

## Geometric Intuition

```
Without Ridge:  weights can be anywhere that minimizes MSE
With Ridge:     weights are constrained inside a "circle" (L2 ball)
                → solution stays near origin → small weights
```

---

## When to Use Ridge

- ✅ You have **many features** and all might be relevant
- ✅ Features are **correlated** (multicollinearity)
- ✅ Model is **overfitting** on training data
- ❌ You want to **eliminate useless features** → use Lasso instead

---

## Quick Summary

```
Ridge Regression:
  ✅ Prevents overfitting via L2 penalty
  ✅ Works well with correlated features
  ✅ Weights shrink but stay non-zero
  ❌ Does not perform feature selection
  ❌ Need to tune λ (use cross-validation)
```
