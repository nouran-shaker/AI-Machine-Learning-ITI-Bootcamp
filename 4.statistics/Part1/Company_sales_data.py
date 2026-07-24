import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("company_sales_data.csv")

# Part 1: Read Total profit of all months and show it using a line plot

plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'])
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Company profit per month')
plt.xticks(df['month_number'])
plt.show()

# Part 2: Get total profit of all months and show line plot with specific style properties

plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'], label='Profit data of last year',
         color='red', marker='o', markerfacecolor='black', linestyle='--', linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Company Sales data of last year')
plt.xticks(df['month_number'])
plt.legend(loc='lower right')
plt.show()

# Part 3: Read all product sales data and show it using a multiline plot

plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['facecream'], label='Face cream Sales Data', marker='o', linewidth=3)
plt.plot(df['month_number'], df['facewash'], label='Face Wash Sales Data', marker='o', linewidth=3)
plt.plot(df['month_number'], df['toothpaste'], label='ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(df['month_number'], df['bathingsoap'], label='BathingSoap Sales Data', marker='o', linewidth=3)
plt.plot(df['month_number'], df['shampoo'], label='Shampoo Sales Data', marker='o', linewidth=3)
plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.xticks(df['month_number'])
plt.legend(loc='upper left')
plt.show()


# Part 4: Read toothpaste sales data of each month and show it using a scatter plot

plt.figure(figsize=(8, 5))
plt.scatter(df['month_number'], df['toothpaste'], label='Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Tooth paste Sales data')
plt.xticks(df['month_number'])
plt.grid(True, linestyle='--')
plt.legend(loc='upper left')
plt.show()


# Part 5: Read face cream and facewash product sales data and show it using a bar chart

plt.figure(figsize=(8, 5))
# Using NumPy to offset the bars side-by-side

x = np.arange(len(df['month_number'])) 
width = 0.25

plt.bar(x - width/2, df['facecream'], width, label='Face Cream sales data')
plt.bar(x + width/2, df['facewash'], width, label='Face Wash sales data')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Facewash and facecream sales data')
plt.xticks(x, df['month_number'])
plt.grid(True, linestyle='--')
plt.legend(loc='upper left')
plt.show()


# Part 6: Read sales data of bathing soap of all months and show it using a bar chart. Save plot.

plt.figure(figsize=(8, 5))
plt.bar(df['month_number'], df['bathingsoap'])
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('bathingsoap sales data')
plt.xticks(df['month_number'])
plt.grid(True, linestyle='--')
plt.savefig('bathingsoap_sales_data.png') 
plt.show()


# Part 7: Read the total profit of each month and show it using a histogram

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(df['total_profit'], profit_range, label='Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.title('Profit data')
plt.legend(loc='upper left')
plt.show()


# Part 8: Calculate total sale data for last year for each product and show it using a Pie chart

plt.figure(figsize=(8, 5))
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
sales_data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), 
              df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]

plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.title('Sales data')
plt.legend(loc='lower right')
plt.show()


# Part 9: Read Bathing soap and facewash of all months and display it using Subplots

fig, ax = plt.subplots(2, sharex=True, figsize=(8, 6))

ax[0].plot(df['month_number'], df['bathingsoap'], color='black', marker='o', linewidth=3)
ax[0].set_title('Sales data of a Bathingsoap')

ax[1].plot(df['month_number'], df['facewash'], color='red', marker='o', linewidth=3)
ax[1].set_title('Sales data of a facewash')

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks(df['month_number'])
plt.show()


# Part 10: Read all product sales data and show it using a stack plot

plt.figure(figsize=(8, 5))
plt.stackplot(df['month_number'], df['facecream'], df['facewash'], df['toothpaste'], 
              df['bathingsoap'], df['shampoo'], df['moisturizer'], 
              labels=['face Cream', 'Face wash', 'Tooth paste', 'Bathing soap', 'Shampoo', 'Moisturizer'],
              colors=['m', 'c', 'r', 'k', 'g', 'y'])

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()