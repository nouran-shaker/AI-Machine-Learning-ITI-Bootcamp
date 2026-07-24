#Fruit Sales Distribution
#Visualize categorical data with a pie chart
import numpy as np
import matplotlib.pyplot as plt


fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
sales = np.random.randint(50, 200, size=5)


explode = [0.1 if s == max(sales) else 0 for s in sales] 


plt.figure(figsize=(8, 8))

plt.pie(sales, labels=fruits, explode=explode, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)

plt.title('Fruit Sales Distribution')
plt.show()