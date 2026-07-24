import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wine_df = pd.read_csv(url, sep=';')

wine_df['acid_balance'] = wine_df['citric acid'] / (wine_df['volatile acidity'] + 0.0001)
wine_df['sulfur_ratio'] = wine_df['free sulfur dioxide'] / (wine_df['total sulfur dioxide'] + 0.0001)

corr_matrix = wine_df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.8)]
wine_df_clean = wine_df.drop(columns=to_drop)

print(f"Features dropped due to high correlation: {to_drop}")

X = wine_df_clean.drop('quality', axis=1)
y = wine_df_clean['quality']

model = LinearRegression()
cv_scores = cross_val_score(model, X, y, cv=10, scoring='r2')
print(f"10-Fold CV Average R-squared: {cv_scores.mean():.4f}")

model.fit(X, y)
importance = pd.Series(model.coef_, index=X.columns).abs().sort_values(ascending=False)
print(f"\nMost Important Property: {importance.index[0]} (Coefficient: {importance.iloc[0]:.4f})")