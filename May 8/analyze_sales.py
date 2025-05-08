import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv(r'C:\Users\Acer\WEEK 1\May 8\sales_data.csv')

# Display basic info
print("Dataframe Head:\n", df.head())
print("\nDataframe Info:\n")
print(df.info())
print("\nDescriptive Stats:\n", df.describe())

# Group by product and sum units sold
product_sales = df.groupby('Product')['Units_Sold'].sum()
print("\nTotal Units Sold per Product:\n", product_sales)

# Save grouped data to CSV
product_sales.to_csv('May 8/product_sales_summary.csv')

# Plot a bar chart of total units sold per product
product_sales.plot(kind='bar', color='skyblue', title='Total Units Sold per Product')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('May 8/product_sales_chart.png')
plt.show()

# Extract the 'Units_Sold' column from the DataFrame as a NumPy array
units = df['Units_Sold'].values

# Calculate the mean (average) of units sold
mean_units = np.mean(units)

# Calculate the median (middle value) of units sold
median_units = np.median(units)

# Calculate the standard deviation (spread of data) of units sold
std_dev_units = np.std(units)

# Print the calculated statistics
print(f"\nMean Units Sold: {mean_units}")
print(f"Median Units Sold: {median_units}")
print(f"Standard Deviation of Units Sold: {std_dev_units}")
