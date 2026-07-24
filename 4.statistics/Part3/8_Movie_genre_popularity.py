# Movie Genre Popularity
# Visualize categorical proportions with a pie chart
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']
tickets = np.random.randint(5000, 30000, size=6)

min_idx = np.argmin(tickets)
explode = [0.1 if i == min_idx else 0 for i in range(len(genres))]

plt.figure(figsize=(8, 8))

plt.pie(tickets, labels=genres, explode=explode, autopct='%1.1f%%', 
        startangle=140, colors=plt.cm.Set3.colors)

plt.title('Movie Genre Popularity (Ticket Sales)')
plt.show()