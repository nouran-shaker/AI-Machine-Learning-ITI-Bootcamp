# Study Hours vs. Exam Scores Regression
# Perform linear regression analysis
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
scores = 30 + 7 * hours + np.random.normal(0, 5, 50)

slope, intercept = np.polyfit(hours, scores, 1)

correlation_matrix = np.corrcoef(hours, scores)
pearson_r = correlation_matrix[0, 1]
r_squared = pearson_r**2

print("R-squared: %.2f" % r_squared)

# Interpretation logic
if r_squared >= 0.7:
    interpretation = "Strong fit. A large portion of the variance in exam scores is explained by study hours."
elif 0.3 <= r_squared < 0.7:
    interpretation = "Moderate fit. A moderate portion of the variance is explained."
else:
    interpretation = "Weak fit. Very little variance in scores is explained by study hours."
print(f"Interpretation: {interpretation}")


plt.figure(figsize=(8, 6))

plt.scatter(hours, scores, color='purple', alpha=0.7, label='Student Data')

x_line = np.array([np.min(hours), np.max(hours)])
y_line = slope * x_line + intercept


plt.plot(x_line, y_line, color='orange', linewidth=2, label=f'Regression Line (y = {slope:.2f}x + {intercept:.2f})')

plt.title('Study Hours vs. Exam Scores Regression')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()