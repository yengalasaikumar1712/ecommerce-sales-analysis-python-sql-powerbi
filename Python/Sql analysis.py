import sqlite3
import pandas as pd

# Connect to database
database_path = r"D:\E - commerence analytics\ecommerce.db"

connection = sqlite3.connect(database_path)


# ==========================================
# 1. TOTAL PROFIT
# ==========================================

query = """
SELECT
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOTAL PROFIT ==========")
print(result)


# ==========================================
# 2. TOTAL ORDERS
# ==========================================

query = """
SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_sales;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOTAL ORDERS ==========")
print(result)

# ==========================================
# 3. TOTAL CUSTOMERS
# ==========================================

query = """
SELECT
    COUNT(DISTINCT Customer_Name) AS Total_Customers
FROM ecommerce_sales;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOTAL CUSTOMERS ==========")
print(result)
# ==========================================
# 4. SALES BY PRODUCT CATEGORY
# ==========================================

query = """
SELECT
    Product_Category,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== SALES BY PRODUCT CATEGORY ==========")
print(result)

# ==========================================
# 5. TOP 10 PRODUCTS BY SALES
# ==========================================

query = """
SELECT
    Product_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(result)

# ==========================================
# 6. TOP 10 CUSTOMERS BY SALES
# ==========================================

query = """
SELECT
    Customer_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
print(result)

# ==========================================
# 7. SALES BY COUNTRY
# ==========================================

query = """
SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== SALES BY COUNTRY ==========")
print(result)

# ==========================================
# 8. TOP 10 COUNTRIES BY SALES
# ==========================================

query = """
SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\n========== TOP 10 COUNTRIES BY SALES ==========")
print(result)

# ==========================================
# 9. SALES BY REGION
# ==========================================

query = """
SELECT
    Region,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== SALES BY REGION ==========")
print(result)

# ==========================================
# 10. SALES BY PAYMENT METHOD
# ==========================================

query = """
SELECT
    Payment_Method,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== SALES BY PAYMENT METHOD ==========")
print(result)

# ==========================================
# 11. MONTHLY SALES
# ==========================================

query = """
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;
"""

result = pd.read_sql_query(query, connection)

print("\n========== MONTHLY SALES ==========")
print(result)

# ==========================================
# 12. LOSS-MAKING ORDERS
# ==========================================

query = """
SELECT
    COUNT(*) AS Loss_Making_Orders,
    SUM(Profit) AS Total_Loss
FROM ecommerce_sales
WHERE Profit < 0;
"""

result = pd.read_sql_query(query, connection)

print("\n========== LOSS-MAKING ORDERS ==========")
print(result)

# ==========================================
# 13. LOSS BY PRODUCT CATEGORY
# ==========================================

query = """
SELECT
    Product_Category,
    SUM(Profit) AS Total_Loss
FROM ecommerce_sales
WHERE Profit < 0
GROUP BY Product_Category
ORDER BY Total_Loss ASC;
"""

result = pd.read_sql_query(query, connection)

print("\n========== LOSS BY CATEGORY ==========")
print(result)

# Close connection AFTER all queries
connection.close()