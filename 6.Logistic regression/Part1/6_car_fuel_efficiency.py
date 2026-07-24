import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
mpg_data = pd.read_csv(url).dropna(subset=['displacement', 'mpg'])

X_disp = mpg_data[['displacement']]
y_mpg = mpg_data['mpg']

model_6 = LinearRegression()
model_6.fit(X_disp, y_mpg)

pred_mpg = model_6.predict([[244]])
print(f"Predicted MPG for a ~4.0L (244 cu in) engine: {pred_mpg[0]:.2f}")
print(f"Slope: {model_6.coef_[0]:.4f}")

sns.regplot(x='displacement', y='mpg', data=mpg_data, line_kws={"color": "red"})
plt.title("Displacement vs MPG")
plt.show()