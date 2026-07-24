# Advertising Spend vs. Revenue
# Quantify correlation and visualize with a scatter plot
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(42)
spend = np.linspace(1000, 10000, 12)
revenue = 5000 + 2.5 * spend + np.random.normal(0, 1000, 12)

r_value, p_value = pearsonr(spend, revenue)

print("Pearson's R: %.2f" % r_value)
print("P-value: %.2f" %p_value)

plt.figure(figsize=(8, 6))

plt.scatter(spend, revenue, color='green', alpha=0.7, s=80, label='Monthly Data')

annotation_text = "Pearson's R = %.2f\np-value = %.2e" % (r_value, p_value)

plt.text(0.05, 0.95, annotation_text, transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', 
         bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray', alpha=0.8))

plt.title('Advertising Spend vs. Revenue (12 Months)')
plt.xlabel('Monthly Ad Spend ($)')
plt.ylabel('Monthly Revenue ($)')
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()