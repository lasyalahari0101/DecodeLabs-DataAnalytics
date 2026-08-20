# 📊 DecodeLabs — Data Analytics Internship

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Completed%20✅-brightgreen)

> **End-to-end Data Analytics portfolio** — 4 projects covering Data Cleaning, EDA, SQL Analysis & Data Visualization on real-world e-commerce data (1,200 orders | $1.26M revenue).

---

## 🎯 About This Project

This repository contains my complete work from the **Data Analytics Internship at DecodeLabs** (Aug 2026). I analyzed a real-world e-commerce dataset with **1,200 orders across 7 product categories**, uncovering actionable business insights through the full analytics pipeline.

---

## 📁 Repository Structure

```
DecodeLabs-DataAnalytics/
│
├── 📄 data_cleaning.py              # Project 1: Data Cleaning & Preparation
├── 📄 eda_analysis.py               # Project 2: Exploratory Data Analysis
├── 📄 sql_analysis.py               # Project 3: SQL Data Analysis (30 queries)
├── 📄 data_visualization.py         # Project 4: Data Visualization & Storytelling
│
├── 📂 visualizations/               # All 7 charts (PNG)
│   ├── chart1_revenue_by_product.png
│   ├── chart2_monthly_revenue_trend.png
│   ├── chart3_order_status_distribution.png
│   ├── chart4_discount_vs_revenue.png
│   ├── chart5_quantity_revenue_scatter.png
│   ├── chart6_top_customers.png
│   └── chart7_executive_dashboard.png
│
├── 📊 Dataset for Data Analytics.xlsx   # Original dataset
├── 📊 cleaned_dataset.csv              # Cleaned output (Project 1)
├── 📊 Cleaned_Dataset.xlsx             # Cleaned output - Excel format
├── 📊 EDA_Report.xlsx                  # EDA findings report (Project 2)
├── 🗄️ decodelabs.db                    # SQLite database (Project 3)
└── 📄 README.md                        # You are here!
```

---

## 🚀 Projects Overview

### ✅ Project 1 — Data Cleaning & Preparation
| Aspect | Details |
|--------|---------|
| **Objective** | Clean and prepare raw e-commerce data for analysis |
| **Records** | 1,200 rows × multiple columns |
| **Tasks** | Handle missing values, remove duplicates, fix data types, validate entries |
| **Output** | `cleaned_dataset.csv`, `Cleaned_Dataset.xlsx` |

**Key Actions:**
- Handled null values using appropriate imputation strategies
- Removed duplicate records
- Standardized data types (dates, numerics, categories)
- Validated data integrity across all columns

---

### ✅ Project 2 — Exploratory Data Analysis (EDA)
| Aspect | Details |
|--------|---------|
| **Objective** | Uncover patterns, trends, and anomalies in the data |
| **Techniques** | Statistical analysis, correlation, distribution analysis, outlier detection |
| **Output** | `EDA_Report.xlsx` |

**Key Findings:**
- 💰 Total Revenue: **$1,264,762**
- 📦 Total Orders: **1,200** across 7 product categories
- 📈 Peak Revenue Month: **June 2024 ($68,069)**
- 🎟️ **74.2%** of orders used discount coupons
- 📉 **41.4%** Cancellation/Return rate identified

---

### ✅ Project 3 — SQL Data Analysis
| Aspect | Details |
|--------|---------|
| **Objective** | Query and analyze data using SQL |
| **Database** | SQLite (`decodelabs.db`) |
| **Queries** | 30 structured queries |
| **Concepts** | SELECT, WHERE, GROUP BY, HAVING, ORDER BY, Subqueries, Aggregations |

**Query Categories:**
- Basic retrieval & filtering (SELECT, WHERE)
- Aggregations (SUM, AVG, COUNT, MIN, MAX)
- Grouping & conditional filtering (GROUP BY, HAVING)
- Sorting & ranking (ORDER BY, LIMIT)
- Advanced subqueries & nested logic

---

### ✅ Project 4 — Data Visualization & Storytelling
| Aspect | Details |
|--------|---------|
| **Objective** | Create boardroom-ready visualizations for business stakeholders |
| **Library** | Matplotlib |
| **Charts** | 7 professional visualizations |
| **Output** | `visualizations/` folder |

**Charts Created:**
| # | Chart | Type | Insight |
|---|-------|------|---------|
| 1 | Revenue by Product | Bar | Chair & Printer lead at ~$195K each |
| 2 | Monthly Revenue Trend | Line | Peak in June 2024, seasonal patterns |
| 3 | Order Status Distribution | Donut | 41.4% orders cancelled/returned |
| 4 | Discount vs Revenue | Bar | Coupon users drive 74.2% of orders |
| 5 | Quantity vs Revenue | Scatter | Linear relationship confirmed |
| 6 | Top 10 Customers | Horizontal Bar | Top customer: $14K+ spend |
| 7 | Executive Dashboard | Multi-panel | Complete business overview |

---

## 📊 Executive Dashboard Preview

![Executive Dashboard](visualizations/chart7_executive_dashboard.png)

---

## 💡 Key Business Insights

| Insight | Impact |
|---------|--------|
| 📉 41.4% Cancellation/Return Rate | Critical risk — needs immediate intervention |
| 💰 Chair & Printer dominate revenue | Focus marketing on top performers |
| 📈 June 2024 peak ($68,069) | Seasonal opportunity for campaigns |
| 🎟️ 74.2% coupon usage | Discount dependency — evaluate profitability |
| 👤 Top 10 customers = disproportionate revenue | Implement loyalty/retention program |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation & analysis |
| **Matplotlib** | Data visualization |
| **SQLite** | Database & SQL queries |
| **Git & GitHub** | Version control & portfolio hosting |
| **Excel/CSV** | Data I/O formats |

---

## ⚡ How to Run

```bash
# Clone the repository
git clone https://github.com/lasyalahari0101/DecodeLabs-DataAnalytics.git
cd DecodeLabs-DataAnalytics

# Install dependencies
pip install pandas matplotlib openpyxl

# Run any project
python data_cleaning.py
python eda_analysis.py
python sql_analysis.py
python data_visualization.py
```

---

## 👩‍💻 Author

**Gosukonda Sai Lasya Lahari**

[![GitHub](https://img.shields.io/badge/GitHub-lasyalahari0101-181717?logo=github)](https://github.com/lasyalahari0101)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://www.linkedin.com/in/your-profile)

---

## 🙏 Acknowledgements

- **DecodeLabs** — For providing this hands-on internship opportunity
- Real-world e-commerce dataset for practical learning

---

## 📜 License

This project is for educational and portfolio purposes as part of the DecodeLabs Data Analytics Internship (August 2026).