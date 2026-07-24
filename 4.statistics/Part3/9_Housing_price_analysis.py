# Housing Price Analysis 
# Compare price distributions across neighborhoods with box plot
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
suburban = np.random.normal(350000, 50000, 100)
urban = np.random.lognormal(12.8, 0.3, 100)
rural = np.random.exponential(250000, 100) + 150000

neighborhood_data = [suburban, urban, rural]
neighborhood_names = ['Suburban', 'Urban', 'Rural']

print("Housing Price Statistical Comparison ")
for i in range(len(neighborhood_names)):
    prices = neighborhood_data[i]
    name = neighborhood_names[i]
    
    q1 = np.percentile(prices, 25)
    median = np.median(prices)
    q3 = np.percentile(prices, 75)
    
    iqr = q3 - q1
    
    print(name)
    print("  Median Price: %.2f " %median)
    print("  IQR (Spread):%.2f " %iqr)


plt.figure(figsize=(10, 6))

plt.boxplot(neighborhood_data, label=neighborhood_names, patch_artist=True, 
            boxprops=dict(facecolor='lightgreen', color='darkgreen'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', color='darkgreen', alpha=0.5))

plt.title('Housing Price Distribution by Neighborhood')
plt.ylabel('Price ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()