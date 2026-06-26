# ============================================
# Sales Data Analysis Project
# Author: Narendra Ankush Surase
# Internship: The Developers Arena
# ============================================

import pandas as pd
print("=" * 60)
print("        SALES DATA ANALYSIS PROJECT")
print("=" * 60)

df = pd.read_csv(r"C:\Users\Narendra\Downloads\sales_data.csv")

print("\nDataset Loaded Successfully!\n")

# -------------------------------
# Display First Five Rows
# -------------------------------

print("First 5 Rows:")
print(df.head())

# -------------------------------
# Dataset Information
# -------------------------------

print("\n" + "="*60)
print("Dataset Information")
print("="*60)

print("Shape :", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInformation:")
df.info()

# -------------------------------
# Missing Values
# -------------------------------

print("\n" + "="*60)
print("Missing Values")
print("="*60)

print(df.isnull().sum())

# Fill Missing Numeric Values

df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Total_Sales"] = df["Total_Sales"].fillna(df["Total_Sales"].mean())

# Remove Duplicate Rows

df.drop_duplicates(inplace=True)

# -------------------------------
# Sales Analysis
# -------------------------------

print("\n" + "="*60)
print("Sales Analysis")
print("="*60)

total_revenue = df["Total_Sales"].sum()

average_sale = df["Total_Sales"].mean()

highest_sale = df["Total_Sales"].max()

lowest_sale = df["Total_Sales"].min()

total_products = df["Quantity"].sum()

best_product = df.groupby("Product")["Quantity"].sum().idxmax()

best_quantity = df.groupby("Product")["Quantity"].sum().max()

print(f"Total Revenue : ₹{total_revenue:,.2f}")
print(f"Average Sale  : ₹{average_sale:,.2f}")
print(f"Highest Sale  : ₹{highest_sale:,.2f}")
print(f"Lowest Sale   : ₹{lowest_sale:,.2f}")
print(f"Total Quantity Sold : {total_products}")

print(f"\nBest Selling Product : {best_product}")
print(f"Units Sold : {best_quantity}")

# -------------------------------
# Region Wise Sales
# -------------------------------

print("\nRegion Wise Sales")

region_sales = df.groupby("Region")["Total_Sales"].sum()

print(region_sales)

# -------------------------------
# Final Report
# -------------------------------

print("\n" + "="*60)
print("FINAL SALES REPORT")
print("="*60)

print(f"Dataset Size          : {df.shape[0]} Rows")
print(f"Number of Columns     : {df.shape[1]}")
print(f"Total Revenue         : ₹{total_revenue:,.2f}")
print(f"Average Sale          : ₹{average_sale:,.2f}")
print(f"Highest Sale          : ₹{highest_sale:,.2f}")
print(f"Lowest Sale           : ₹{lowest_sale:,.2f}")
print(f"Best Selling Product  : {best_product}")
print(f"Total Quantity Sold   : {total_products}")

print("="*60)
print("Analysis Completed Successfully!")
print("="*60)