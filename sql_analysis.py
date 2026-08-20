# ============================================================
# PROJECT 3: SQL DATA ANALYSIS
# DecodeLabs Data Analytics Internship 2026
# ============================================================

import pandas as pd
import sqlite3

# ─────────────────────────────────────────
# STEP 1: LOAD DATASET INTO SQL DATABASE
# ─────────────────────────────────────────
print("=" * 60)
print("PROJECT 3: SQL DATA ANALYSIS")
print("=" * 60)

# Load cleaned dataset
df = pd.read_excel("Cleaned_Dataset.xlsx", engine='openpyxl')

# Create SQLite database in memory
conn = sqlite3.connect("decodelabs.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

print("✅ Dataset loaded into SQLite database!")
print(f"   Table: 'orders' | Rows: {len(df)} | Columns: {len(df.columns)}")


# ─────────────────────────────────────────
# HELPER FUNCTION
# ─────────────────────────────────────────
def run_query(title, query):
    print(f"\n{'─' * 60}")
    print(f"📌 {title}")
    print(f"{'─' * 60}")
    print(f"SQL: {query}\n")
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))
    return result


# ═══════════════════════════════════════════════════════════
# PART A: SELECT QUERIES
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART A: SELECT QUERIES")
print("=" * 60)

# Query 1: Select all columns (first 10 rows)
run_query("Query 1: Select first 10 orders",
    "SELECT * FROM orders LIMIT 10")

# Query 2: Select specific columns
run_query("Query 2: Select OrderID, Product, TotalPrice",
    "SELECT OrderID, Product, TotalPrice FROM orders LIMIT 10")

# Query 3: Select distinct products
run_query("Query 3: All unique products",
    "SELECT DISTINCT Product FROM orders")

# Query 4: Select distinct payment methods
run_query("Query 4: All unique payment methods",
    "SELECT DISTINCT PaymentMethod FROM orders")

# Query 5: Select distinct order statuses
run_query("Query 5: All unique order statuses",
    "SELECT DISTINCT OrderStatus FROM orders")


# ═══════════════════════════════════════════════════════════
# PART B: WHERE (FILTERING) QUERIES
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART B: WHERE - FILTERING DATA")
print("=" * 60)

# Query 6: Orders with TotalPrice > $2000
run_query("Query 6: High-value orders (TotalPrice > $2000)",
    "SELECT OrderID, Product, Quantity, TotalPrice FROM orders WHERE TotalPrice > 2000 LIMIT 10")

# Query 7: Cancelled orders
run_query("Query 7: Cancelled orders",
    "SELECT OrderID, Product, TotalPrice, CustomerID FROM orders WHERE OrderStatus = 'Cancelled' LIMIT 10")

# Query 8: Laptop orders only
run_query("Query 8: All Laptop orders",
    "SELECT OrderID, CustomerID, Quantity, TotalPrice FROM orders WHERE Product = 'Laptop' LIMIT 10")

# Query 9: Orders paid by Credit Card
run_query("Query 9: Credit Card payments",
    "SELECT OrderID, Product, TotalPrice FROM orders WHERE PaymentMethod = 'Credit Card' LIMIT 10")

# Query 10: Orders with coupon used
run_query("Query 10: Orders with coupons",
    "SELECT OrderID, Product, CouponCode, TotalPrice FROM orders WHERE CouponCode != 'NONE' LIMIT 10")

# Query 11: Orders between $500 and $1500
run_query("Query 11: Orders between $500 and $1500",
    "SELECT OrderID, Product, TotalPrice FROM orders WHERE TotalPrice BETWEEN 500 AND 1500 LIMIT 10")

# Query 12: Orders from Instagram referral
run_query("Query 12: Instagram referral orders",
    "SELECT OrderID, Product, TotalPrice, ReferralSource FROM orders WHERE ReferralSource = 'Instagram' LIMIT 10")


# ═══════════════════════════════════════════════════════════
# PART C: ORDER BY (SORTING) QUERIES
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART C: ORDER BY - SORTING DATA")
print("=" * 60)

# Query 13: Top 10 most expensive orders
run_query("Query 13: Top 10 most expensive orders",
    "SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice FROM orders ORDER BY TotalPrice DESC LIMIT 10")

# Query 14: Top 10 cheapest orders
run_query("Query 14: Top 10 cheapest orders",
    "SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice FROM orders ORDER BY TotalPrice ASC LIMIT 10")

# Query 15: Orders sorted by date (most recent first)
run_query("Query 15: Most recent orders",
    "SELECT OrderID, Date, Product, TotalPrice FROM orders ORDER BY Date DESC LIMIT 10")

# Query 16: Products sorted alphabetically
run_query("Query 16: Orders sorted by Product name",
    "SELECT OrderID, Product, TotalPrice FROM orders ORDER BY Product ASC LIMIT 10")


# ═══════════════════════════════════════════════════════════
# PART D: GROUP BY (GROUPING) QUERIES
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART D: GROUP BY - GROUPING DATA")
print("=" * 60)

# Query 17: Total revenue by product
run_query("Query 17: Total revenue by Product",
    """SELECT Product, 
              COUNT(*) AS Order_Count, 
              SUM(TotalPrice) AS Total_Revenue,
              ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value
       FROM orders 
       GROUP BY Product 
       ORDER BY Total_Revenue DESC""")

# Query 18: Orders by payment method
run_query("Query 18: Orders by Payment Method",
    """SELECT PaymentMethod, 
              COUNT(*) AS Order_Count, 
              SUM(TotalPrice) AS Total_Revenue
       FROM orders 
       GROUP BY PaymentMethod 
       ORDER BY Total_Revenue DESC""")

# Query 19: Orders by status
run_query("Query 19: Orders by Status",
    """SELECT OrderStatus, 
              COUNT(*) AS Order_Count, 
              SUM(TotalPrice) AS Total_Revenue,
              ROUND(AVG(TotalPrice), 2) AS Avg_Value
       FROM orders 
       GROUP BY OrderStatus 
       ORDER BY Order_Count DESC""")

# Query 20: Revenue by referral source
run_query("Query 20: Revenue by Referral Source",
    """SELECT ReferralSource, 
              COUNT(*) AS Order_Count, 
              SUM(TotalPrice) AS Total_Revenue,
              ROUND(AVG(TotalPrice), 2) AS Avg_Value
       FROM orders 
       GROUP BY ReferralSource 
       ORDER BY Total_Revenue DESC""")

# Query 21: Revenue by coupon code
run_query("Query 21: Revenue by Coupon Code",
    """SELECT CouponCode, 
              COUNT(*) AS Times_Used, 
              ROUND(SUM(TotalPrice), 2) AS Total_Revenue,
              ROUND(AVG(TotalPrice), 2) AS Avg_Value
       FROM orders 
       GROUP BY CouponCode 
       ORDER BY Times_Used DESC""")


# ═══════════════════════════════════════════════════════════
# PART E: AGGREGATION QUERIES (COUNT, SUM, AVG)
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART E: AGGREGATIONS (COUNT, SUM, AVG)")
print("=" * 60)

# Query 22: Total order count
run_query("Query 22: Total number of orders",
    "SELECT COUNT(*) AS Total_Orders FROM orders")

# Query 23: Total revenue
run_query("Query 23: Total revenue",
    "SELECT ROUND(SUM(TotalPrice), 2) AS Total_Revenue FROM orders")

# Query 24: Average order value
run_query("Query 24: Average order value",
    "SELECT ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value FROM orders")

# Query 25: Min and Max order values
run_query("Query 25: Min and Max order values",
    """SELECT ROUND(MIN(TotalPrice), 2) AS Min_Order, 
              ROUND(MAX(TotalPrice), 2) AS Max_Order,
              ROUND(MAX(TotalPrice) - MIN(TotalPrice), 2) AS Range_Value
       FROM orders""")

# Query 26: Count of cancelled orders
run_query("Query 26: Cancelled order count and lost revenue",
    """SELECT COUNT(*) AS Cancelled_Orders, 
              ROUND(SUM(TotalPrice), 2) AS Lost_Revenue
       FROM orders 
       WHERE OrderStatus = 'Cancelled'""")

# Query 27: Average quantity per product
run_query("Query 27: Average quantity ordered per product",
    """SELECT Product, 
              ROUND(AVG(Quantity), 2) AS Avg_Quantity,
              SUM(Quantity) AS Total_Quantity
       FROM orders 
       GROUP BY Product 
       ORDER BY Total_Quantity DESC""")

# Query 28: Count of unique customers
run_query("Query 28: Unique customer count",
    "SELECT COUNT(DISTINCT CustomerID) AS Unique_Customers FROM orders")


# ═══════════════════════════════════════════════════════════
# PART F: ADVANCED QUERIES (HAVING + PERCENTAGE)
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("PART F: ADVANCED - HAVING & CALCULATIONS")
print("=" * 60)

# Query 29: Products with revenue > $180,000
run_query("Query 29: Products with revenue > $180,000 (HAVING)",
    """SELECT Product, 
              ROUND(SUM(TotalPrice), 2) AS Total_Revenue
       FROM orders 
       GROUP BY Product 
       HAVING SUM(TotalPrice) > 180000
       ORDER BY Total_Revenue DESC""")

# Query 30: Percentage contribution by product
run_query("Query 30: Percentage contribution by Product",
    """SELECT Product,
              ROUND(SUM(TotalPrice), 2) AS Revenue,
              ROUND(SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM orders), 2) AS Percentage
       FROM orders
       GROUP BY Product
       ORDER BY Percentage DESC""")


# ─────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("📋 PROJECT 3 SUMMARY")
print("=" * 60)
print(f"""
✅ Total Queries Executed: 30

📌 SQL Concepts Demonstrated:
   • SELECT         — Basic data retrieval
   • WHERE          — Filtering rows
   • ORDER BY       — Sorting results
   • GROUP BY       — Grouping data
   • COUNT()        — Counting records
   • SUM()          — Summing values
   • AVG()          — Calculating averages
   • MIN() / MAX()  — Finding extremes
   • BETWEEN        — Range filtering
   • DISTINCT       — Unique values
   • HAVING         — Filtering groups
   • Subqueries     — Percentage calculations

🎉 PROJECT 3: SQL DATA ANALYSIS COMPLETE!
""")

# Close database connection
conn.close()
print("=" * 60)