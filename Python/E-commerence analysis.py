import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = r"D:\E - commerence analytics\Data\global_ecommerce_sales.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. DATA UNDERSTANDING
# ==========================================

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATASET INFORMATION ==========")
print(df.info())


# ==========================================
# 3. DATA CLEANING
# ==========================================

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== UNIQUE VALUES ==========")
print(df.nunique())


# ==========================================
# 4. BASIC STATISTICS
# ==========================================

print("\n========== BASIC STATISTICS ==========")
print(df.describe())


# ==========================================
# 5. BASIC BUSINESS METRICS
# ==========================================

total_sales = df["Total_Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_Name"].nunique()

total_quantity = df["Quantity"].sum()

average_order_value = total_sales / total_orders


print("\n========== BUSINESS METRICS ==========")

print("Total Sales:", round(total_sales, 2))

print("Total Profit:", round(total_profit, 2))

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

print("Total Quantity Sold:", total_quantity)

print("Average Order Value:", round(average_order_value, 2))


# ==========================================
# 6. SALES BY PRODUCT CATEGORY
# ==========================================

category_sales = (
    df.groupby("Product_Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY CATEGORY ==========")

print(category_sales)


# ==========================================
# 7. SALES BY CATEGORY - CHART
# ==========================================

category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\sales_by_category.png"
)

plt.close()


# ==========================================
# 8. PROFIT BY PRODUCT CATEGORY
# ==========================================

profit_by_category = (
    df.groupby("Product_Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== PROFIT BY CATEGORY ==========")

print(profit_by_category)


# ==========================================
# 9. PROFIT BY CATEGORY - CHART
# ==========================================

profit_by_category.plot(kind="bar")

plt.title("Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\profit_by_category.png"
)

plt.close()


# ==========================================
# 10. COMPLETION MESSAGE
# ==========================================

print("\n==========================================")
print("Analysis completed successfully!")
print("Charts saved in the Screenshots folder.")
print("==========================================")
# ==========================================
# 11. MONTHLY SALES ANALYSIS
# ==========================================

# Create a Month column
df["Month"] = df["Order_Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = (
    df.groupby("Month")["Total_Sales"]
    .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)
# ==========================================
# 12. MONTHLY SALES - LINE CHART
# ==========================================

plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig(
    r"D:\E - commerence analytics\Screenshots\monthly_sales_trend.png"
)

plt.close()

print("\nMonthly sales chart saved successfully!")
# ==========================================
# 13. TOP 10 PRODUCTS BY SALES
# ==========================================

top_products = (
    df.groupby("Product_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(top_products)
# ==========================================
# 14. TOP 10 PRODUCTS - CHART
# ==========================================

plt.figure(figsize=(12, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\top_10_products_sales.png"
)

plt.close()

print("\nTop 10 products chart saved successfully!")
# ==========================================
# 15. TOP 10 CUSTOMERS BY SALES
# ==========================================

top_customers = (
    df.groupby("Customer_Name")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
print(top_customers)
# ==========================================
# 16. SALES BY CUSTOMER SEGMENT
# ==========================================

segment_sales = (
    df.groupby("Customer_Segment")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY CUSTOMER SEGMENT ==========")
print(segment_sales)
# ==========================================
# 17. PROFIT BY CUSTOMER SEGMENT
# ==========================================

segment_profit = (
    df.groupby("Customer_Segment")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== PROFIT BY CUSTOMER SEGMENT ==========")
print(segment_profit)
# ==========================================
# 18. CUSTOMER SEGMENT ANALYSIS - CHART
# ==========================================

segment_analysis = df.groupby("Customer_Segment")[[
    "Total_Sales",
    "Profit"
]].sum()

segment_analysis.plot(kind="bar", figsize=(10, 6))

plt.title("Sales and Profit by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Amount")

plt.xticks(rotation=0)
plt.legend(["Total Sales", "Profit"])

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\customer_segment_analysis.png"
)

plt.close()

print("\nCustomer segment chart saved successfully!")
# ==========================================
# 19. SALES BY COUNTRY
# ==========================================

country_sales = (
    df.groupby("Country")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY COUNTRY ==========")
print(country_sales)
# ==========================================
# 20. TOP 10 COUNTRIES BY SALES
# ==========================================

top_countries = country_sales.head(10)

print("\n========== TOP 10 COUNTRIES BY SALES ==========")
print(top_countries)
# ==========================================
# 21. TOP 10 COUNTRIES - CHART
# ==========================================

plt.figure(figsize=(12, 6))

top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\top_10_countries_sales.png"
)

plt.close()

print("\nTop 10 countries chart saved successfully!")
# ==========================================
# 22. SALES BY REGION
# ==========================================

region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY REGION ==========")
print(region_sales)
# ==========================================
# 23. SALES BY REGION - CHART
# ==========================================

plt.figure(figsize=(10, 6))

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\sales_by_region.png"
)

plt.close()

print("\nRegional sales chart saved successfully!")
# ==========================================
# 24. SALES BY PAYMENT METHOD
# ==========================================

payment_sales = (
    df.groupby("Payment_Method")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY PAYMENT METHOD ==========")
print(payment_sales)
# ==========================================
# 25. PAYMENT METHOD - CHART
# ==========================================

plt.figure(figsize=(10, 6))

payment_sales.plot(kind="bar")

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\sales_by_payment_method.png"
)

plt.close()

print("\nPayment method chart saved successfully!")
# ==========================================
# 26. DISCOUNT ANALYSIS
# ==========================================

discount_analysis = (
    df.groupby("Discount_Percent")["Profit"]
    .agg(["sum", "mean", "count"])
    .sort_index()
)

print("\n========== DISCOUNT vs PROFIT ==========")
print(discount_analysis)
# ==========================================
# 27. DISCOUNT vs PROFIT - CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    discount_analysis.index,
    discount_analysis["mean"],
    marker="o"
)

plt.title("Average Profit by Discount Percentage")
plt.xlabel("Discount Percentage")
plt.ylabel("Average Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\discount_vs_profit.png"
)

plt.close()

print("\nDiscount analysis chart saved successfully!")
# ==========================================
# 28. LOSS-MAKING ORDERS
# ==========================================

loss_orders = df[df["Profit"] < 0]

print("\n========== LOSS-MAKING ORDERS ==========")

print("Number of Loss-Making Orders:", len(loss_orders))

print("Total Loss:", round(loss_orders["Profit"].sum(), 2))

print("\nLoss-Making Orders by Category:")
print(
    loss_orders.groupby("Product_Category")["Profit"]
    .sum()
    .sort_values()
)
# ==========================================
# 29. LOSS-MAKING ORDERS - CHART
# ==========================================

loss_by_category = (
    loss_orders.groupby("Product_Category")["Profit"]
    .sum()
    .sort_values()
)

plt.figure(figsize=(10, 6))

loss_by_category.plot(kind="bar")

plt.title("Losses by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Loss")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"D:\E - commerence analytics\Screenshots\loss_by_category.png"
)

plt.close()

print("\nLoss analysis chart saved successfully!")
# ==========================================
# 30. CREATE SQL DATABASE
# ==========================================

import sqlite3

database_path = r"D:\E - commerence analytics\ecommerce.db"

# Connect to SQLite database
connection = sqlite3.connect(database_path)

# Make a copy of dataframe
sql_df = df.copy()

# Convert Order_Date to text
sql_df["Order_Date"] = sql_df["Order_Date"].dt.strftime("%Y-%m-%d")

# Convert Month from Period to text
sql_df["Month"] = sql_df["Month"].astype(str)

# Create SQLite table
sql_df.to_sql(
    "ecommerce_sales",
    connection,
    if_exists="replace",
    index=False
)

# Check number of rows
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM ecommerce_sales")

row_count = cursor.fetchone()[0]

print("\n========== SQL DATABASE ==========")
print("Rows inserted:", row_count)

connection.close()