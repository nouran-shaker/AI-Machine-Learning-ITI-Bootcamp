# Income Distribution Across Professions 
# Compare distributions with box plots
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
engineers = np.random.exponential(80000, 100) + 40000
teachers = np.random.normal(55000, 8000, 100)
artists = np.random.lognormal(10.5, 0.4, 100)

incomes_data = [engineers, teachers, artists]
professions = ['Engineers', 'Teachers', 'Artists']

for i in range(len(professions)):
    data = incomes_data[i]
    profession_name = professions[i]
    
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    
    print("Median: %.2f" % median)
    print("IQR: %.2f" %iqr)
    print("Number of Outliers: ",len(outliers))


plt.figure(figsize=(10, 6))


plt.boxplot(incomes_data, label=professions, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', color='red', alpha=0.5))

plt.title('Income Distribution Across Professions')
plt.ylabel('Income ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()