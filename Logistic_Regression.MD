# 🔀 Logistic Regression & Why Linear Regression Fails for Classification

---

## Part 1 — Why Linear Regression Fails for Classification

### Classification Problem

In classification, the output `y` is a **category**, not a number.  
Example (binary): `y ∈ {0, 1}` → spam/not spam, disease/no disease

### What Happens if We Use Linear Regression?

Linear regression predicts:
```
ŷ = w₀ + w₁·x
```

This gives values like `ŷ = -0.5`, `ŷ = 1.7`, `ŷ = 3.2` — which make **no sense** for classes 0 or 1.

### 3 Core Problems

#### ❌ Problem 1 — Output Range is Unbounded
```
Linear Regression output: (-∞, +∞)
Classification needs:      [0, 1]  (probabilities)
```

#### ❌ Problem 2 — Sensitive to Outliers (Threshold Shifts)
```
Example: Points at x = 1,2,3 are class 1; x = 4,5,6 are class 0
Linear regression draws a line. Add an outlier at x = 20 (still class 0)
→ The line tilts, and the decision boundary shifts incorrectly.
```

```
Without outlier:     |_____|-----|
With outlier:        |___________|-----|
                     Boundary shifts → misclassifies!
```

#### ❌ Problem 3 — Assumes Linearity in Output
- Linear regression assumes output changes uniformly with input
- Class probability should be **S-shaped (sigmoid)**, not linear

### Visual Comparison

```
Linear Regression fit for classification:

  y                         ● ●
  1 |                   ●●●
    |               ●●●
  0 |●●●●●●●
    |_________________________ x
    
    ŷ can go below 0 and above 1 — meaningless as probability!
```

---

## Part 2 — Logistic Regression

### What is Logistic Regression?

Despite the name, **Logistic Regression is a classification algorithm**.  
It predicts the **probability** that an input belongs to class 1.

```
P(y=1 | x) = σ(w₀ + w₁x₁ + ... + wₙxₙ)
```

---

### The Sigmoid Function — The Key Fix

Logistic Regression wraps the linear output inside a **sigmoid function**:

```
σ(z) = 1 / (1 + e^(-z))
```

| z | σ(z) |
|---|------|
| -∞ | → 0 |
| 0  | → 0.5 |
| +∞ | → 1 |

This squashes any real number into `(0, 1)` — valid as a probability!

```
Sigmoid shape:

  σ(z)
  1.0 |          _________
  0.5 |        /
  0.0 |_______/
       _____________________ z
         -5   0   +5
```

---

### Decision Boundary

```
If σ(z) ≥ 0.5  →  predict class 1
If σ(z) < 0.5  →  predict class 0
```

This corresponds to `z ≥ 0`, i.e., the linear equation `w·x ≥ 0`.

---

### Cost Function — Log Loss (Binary Cross-Entropy)

MSE doesn't work with sigmoid (non-convex). We use **Log Loss**:

```
Loss = -(1/n) * Σ [ yᵢ·log(ŷᵢ) + (1-yᵢ)·log(1-ŷᵢ) ]
```

| Actual y | Predicted ŷ | Loss |
|----------|------------|------|
| 1 | Close to 1 | Low ✅ |
| 1 | Close to 0 | High ❌ |
| 0 | Close to 0 | Low ✅ |
| 0 | Close to 1 | High ❌ |

---

### Python Implementation

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_breast_cancer

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # probability of class 1

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

---

### Multi-class Logistic Regression

Logistic Regression can handle multiple classes using:
- **One-vs-Rest (OvR)**: train one classifier per class
- **Softmax (Multinomial)**: extends sigmoid to multiple classes

```python
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
```

---

### Linear vs Logistic Regression — Side-by-Side

| Feature | Linear Regression | Logistic Regression |
|---------|------------------|---------------------|
| **Output** | Continuous (−∞, +∞) | Probability [0, 1] |
| **Task** | Regression | Classification |
| **Activation** | None (identity) | Sigmoid |
| **Cost Function** | MSE | Log Loss |
| **Boundary** | No boundary | Decision boundary |
| **Handles outliers** | ❌ Poorly | ✅ Better |

---

## Quick Summary

```
Why Linear Regression fails for classification:
  ❌ Outputs values outside [0, 1]
  ❌ Decision boundary shifts with outliers
  ❌ Assumes linear change in class probability

Logistic Regression fixes this by:
  ✅ Applying sigmoid → output in (0, 1)
  ✅ Using Log Loss instead of MSE
  ✅ Learning a stable decision boundary
```
