from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def evaluate_model(y_true, y_pred):
    """
    Evaluates the model performance using classification metrics.

    Parameters:
        - y_true (array): True labels.
        - y_pred (array): Predicted labels.

    Returns:
        - dict: Evaluation metrics.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    print(f"\nAccuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1_score": f1}
