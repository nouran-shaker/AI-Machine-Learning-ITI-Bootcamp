#Student Exam Scores Analysis
#Analyze score distributions using dot plots, histograms, and z-scores
import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(42)
scores=np.random.normal(70,10,100)

mean=np.mean(scores)
std=np.std(scores)
z_scores=(scores-mean)/std

outlier_condition = (z_scores > 2) | (z_scores < -2)
outliers = scores[outlier_condition]

print("Identified ",len(outliers)," outliers:", outliers)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)

jitter=np.random.uniform(-0.1,0.1,size=len(scores))

plt.scatter(scores,jitter,alpha=0.6,color='blue',label='Outliers')

outlier_jitter = jitter[outlier_condition]
plt.scatter(outliers, outlier_jitter, color='red', label='Outliers')

plt.title('Dot Plot of Student Exam Scores')
plt.xlabel('Score')
plt.yticks([])  
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(scores, bins=10, edgecolor='black', color='skyblue')
plt.title('Histogram of Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()