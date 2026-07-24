# Website Traffic Analysis
# Analyze traffic distribution with histograms and z-scores
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
traffic = np.random.poisson(lam=50, size=744) 

mean_traffic = np.mean(traffic)
std_traffic = np.std(traffic)
z_scores = (traffic - mean_traffic) / std_traffic

anomaly_condition = z_scores > 3
anomalies = traffic[anomaly_condition]

print("Mean Hourly Traffic: %.2f" % mean_traffic)
print("Standard Deviation:%.2f " %std_traffic)
print("Identified ", len(anomalies)," anomalies (Z-score > 3): ",anomalies)

plt.figure(figsize=(10, 6))

plt.hist(traffic, bins=20, edgecolor='black', color='teal', alpha=0.7, label='Normal Traffic Hours')

threshold = mean_traffic + 3 * std_traffic
plt.axvline(threshold, color='red', linestyle='dashed', linewidth=2, label=f'Anomaly Threshold ({threshold:.1f} visits)')

plt.title('Distribution of Hourly Website Traffic (1 Month)')
plt.xlabel('Number of Visits per Hour')
plt.ylabel('Frequency (Hours)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()