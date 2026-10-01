-- =====================================================
-- E-COMMERCE SALES & CUSTOMER ANALYTICS
-- SQL QUERIES
-- =====================================================


-- 1. VIEW FIRST 10 RECORDS
-- =====================================================

SELECT *
FROM ecommerce_sales
LIMIT 10;


-- 2. TOTAL SALES
-- =====================================================

SELECT
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales;


-- 3. TOTAL PROFIT
-- =====================================================

SELECT
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales;


-- 4. TOTAL ORDERS
-- =====================================================

SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_sales;


-- 5. TOTAL CUSTOMERS
-- =====================================================

SELECT
    COUNT(DISTINCT Customer_Name) AS Total_Customers
FROM ecommerce_sales;


-- 6. TOTAL QUANTITY SOLD
-- =====================================================

SELECT
    SUM(Quantity) AS Total_Quantity_Sold
FROM ecommerce_sales;


-- 7. AVERAGE ORDER VALUE
-- =====================================================

SELECT
    AVG(Total_Sales) AS Average_Order_Value
FROM ecommerce_sales;


-- 8. SALES BY PRODUCT CATEGORY
-- =====================================================

SELECT
    Product_Category,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;


-- 9. PROFIT BY PRODUCT CATEGORY
-- =====================================================

SELECT
    Product_Category,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Profit DESC;


-- 10. TOP 10 PRODUCTS BY SALES
-- =====================================================

SELECT
    Product_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;


-- 11. TOP 10 CUSTOMERS BY SALES
-- =====================================================

SELECT
    Customer_Name,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;


-- 12. SALES BY CUSTOMER SEGMENT
-- =====================================================

SELECT
    Customer_Segment,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_Segment
ORDER BY Total_Sales DESC;


-- 13. PROFIT BY CUSTOMER SEGMENT
-- =====================================================

SELECT
    Customer_Segment,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Customer_Segment
ORDER BY Total_Profit DESC;


-- 14. SALES BY COUNTRY
-- =====================================================

SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC;


-- 15. TOP 10 COUNTRIES BY SALES
-- =====================================================

SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 10;


-- 16. SALES BY REGION
-- =====================================================

SELECT
    Region,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;


-- 17. SALES BY PAYMENT METHOD
-- =====================================================

SELECT
    Payment_Method,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;


-- 18. ORDERS BY PAYMENT METHOD
-- =====================================================

SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Orders DESC;


-- 19. MONTHLY SALES
-- =====================================================

SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Total_Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;


-- 20. MONTHLY PROFIT
-- =====================================================

SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;


-- 21. SALES AND PROFIT BY MONTH
-- =====================================================

SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Month
ORDER BY Month;


-- 22. LOSS-MAKING ORDERS
-- =====================================================

SELECT
    COUNT(*) AS Loss_Making_Orders,
    SUM(Profit) AS Total_Loss
FROM ecommerce_sales
WHERE Profit < 0;


-- 23. LOSS BY PRODUCT CATEGORY
-- =====================================================

SELECT
    Product_Category,
    SUM(Profit) AS Total_Loss
FROM ecommerce_sales
WHERE Profit < 0
GROUP BY Product_Category
ORDER BY Total_Loss ASC;


-- 24. ORDERS WITH DISCOUNT
-- =====================================================

SELECT
    Discount_Percent,
    COUNT(*) AS Number_of_Orders
FROM ecommerce_sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;


-- 25. DISCOUNT VS PROFIT
-- =====================================================

SELECT
    Discount_Percent,
    SUM(Profit) AS Total_Profit,
    AVG(Profit) AS Average_Profit,
    COUNT(*) AS Number_of_Orders
FROM ecommerce_sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;


-- 26. CATEGORY SALES AND PROFIT
-- =====================================================

SELECT
    Product_Category,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;


-- 27. COUNTRY SALES AND PROFIT
-- =====================================================

SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC;


-- 28. REGION SALES AND PROFIT
-- =====================================================

SELECT
    Region,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;


-- 29. MOST PROFITABLE PRODUCTS
-- =====================================================

SELECT
    Product_Name,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;


-- 30. LEAST PROFITABLE PRODUCTS
-- =====================================================

SELECT
    Product_Name,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Profit ASC
LIMIT 10;