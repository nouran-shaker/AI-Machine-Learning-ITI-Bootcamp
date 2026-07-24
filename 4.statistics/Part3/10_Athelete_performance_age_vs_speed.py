# Athlete Performance: Age vs. Speed
# Analyze correlation and regression
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
age = np.random.randint(18, 40, 40)
speed = 10 - 0.15 * age + np.random.normal(0, 0.5, 40)

correlation_matrix = np.corrcoef(age, speed)
pearson_r = correlation_matrix[0, 1]

print(f"Pearson's R: {pearson_r:.4f}")
print("Discussion:")
if pearson_r < -0.7:
    print("There is a strong negative correlation. As age increases, sprint speed consistently decreases.")
elif -0.7 <= pearson_r < -0.3:
    print("There is a moderate negative correlation. Older athletes tend to be slower, but there is noticeable variance.")
else:
    print("There is a weak negative correlation or no correlation.")


slope, intercept = np.polyfit(age, speed, 1)

plt.figure(figsize=(8, 6))

plt.scatter(age, speed, color='darkblue', alpha=0.7, label='Athletes')

x_line = np.array([np.min(age), np.max(age)])
y_line = slope * x_line + intercept

plt.plot(x_line, y_line, color='red', linewidth=2, label=f'Trend (y = {slope:.2f}x + {intercept:.2f})')

plt.title('Athlete Performance: Age vs. Sprint Speed')
plt.xlabel('Age (years)')
plt.ylabel('Sprint Speed (m/s)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()