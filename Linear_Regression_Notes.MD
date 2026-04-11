# 📈 Linear Regression

## What is Linear Regression?

Linear Regression is a **supervised learning** algorithm used to predict a **continuous output** variable based on one or more input features.

It models the relationship between input `X` and output `y` as a straight line.

---

## Equation

### Simple Linear Regression (1 feature):
```
ŷ = w₀ + w₁·x
```

### Multiple Linear Regression (n features):
```
ŷ = w₀ + w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ
```

| Symbol | Meaning |
|--------|---------|
| `ŷ`    | Predicted output |
| `w₀`   | Bias / Intercept |
| `w₁...wₙ` | Weights / Coefficients |
| `x₁...xₙ` | Input features |

---

## Cost Function — Mean Squared Error (MSE)

We minimize the difference between predicted `ŷ` and actual `y`:

```
MSE = (1/n) * Σ (yᵢ - ŷᵢ)²
```

The goal is to find weights `w` that **minimize MSE**.

---

## How the Model Learns — Gradient Descent

```
w := w - α * (∂MSE/∂w)
```

- `α` = learning rate (how big the steps are)
- We iteratively update weights to move toward the minimum cost

---

## Assumptions of Linear Regression

1. **Linearity** — relationship between X and y is linear
2. **Independence** — observations are independent
3. **Homoscedasticity** — constant variance of errors
4. **No multicollinearity** — features are not highly correlated
5. **Normality of errors** — residuals are normally distributed

---

## Python Implementation

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

---

## Evaluation Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| **MSE** | `Σ(y - ŷ)² / n` | Mean of squared errors |
| **RMSE** | `√MSE` | Root mean squared error (same unit as y) |
| **MAE** | `Σ|y - ŷ| / n` | Mean of absolute errors |
| **R² Score** | `1 - SS_res/SS_tot` | How well model explains variance (1 = perfect) |

---

## Limitations

- Only works for **linear relationships**
- Sensitive to **outliers**
- Fails for **classification problems** (see Logistic Regression notes)
- Prone to **overfitting** with many features → use Ridge/Lasso Regression

---

## Quick Summary

```
Linear Regression:
  ✅ Continuous output prediction
  ✅ Simple & interpretable
  ❌ Cannot handle classification
  ❌ Sensitive to outliers and multicollinearity
```
