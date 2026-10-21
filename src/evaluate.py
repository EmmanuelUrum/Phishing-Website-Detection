"""Shared metrics for all models."""
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def evaluate(model, X_test, y_test) -> dict:
    pred = model.predict(X_test)
    scores = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else pred
    return {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred),
        "recall": recall_score(y_test, pred),
        "f1": f1_score(y_test, pred),
        "roc_auc": roc_auc_score(y_test, scores),
    }
