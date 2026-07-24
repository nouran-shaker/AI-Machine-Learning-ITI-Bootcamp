from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt


data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.20, random_state=42)

lr = LogisticRegression(max_iter=10000)
rf = RandomForestClassifier(random_state=42)
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

lr_preds = lr.predict(X_test)

print("--- Sample Predictions (First 10 Patients in Test Set) ---")
print("Actual Labels:  ",y_test[:10])
print("Model Predicti ons:  ",lr_preds[:10])

print("--- Logistic Regression Confusion Matrix ---")
print(confusion_matrix(y_test, lr_preds))
print("--- Classification Report ---")
print(classification_report(y_test, lr_preds))

lr_probs = lr.predict_proba(X_test)[:, 1] 
fpr, tpr, _ = roc_curve(y_test, lr_probs)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f'Logistic Reg (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
plt.title('Receiver Operating Characteristic (ROC)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()

skf = StratifiedKFold(n_splits=5)
scores = cross_val_score(rf, data.data, data.target, cv=skf)
print("Stratified K-Fold Accuracies: ",scores)