# 📊 Performance Metrics — Accuracy, Precision, Recall & F-Beta Score

---

## Why Do We Need Metrics Beyond Accuracy?

Consider a dataset: **95% class 0, 5% class 1** (e.g., fraud detection)

A dumb model that always predicts class 0 gets **95% accuracy** — but it's useless!

We need better metrics → **Precision, Recall, F-Score**.

---

## The Confusion Matrix

The confusion matrix shows the full picture of classification results.

```
                   Predicted
                   0          1
Actual   0    [ TN          FP ]
         1    [ FN          TP ]
```

| Term | Abbr | Meaning |
|------|------|---------|
| **True Positive**  | TP | Model predicted 1 → Actual is 1 ✅ |
| **True Negative**  | TN | Model predicted 0 → Actual is 0 ✅ |
| **False Positive** | FP | Model predicted 1 → Actual is 0 ❌ (Type I error) |
| **False Negative** | FN | Model predicted 0 → Actual is 1 ❌ (Type II error) |

### Example

| | Predicted: Spam | Predicted: Not Spam |
|--|---|---|
| **Actual: Spam** | TP = 50 | FN = 10 |
| **Actual: Not Spam** | FP = 5 | TN = 935 |

---

## 1. Accuracy

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

- **What it measures**: Overall correctness
- **When to use**: When classes are balanced
- **When NOT to use**: Imbalanced datasets (misleading!)

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```

---

## 2. Precision

```
Precision = TP / (TP + FP)
```

- **Question it answers**: "Of all the times I predicted positive, how many were actually positive?"
- **Focus**: Avoiding **False Positives**
- **High precision matters when**: Cost of FP is high  
  → Example: Spam filter (don't mark real email as spam)

```
High Precision = When I say it's spam, I'm usually right.
```

```python
from sklearn.metrics import precision_score
precision_score(y_test, y_pred)
```

---

## 3. Recall (Sensitivity / True Positive Rate)

```
Recall = TP / (TP + FN)
```

- **Question it answers**: "Of all actual positives, how many did I correctly find?"
- **Focus**: Avoiding **False Negatives**
- **High recall matters when**: Cost of FN is high  
  → Example: Cancer detection (don't miss a sick patient!)

```
High Recall = I catch most of the actual positive cases.
```

```python
from sklearn.metrics import recall_score
recall_score(y_test, y_pred)
```

---

## Precision vs Recall Trade-off

```
        High Precision          High Recall
        Low Recall              Low Precision

Increase threshold → Precision ↑,  Recall ↓
Decrease threshold → Recall ↑,     Precision ↓
```

You can't always maximize both — pick based on your use case.

| Use Case | Priority |
|----------|----------|
| Spam detection | High Precision (FP costly) |
| Cancer screening | High Recall (FN costly) |
| Fraud detection | High Recall (FN costly) |
| Recommendation system | Balance both |

---

## 4. F1 Score

The **harmonic mean** of Precision and Recall:

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

- **Range**: [0, 1] — higher is better
- **When to use**: You want balance between precision and recall
- **Better than accuracy** for imbalanced datasets

```python
from sklearn.metrics import f1_score
f1_score(y_test, y_pred)
```

---

## 5. F-Beta Score (Generalized F Score)

F1 treats Precision and Recall **equally**. F-Beta lets you **control the balance**:

```
F_β = (1 + β²) * (Precision * Recall) / (β²·Precision + Recall)
```

| β value | Emphasis | Use When |
|---------|----------|----------|
| `β < 1` (e.g., 0.5) | More weight on **Precision** | FP is costly (e.g., spam filter) |
| `β = 1` | Equal weight → **F1 Score** | Balanced importance |
| `β > 1` (e.g., 2) | More weight on **Recall** | FN is costly (e.g., disease detection) |

```python
from sklearn.metrics import fbeta_score

# β = 0.5 → precision matters more
fbeta_score(y_test, y_pred, beta=0.5)

# β = 2 → recall matters more
fbeta_score(y_test, y_pred, beta=2)
```

---

## All Metrics Together

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, fbeta_score, confusion_matrix, classification_report
)

print("Accuracy  :", accuracy_score(y_test, y_pred))
print("Precision :", precision_score(y_test, y_pred))
print("Recall    :", recall_score(y_test, y_pred))
print("F1 Score  :", f1_score(y_test, y_pred))
print("F2 Score  :", fbeta_score(y_test, y_pred, beta=2))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nFull Report:\n", classification_report(y_test, y_pred))
```

---

## Dataset Table Format (from Notes)

When evaluating manually:

| x₁ | x₂ | y (actual) | ŷ (predicted) |
|----|----|-----------|--------------|
| -  | -  | 0         | 1            |
| -  | -  | 1         | 1            |
| ...| ...| ...       | ...          |

Then build the confusion matrix by comparing `y` vs `ŷ` for each row.

---

## Quick Reference Cheat Sheet

```
Confusion Matrix:
  TP = correct positive predictions
  TN = correct negative predictions
  FP = wrong positive predictions  (Type I error)
  FN = wrong negative predictions  (Type II error)

Formulas:
  Accuracy  = (TP + TN) / Total
  Precision = TP / (TP + FP)       → care about FP
  Recall    = TP / (TP + FN)       → care about FN
  F1        = 2·P·R / (P + R)      → balance both
  F_β       = (1+β²)·P·R / (β²·P + R)  → tune the balance
```
