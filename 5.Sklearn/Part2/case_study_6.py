import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
df = pd.read_csv(url, names=columns)

print("--- 1. Handling Missing Values ---")

df.replace('?', np.nan, inplace=True)
print("Missing values found:",df.isnull().sum()[df.isnull().sum() > 0])
df.fillna(df.median(numeric_only=True), inplace=True) 

print("--- 2. Creating Age Groups (Binning) ---")

bins = [0, 40, 55, 70, 100]
labels = ['Young', 'Middle-aged', 'Senior', 'Elderly']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
print("First 5 rows of new 'age_group' column:")
print(df[['age', 'age_group']].head(), "\n")

print("--- 3. Encoding Categorical Variables ---")

df_encoded = pd.get_dummies(df, columns=['cp'], drop_first=True)
print("Columns after One-Hot Encoding 'cp':")
print(df_encoded.columns[:7].tolist(), "...", df_encoded.columns[-3:].tolist())


plt.figure(figsize=(12, 8))

numeric_df = df.drop('age_group', axis=1).astype(float)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Heart Disease Features")
plt.show()