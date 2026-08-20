# ============================================================
# PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA)
# DecodeLabs Data Analytics Internship 2026
# ============================================================

import pandas as pd
import numpy as np

# ─────────────────────────────────────────
# STEP 1: LOAD THE CLEANED DATASET
# ─────────────────────────────────────────
print("=" * 60)
print("PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

df = pd.read_excel("Cleaned_Dataset.xlsx", engine='openpyxl')
print(f"\n✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")


# ─────────────────────────────────────────
# STEP 2: BASIC STATISTICS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2: BASIC STATISTICS (Mean, Median, Count)")
print("=" * 60)

# Numeric columns summary
print("\n📊 Descriptive Statistics for Numeric Columns:\n")
numeric_stats = df[['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']].describe()
print(numeric_stats.round(2))

# Mean and Median specifically
print("\n📈 Mean Values:")
print(f"   Quantity     : {df['Quantity'].mean():.2f}")
print(f"   UnitPrice    : ${df['UnitPrice'].mean():.2f}")
print(f"   TotalPrice   : ${df['TotalPrice'].mean():.2f}")
print(f"   ItemsInCart  : {df['ItemsInCart'].mean():.2f}")

print("\n📉 Median Values:")
print(f"   Quantity     : {df['Quantity'].median():.2f}")
print(f"   UnitPrice    : ${df['UnitPrice'].median():.2f}")
print(f"   TotalPrice   : ${df['TotalPrice'].median():.2f}")
print(f"   ItemsInCart  : {df['ItemsInCart'].median():.2f}")

print("\n🔢 Count of Records per Category:")
print(f"   Total Orders         : {df.shape[0]}")
print(f"   Unique Customers     : {df['CustomerID'].nunique()}")
print(f"   Unique Products      : {df['Product'].nunique()}")
print(f"   Unique Payment Methods: {df['PaymentMethod'].nunique()}")


# ─────────────────────────────────────────
# STEP 3: TRENDS ANALYSIS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3: TRENDS ANALYSIS")
print("=" * 60)

# Monthly Order Trends
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

monthly_orders = df.groupby('Month').agg(
    Order_Count=('OrderID', 'count'),
    Total_Revenue=('TotalPrice', 'sum'),
    Avg_Order_Value=('TotalPrice', 'mean')
).reset_index()

print("\n📅 Monthly Order Trends:")
print(monthly_orders.to_string(index=False))

# Best & Worst months
best_month = monthly_orders.loc[monthly_orders['Total_Revenue'].idxmax()]
worst_month = monthly_orders.loc[monthly_orders['Total_Revenue'].idxmin()]
print(f"\n🏆 Best Revenue Month  : {best_month['Month']} (${best_month['Total_Revenue']:.2f})")
print(f"📉 Lowest Revenue Month: {worst_month['Month']} (${worst_month['Total_Revenue']:.2f})")

# Product Performance
print("\n📦 Revenue by Product:")
product_revenue = df.groupby('Product').agg(
    Total_Revenue=('TotalPrice', 'sum'),
    Avg_Price=('UnitPrice', 'mean'),
    Total_Quantity=('Quantity', 'sum'),
    Order_Count=('OrderID', 'count')
).sort_values('Total_Revenue', ascending=False)
print(product_revenue.round(2).to_string())

# Payment Method Trends
print("\n💳 Revenue by Payment Method:")
payment_revenue = df.groupby('PaymentMethod').agg(
    Order_Count=('OrderID', 'count'),
    Total_Revenue=('TotalPrice', 'sum')
).sort_values('Total_Revenue', ascending=False)
print(payment_revenue.round(2).to_string())

# Order Status Distribution
print("\n📋 Order Status Breakdown:")
status_breakdown = df.groupby('OrderStatus').agg(
    Order_Count=('OrderID', 'count'),
    Total_Revenue=('TotalPrice', 'sum'),
    Percentage=('OrderID', lambda x: f"{len(x)/len(df)*100:.1f}%")
)
print(status_breakdown.to_string())

# Referral Source Analysis
print("\n🔗 Referral Source Performance:")
referral_stats = df.groupby('ReferralSource').agg(
    Order_Count=('OrderID', 'count'),
    Total_Revenue=('TotalPrice', 'sum'),
    Avg_Order_Value=('TotalPrice', 'mean')
).sort_values('Total_Revenue', ascending=False)
print(referral_stats.round(2).to_string())


# ─────────────────────────────────────────
# STEP 4: OUTLIER DETECTION
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 4: OUTLIER DETECTION (IQR Method)")
print("=" * 60)

def detect_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound, Q1, Q3, IQR

for col in ['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']:
    outliers, lb, ub, q1, q3, iqr = detect_outliers(df, col)
    print(f"\n📊 {col}:")
    print(f"   Q1 = {q1:.2f} | Q3 = {q3:.2f} | IQR = {iqr:.2f}")
    print(f"   Lower Bound = {lb:.2f} | Upper Bound = {ub:.2f}")
    print(f"   Outliers Found: {len(outliers)}")
    if len(outliers) > 0:
        print(f"   ⚠️  Outlier range: {outliers[col].min():.2f} – {outliers[col].max():.2f}")


# ─────────────────────────────────────────
# STEP 5: CORRELATION ANALYSIS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 5: CORRELATION ANALYSIS")
print("=" * 60)

correlation = df[['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']].corr()
print("\n📈 Correlation Matrix:")
print(correlation.round(3).to_string())

print("\n🔑 Key Correlations:")
print(f"   Quantity ↔ TotalPrice  : {correlation.loc['Quantity', 'TotalPrice']:.3f}")
print(f"   UnitPrice ↔ TotalPrice : {correlation.loc['UnitPrice', 'TotalPrice']:.3f}")
print(f"   ItemsInCart ↔ TotalPrice: {correlation.loc['ItemsInCart', 'TotalPrice']:.3f}")


# ─────────────────────────────────────────
# STEP 6: COUPON CODE ANALYSIS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 6: COUPON CODE ANALYSIS")
print("=" * 60)

coupon_usage = df['CouponCode'].value_counts()
print(f"\n🎟️  Orders WITH coupon   : {(df['CouponCode'] != 'NONE').sum()}")
print(f"🚫 Orders WITHOUT coupon: {(df['CouponCode'] == 'NONE').sum()}")

coupon_orders = df[df['CouponCode'] != 'NONE']
no_coupon_orders = df[df['CouponCode'] == 'NONE']
print(f"\n💰 Avg Order Value WITH coupon   : ${coupon_orders['TotalPrice'].mean():.2f}")
print(f"💰 Avg Order Value WITHOUT coupon: ${no_coupon_orders['TotalPrice'].mean():.2f}")

print("\n🏷️  Top Coupon Codes Used:")
top_coupons = coupon_orders['CouponCode'].value_counts().head(10)
print(top_coupons.to_string())


# ─────────────────────────────────────────
# STEP 7: KEY OBSERVATIONS SUMMARY
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 7: KEY OBSERVATIONS & INSIGHTS")
print("=" * 60)

total_revenue = df['TotalPrice'].sum()
avg_order = df['TotalPrice'].mean()
top_product = product_revenue.index[0]
top_payment = payment_revenue.index[0]
cancel_rate = (df['OrderStatus'] == 'Cancelled').sum() / len(df) * 100
return_rate = (df['OrderStatus'] == 'Returned').sum() / len(df) * 100

print(f"""
📋 KEY OBSERVATIONS:
─────────────────────────────────────────
1. 💰 REVENUE OVERVIEW
   • Total Revenue: ${total_revenue:,.2f}
   • Average Order Value: ${avg_order:.2f}
   • Total Orders: {len(df)}

2. 📦 PRODUCT INSIGHTS
   • Top Revenue Product: {top_product}
   • {df['Product'].nunique()} unique products in catalog

3. 💳 PAYMENT TRENDS
   • Most Popular Payment: {top_payment}
   • {df['PaymentMethod'].nunique()} payment methods available

4. ⚠️  RISK INDICATORS
   • Cancellation Rate: {cancel_rate:.1f}%
   • Return Rate: {return_rate:.1f}%
   • Combined Loss Rate: {cancel_rate + return_rate:.1f}%

5. 🎟️  COUPON IMPACT
   • {(df['CouponCode'] != 'NONE').sum()} orders used coupons ({(df['CouponCode'] != 'NONE').sum()/len(df)*100:.1f}%)
   • Avg with coupon: ${coupon_orders['TotalPrice'].mean():.2f}
   • Avg without coupon: ${no_coupon_orders['TotalPrice'].mean():.2f}

6. 📅 TIME TRENDS
   • Best Month: {best_month['Month']}
   • Weakest Month: {worst_month['Month']}
─────────────────────────────────────────
""")

# ─────────────────────────────────────────
# STEP 8: SAVE EDA REPORT
# ─────────────────────────────────────────
print("=" * 60)
print("STEP 8: SAVING EDA REPORT...")
print("=" * 60)

# Save summary stats to Excel
with pd.ExcelWriter("EDA_Report.xlsx", engine='openpyxl') as writer:
    numeric_stats.to_excel(writer, sheet_name='Basic_Statistics')
    monthly_orders.to_excel(writer, sheet_name='Monthly_Trends', index=False)
    product_revenue.to_excel(writer, sheet_name='Product_Analysis')
    payment_revenue.to_excel(writer, sheet_name='Payment_Analysis')
    correlation.to_excel(writer, sheet_name='Correlation_Matrix')

print("✅ EDA_Report.xlsx saved!")
print("\n🎉 PROJECT 2: EDA COMPLETE! Ready for submission!")
print("=" * 60)