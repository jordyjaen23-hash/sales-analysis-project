import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# PATH
# =========================
path = r"C:\Users\jordy\OneDrive\Escritorio\Proyecto Ventas\sales.csv.csv"

print("Existe archivo:", os.path.exists(path))

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(path, encoding="latin1", sep=None, engine="python")

print("\nDataset Info:")
print(df.info())

print("\nColumnas:")
print(df.columns)

# =========================
# DATE FIX
# =========================
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# =========================
# CLEANING
# =========================
df.dropna(inplace=True)

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# =========================
# ANALYSIS
# =========================

total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

sales_by_month = df.groupby('Month')['Sales'].sum().sort_index()
sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
profit_by_category = df.groupby('Category')['Profit'].sum()

print("\nSales by Month:")
print(sales_by_month)

print("\nSales by Category:")
print(sales_by_category)

print("\nTop Products:")
print(top_products)

print("\nProfit by Category:")
print(profit_by_category)

# =========================
# GRAPHS (SAVED IN IMAGES/)
# =========================

# Sales by Month
plt.figure()
sales_by_month.plot(kind='bar')
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("images/sales_by_month.png")
plt.close()

# Sales by Category
plt.figure()
sales_by_category.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("images/sales_by_category.png")
plt.close()

# Top Products
plt.figure()
top_products.plot(kind='barh')
plt.title("Top Products")
plt.gca().invert_yaxis()
plt.savefig("images/top_products.png")
plt.close()

# Profit by Category
plt.figure()
profit_by_category.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.savefig("images/profit_by_category.png")
plt.close()

print("\nAnalysis complete. Graphs saved in 'images/' folder.")
