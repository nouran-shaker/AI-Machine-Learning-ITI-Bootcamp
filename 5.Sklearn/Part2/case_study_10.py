import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, TargetEncoder
from sklearn.metrics import accuracy_score
import category_encoders as ce

titanic = fetch_openml('titanic', version=1, as_frame=True, parser='auto').frame

df = titanic[['cabin', 'survived']].dropna().copy()
df['survived'] = df['survived'].astype(int)

X = df[['cabin']]
y = df['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("--- Original High Cardinality Data ---")
print("Number of Unique Cabins: ",X['cabin'].nunique())

def evaluate_encoder(encoder_name, X_train_enc, X_test_enc):
    model = LogisticRegression(max_iter=1000).fit(X_train_enc, y_train)
    acc = accuracy_score(y_test, model.predict(X_test_enc))
    shape = X_train_enc.shape[1]
    print(encoder_name,": Output Columns = ",shape," | Accuracy = ",acc)


ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_train_ohe = ohe.fit_transform(X_train)
X_test_ohe = ohe.transform(X_test)
evaluate_encoder("One-Hot Encoding", X_train_ohe, X_test_ohe)

target_enc = TargetEncoder(target_type='binary')
X_train_te = target_enc.fit_transform(X_train, y_train)
X_test_te = target_enc.transform(X_test)
evaluate_encoder("Target Encoding ", X_train_te, X_test_te)

bin_enc = ce.BinaryEncoder(cols=['cabin'])
X_train_bin = bin_enc.fit_transform(X_train)
X_test_bin = bin_enc.transform(X_test)
evaluate_encoder("Binary Encoding ", X_train_bin, X_test_bin)