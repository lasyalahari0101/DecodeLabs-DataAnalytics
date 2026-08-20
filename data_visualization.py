# ============================================================
# PROJECT 4: DATA VISUALIZATION - DATA STORYTELLING
# DecodeLabs Data Analytics Internship (Batch 2026)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ============================================================
# CONFIGURATION — Boardroom-Ready Style
# ============================================================
SPOTLIGHT = '#2563EB'
MUTED = '#9CA3AF'
DARK_TEXT = '#1F2937'
LIGHT_BG = '#FFFFFF'
ACCENT_RED = '#DC2626'
ACCENT_GREEN = '#059669'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['figure.facecolor'] = LIGHT_BG
plt.rcParams['axes.facecolor'] = LIGHT_BG
plt.rcParams['figure.dpi'] = 150

# ============================================================
# LOAD DATA
# ============================================================
print("=" * 60)
print("  PROJECT 4: DATA VISUALIZATION - DATA STORYTELLING")
print("  DecodeLabs Data Analytics Internship")
print("=" * 60)
print()

df = pd.read_csv('cleaned_dataset.csv')
print(f"✅ Dataset loaded: {len(df)} rows x {len(df.columns)} columns")
print(f"✅ Columns: {df.columns.tolist()}")
print()

# Parse date
df['Date'] = pd.to_datetime(df['Date'])

# Create output folder
os.makedirs('visualizations', exist_ok=True)
print("📁 Output folder created: /visualizations")
print()

# ============================================================
# CHART 1: BAR CHART — Revenue by Product
# ============================================================
print("-" * 60)
print("📊 CHART 1: Revenue by Product (Bar Chart)")
print("-" * 60)

revenue_by_product = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
colors = [SPOTLIGHT if i == 0 else MUTED for i in range(len(revenue_by_product))]
bars = ax.bar(revenue_by_product.index, revenue_by_product.values, color=colors, width=0.6)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2000,
            f'${height:,.0f}', ha='center', va='bottom',
            fontsize=9, fontweight='bold', color=DARK_TEXT)

ax.set_title(f'"{revenue_by_product.index[0]}" leads revenue at ${revenue_by_product.values[0]:,.0f} —\n'
             f'{((revenue_by_product.values[0]/revenue_by_product.sum())*100):.1f}% of total sales',
             fontsize=13, fontweight='bold', color=DARK_TEXT, pad=20)

ax.set_ylabel('Total Revenue ($)', fontsize=10, color=DARK_TEXT)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'${x:,.0f}'))
ax.grid(axis='y', alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/chart1_revenue_by_product.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart1_revenue_by_product.png")
print(f"   💡 Insight: {revenue_by_product.index[0]} = ${revenue_by_product.values[0]:,.0f} (Top Revenue)")
print()

# ============================================================
# CHART 2: LINE CHART — Monthly Revenue Trend
# ============================================================
print("-" * 60)
print("📈 CHART 2: Monthly Revenue Trend (Line Chart)")
print("-" * 60)

df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('YearMonth')['TotalPrice'].sum()
monthly_revenue.index = monthly_revenue.index.astype(str)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(range(len(monthly_revenue)), monthly_revenue.values,
        color=SPOTLIGHT, linewidth=2.5, marker='o', markersize=4)

peak_idx = monthly_revenue.values.argmax()
peak_value = monthly_revenue.values[peak_idx]
peak_month = monthly_revenue.index[peak_idx]

low_idx = monthly_revenue.values.argmin()
low_value = monthly_revenue.values[low_idx]
low_month = monthly_revenue.index[low_idx]

ax.scatter(peak_idx, peak_value, color=ACCENT_GREEN, s=150, zorder=5)
ax.annotate(f'PEAK: ${peak_value:,.0f}\n({peak_month})',
            xy=(peak_idx, peak_value), xytext=(peak_idx+1, peak_value+3000),
            fontsize=9, fontweight='bold', color=ACCENT_GREEN,
            arrowprops=dict(arrowstyle='->', color=ACCENT_GREEN))

ax.scatter(low_idx, low_value, color=ACCENT_RED, s=150, zorder=5)
ax.annotate(f'LOW: ${low_value:,.0f}\n({low_month})',
            xy=(low_idx, low_value), xytext=(low_idx+1, low_value-6000),
            fontsize=9, fontweight='bold', color=ACCENT_RED,
            arrowprops=dict(arrowstyle='->', color=ACCENT_RED))

ax.set_title(f'Revenue peaked at ${peak_value:,.0f} in {peak_month} —\noverall trend shows fluctuating monthly performance',
             fontsize=13, fontweight='bold', color=DARK_TEXT, pad=20)

ax.set_ylabel('Revenue ($)', fontsize=10, color=DARK_TEXT)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'${x:,.0f}'))
tick_positions = list(range(0, len(monthly_revenue), 3))
ax.set_xticks(tick_positions)
ax.set_xticklabels([monthly_revenue.index[i] for i in tick_positions], rotation=45, ha='right')
ax.grid(axis='y', alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/chart2_monthly_revenue_trend.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart2_monthly_revenue_trend.png")
print(f"   💡 Insight: Peak = {peak_month} (${peak_value:,.0f}) | Low = {low_month} (${low_value:,.0f})")
print()

# ============================================================
# CHART 3: HORIZONTAL BAR — Order Status Distribution
# ============================================================
print("-" * 60)
print("📊 CHART 3: Order Status Breakdown (Horizontal Bar)")
print("-" * 60)

status_counts = df['OrderStatus'].value_counts()
total_orders = len(df)

fig, ax = plt.subplots(figsize=(10, 5))
status_colors = []
for status in status_counts.index:
    if status in ['Cancelled', 'Returned']:
        status_colors.append(ACCENT_RED)
    elif status == 'Delivered':
        status_colors.append(ACCENT_GREEN)
    else:
        status_colors.append(MUTED)

ax.barh(status_counts.index, status_counts.values, color=status_colors, height=0.6)

for i, (val, idx) in enumerate(zip(status_counts.values, status_counts.index)):
    pct = (val / total_orders) * 100
    ax.text(val + 3, i, f'{val} ({pct:.1f}%)', va='center',
            fontsize=10, fontweight='bold', color=DARK_TEXT)

cancelled = status_counts.get('Cancelled', 0)
returned = status_counts.get('Returned', 0)
risk_pct = ((cancelled + returned) / total_orders) * 100

ax.set_title(f'⚠️ {risk_pct:.1f}% of orders are Cancelled or Returned —\na critical business risk requiring immediate action',
             fontsize=13, fontweight='bold', color=DARK_TEXT, pad=20)

ax.set_xlabel('Number of Orders', fontsize=10, color=DARK_TEXT)
ax.grid(axis='x', alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/chart3_order_status.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart3_order_status.png")
print(f"   💡 Insight: {risk_pct:.1f}% orders are Cancelled/Returned (Business Risk!)")
print()

# ============================================================
# CHART 4: STACKED BAR — Payment Method vs Order Status
# ============================================================
print("-" * 60)
print("📊 CHART 4: Payment Method vs Order Status (Stacked Bar)")
print("-" * 60)

payment_status = pd.crosstab(df['PaymentMethod'], df['OrderStatus'])

fig, ax = plt.subplots(figsize=(10, 6))
stack_colors = {'Delivered': ACCENT_GREEN, 'Cancelled': ACCENT_RED,
                'Returned': '#F59E0B', 'Pending': MUTED, 'Shipped': SPOTLIGHT}

bottom = None
for col in payment_status.columns:
    color = stack_colors.get(col, MUTED)
    vals = payment_status[col].values
    ax.bar(payment_status.index, vals,
           bottom=bottom if bottom is not None else 0,
           label=col, color=color, width=0.5)
    bottom = vals if bottom is None else bottom + vals

cancel_rate = {}
for method in payment_status.index:
    total = payment_status.loc[method].sum()
    c = payment_status.loc[method].get('Cancelled', 0)
    cancel_rate[method] = (c / total) * 100

worst_method = max(cancel_rate, key=cancel_rate.get)

ax.set_title(f'"{worst_method}" has the highest cancellation rate at {cancel_rate[worst_method]:.1f}% —\n'
             f'consider investigating payment friction for this method',
             fontsize=12, fontweight='bold', color=DARK_TEXT, pad=20)

ax.set_xlabel('Payment Method', fontsize=10, color=DARK_TEXT)
ax.set_ylabel('Number of Orders', fontsize=10, color=DARK_TEXT)
ax.legend(loc='upper right', frameon=False, fontsize=9)
ax.grid(axis='y', alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/chart4_payment_status.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart4_payment_status.png")
print(f"   💡 Insight: {worst_method} has highest cancellation rate ({cancel_rate[worst_method]:.1f}%)")
print()

# ============================================================
# CHART 5: SCATTER PLOT — Quantity vs Total Price
# ============================================================
print("-" * 60)
print("🔵 CHART 5: Quantity vs Total Price (Scatter Plot)")
print("-" * 60)

fig, ax = plt.subplots(figsize=(10, 6))

delivered = df[df['OrderStatus'] == 'Delivered']
cancelled_df = df[df['OrderStatus'] == 'Cancelled']
others = df[~df['OrderStatus'].isin(['Delivered', 'Cancelled'])]

ax.scatter(others['Quantity'], others['TotalPrice'], color=MUTED, alpha=0.4, s=30, label='Other')
ax.scatter(delivered['Quantity'], delivered['TotalPrice'], color=SPOTLIGHT, alpha=0.5, s=30, label='Delivered')
ax.scatter(cancelled_df['Quantity'], cancelled_df['TotalPrice'], color=ACCENT_RED, alpha=0.5, s=30, label='Cancelled')

correlation = df['Quantity'].corr(df['TotalPrice'])

ax.set_title(f'Correlation (r = {correlation:.2f}) between Quantity and Revenue —\nhigher quantities directly drive higher order values',
             fontsize=12, fontweight='bold', color=DARK_TEXT, pad=20)

ax.set_xlabel('Quantity Ordered', fontsize=10, color=DARK_TEXT)
ax.set_ylabel('Total Price ($)', fontsize=10, color=DARK_TEXT)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'${x:,.0f}'))
ax.legend(loc='upper left', frameon=False, fontsize=9)
ax.grid(alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/chart5_quantity_vs_price.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart5_quantity_vs_price.png")
print(f"   💡 Insight: Correlation = {correlation:.2f}")
print()

# ============================================================
# CHART 6: DONUT — Coupon Code Usage
# ============================================================
print("-" * 60)
print("🍩 CHART 6: Coupon Usage (Donut Chart)")
print("-" * 60)

coupon_filled = df['CouponCode'].notna().sum()
coupon_empty = df['CouponCode'].isna().sum()
coupon_data = pd.Series({'Coupon Used': coupon_filled, 'No Coupon': coupon_empty})

fig, ax = plt.subplots(figsize=(8, 8))
colors_pie = [SPOTLIGHT, MUTED]
wedges, texts, autotexts = ax.pie(
    coupon_data.values, labels=coupon_data.index,
    autopct='%1.1f%%', colors=colors_pie,
    explode=[0.05, 0], startangle=90,
    textprops={'fontsize': 12, 'fontweight': 'bold'},
    pctdistance=0.8
)

centre_circle = plt.Circle((0, 0), 0.55, fc=LIGHT_BG)
ax.add_artist(centre_circle)
ax.text(0, 0, f'{len(df)}\nOrders', ha='center', va='center',
        fontsize=14, fontweight='bold', color=DARK_TEXT)

coupon_pct = (coupon_filled / len(df)) * 100
ax.set_title(f'{coupon_pct:.1f}% of orders used coupons —\nhigh discount dependency may impact profit margins',
             fontsize=12, fontweight='bold', color=DARK_TEXT, pad=20)

plt.tight_layout()
plt.savefig('visualizations/chart6_coupon_usage.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart6_coupon_usage.png")
print(f"   💡 Insight: {coupon_pct:.1f}% orders used coupons")
print()

# ============================================================
# CHART 7: EXECUTIVE SUMMARY DASHBOARD
# ============================================================
print("-" * 60)
print("📋 CHART 7: Executive Summary Dashboard")
print("-" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('DecodeLabs E-Commerce — Executive Dashboard\nKey Metrics & Insights at a Glance',
             fontsize=15, fontweight='bold', color=DARK_TEXT, y=0.98)

# KPI 1: Total Revenue
ax1 = axes[0, 0]
total_rev = df['TotalPrice'].sum()
avg_order = df['TotalPrice'].mean()
ax1.text(0.5, 0.65, f'${total_rev:,.0f}', ha='center', va='center',
         fontsize=26, fontweight='bold', color=SPOTLIGHT, transform=ax1.transAxes)
ax1.text(0.5, 0.40, 'Total Revenue', ha='center', va='center',
         fontsize=12, color=DARK_TEXT, transform=ax1.transAxes)
ax1.text(0.5, 0.20, f'Avg Order: ${avg_order:,.2f}', ha='center', va='center',
         fontsize=10, color=MUTED, transform=ax1.transAxes)
ax1.axis('off')

# KPI 2: Order Status mini bar
ax2 = axes[0, 1]
top3_status = status_counts.head(3)
colors_mini = [ACCENT_GREEN if s == 'Delivered' else ACCENT_RED if s == 'Cancelled' else MUTED
               for s in top3_status.index]
ax2.barh(top3_status.index, top3_status.values, color=colors_mini, height=0.5)
for i, val in enumerate(top3_status.values):
    ax2.text(val + 3, i, f'{val}', va='center', fontsize=10, fontweight='bold')
ax2.set_title('Order Status (Top 3)', fontsize=11, fontweight='bold', color=DARK_TEXT)
ax2.grid(axis='x', alpha=0.2, linestyle='--')

# KPI 3: Top 3 Products
ax3 = axes[1, 0]
top3_products = revenue_by_product.head(3)
colors_prod = [SPOTLIGHT] + [MUTED] * 2
ax3.bar(top3_products.index, top3_products.values, color=colors_prod, width=0.5)
for bar in ax3.patches:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 500,
             f'${height:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax3.set_title('Top 3 Products by Revenue', fontsize=11, fontweight='bold', color=DARK_TEXT)
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'${x:,.0f}'))
ax3.grid(axis='y', alpha=0.2, linestyle='--')

# KPI 4: Key Metrics
ax4 = axes[1, 1]
unique_customers = df['CustomerID'].nunique()
metrics_text = (
    f"📦  Total Orders:        {total_orders:,}\n\n"
    f"👥  Unique Customers:    {unique_customers:,}\n\n"
    f"💰  Avg Order Value:     ${avg_order:,.2f}\n\n"
    f"⚠️  Risk Rate:           {risk_pct:.1f}%\n\n"
    f"🎟️  Coupon Usage:        {coupon_pct:.1f}%"
)
ax4.text(0.05, 0.5, metrics_text, ha='left', va='center',
         fontsize=11, color=DARK_TEXT, transform=ax4.transAxes, linespacing=1.8,
         fontfamily='monospace')
ax4.set_title('Key Business Metrics', fontsize=11, fontweight='bold', color=DARK_TEXT)
ax4.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('visualizations/chart7_executive_dashboard.png', bbox_inches='tight', facecolor=LIGHT_BG)
plt.close()
print(f"   ✅ Saved: chart7_executive_dashboard.png")
print()

# ============================================================
# FINAL SUMMARY
# ============================================================
print("=" * 60)
print("  🎉 PROJECT 4: DATA VISUALIZATION — COMPLETE!")
print("=" * 60)
print()
print("  📁 Charts saved in: /visualizations/")
print()
print("  ✅ Chart 1: Revenue by Product       (Bar Chart)")
print("  ✅ Chart 2: Monthly Revenue Trend    (Line Chart)")
print("  ✅ Chart 3: Order Status Breakdown   (Horizontal Bar)")
print("  ✅ Chart 4: Payment vs Status        (Stacked Bar)")
print("  ✅ Chart 5: Quantity vs Price        (Scatter Plot)")
print("  ✅ Chart 6: Coupon Usage             (Donut Chart)")
print("  ✅ Chart 7: Executive Dashboard      (Summary)")
print()
print("  🏆 ALL 4 PROJECTS COMPLETE!")
print("  🎓 DecodeLabs Data Analytics Internship — DONE!")
print("=" * 60)