from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp_reg = MLPRegressor(hidden_layer_sizes=(20, 10), activation='relu', max_iter=1000, random_state=42)
mlp_reg.fit(X_train_scaled, y_train)
mlp_pred = mlp_reg.predict(X_test_scaled)

lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
lin_pred = lin_reg.predict(X_test_scaled)

print("MLP MSE:", mean_squared_error(y_test, mlp_pred), "R2:", r2_score(y_test, mlp_pred))
print("Linear Reg MSE:", mean_squared_error(y_test, lin_pred), "R2:", r2_score(y_test, lin_pred))