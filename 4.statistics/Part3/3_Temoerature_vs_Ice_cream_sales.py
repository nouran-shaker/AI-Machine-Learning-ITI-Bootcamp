# Temperature vs. Ice Cream Sales
# Investigate correlation using scatter plots and Pearson’s R

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
temp = np.linspace(20, 35, 30)
sales = 50 + 2 * temp + np.random.normal(0, 5, 30)

correlation_matrix = np.corrcoef(temp, sales)
pearson_r = correlation_matrix[0, 1]

if pearson_r >= 0.7:
    interpretation = "Strong positive correlation"
elif 0.3 <= pearson_r < 0.7:
    interpretation = "Moderate positive correlation"
elif -0.3 < pearson_r < 0.3:
    interpretation = "Weak or no correlation"
elif -0.7 < pearson_r <= -0.3:
    interpretation = "Moderate negative correlation"
else:
    interpretation = "Strong negative correlation"

print(f"Pearson's R: {pearson_r:.4f}")
print(f"Interpretation: {interpretation}")

slope, intercept = np.polyfit(temp, sales, 1)

regression_line = slope * temp + intercept

plt.figure(figsize=(8, 6))


plt.scatter(temp, sales, color='blue', alpha=0.7, label='Daily Data')


plt.plot(temp, regression_line, color='red', linewidth=2, label=f'Trend (y = {slope:.2f}x + {intercept:.2f})')

plt.title('Temperature vs. Ice Cream Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales ($)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()