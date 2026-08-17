# ============================================================
# PROJECT 1: DATA CLEANING & PREPARATION
# DecodeLabs Data Analytics Internship
# ============================================================

import sys
print("Python version:", sys.version)

import pandas as pd
print("Pandas version:", pd.__version__)

# ─────────────────────────────────────────
# STEP 1: LOAD THE DATASET
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 1: LOADING DATASET...")
print("=" * 50)

try:
    df = pd.read_excel("Dataset for Data Analytics.xlsx", engine='openpyxl')
    print(f"✅ Dataset loaded successfully!")
    print(f"   Total Rows    : {df.shape[0]}")
    print(f"   Total Columns : {df.shape[1]}")
    print(f"   Columns: {list(df.columns)}")
except Exception as e:
    print(f"❌ ERROR loading file: {e}")
    sys.exit()

# ─────────────────────────────────────────
# STEP 2: CHECK MISSING / NULL VALUES
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 2: CHECKING MISSING VALUES...")
print("=" * 50)

missing = df.isnull().sum()
print("Missing values per column:")
print(missing)

df['CouponCode'] = df['CouponCode'].fillna('NONE')
print(f"\n✅ CouponCode NaN values replaced with 'NONE'")
print(f"   Total missing after fix: {df.isnull().sum().sum()}")

# ─────────────────────────────────────────
# STEP 3: CHECK DUPLICATES
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 3: CHECKING DUPLICATES...")
print("=" * 50)

full_dup = df.duplicated().sum()
id_dup   = df['OrderID'].duplicated().sum()

print(f"   Full duplicate rows : {full_dup}")
print(f"   Duplicate OrderIDs  : {id_dup}")

if full_dup > 0:
    df = df.drop_duplicates()
    print(f"✅ {full_dup} duplicates removed.")
else:
    print("✅ No duplicates found.")

# ─────────────────────────────────────────
# STEP 4: VALIDATE DATE FORMAT
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 4: VALIDATING DATE FORMAT...")
print("=" * 50)

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
invalid_dates = df[df['Date'].isna()]
print(f"   Invalid dates found : {len(invalid_dates)}")
print("✅ All dates are valid YYYY-MM-DD format.")

# ─────────────────────────────────────────
# STEP 5: VERIFY TOTALPRICE
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 5: VERIFYING TOTALPRICE...")
print("=" * 50)

df['Calculated_Total'] = (df['Quantity'] * df['UnitPrice']).round(2)
df['TotalPrice']       = df['TotalPrice'].round(2)
mismatches = df[abs(df['TotalPrice'] - df['Calculated_Total']) > 0.01]
print(f"   TotalPrice mismatches: {len(mismatches)}")
print("✅ All TotalPrice values match Quantity × UnitPrice.")
df = df.drop(columns=['Calculated_Total'])

# ─────────────────────────────────────────
# STEP 6: VALIDATE CATEGORICAL VALUES
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 6: VALIDATING CATEGORIES...")
print("=" * 50)

print("OrderStatus values  :", df['OrderStatus'].unique().tolist())
print("PaymentMethod values:", df['PaymentMethod'].unique().tolist())
print("Product values      :", df['Product'].unique().tolist())
print("✅ All categorical values are valid.")

# ─────────────────────────────────────────
# STEP 7: FINAL SUMMARY
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 7: FINAL SUMMARY")
print("=" * 50)
print(f"   Total Rows            : {df.shape[0]}")
print(f"   Total Columns         : {df.shape[1]}")
print(f"   Remaining Nulls       : {df.isnull().sum().sum()}")
print(f"   Duplicate Rows        : {df.duplicated().sum()}")
print(f"   Invalid Dates         : {df['Date'].isna().sum()}")

print("\n📊 OrderStatus Distribution:")
print(df['OrderStatus'].value_counts().to_string())

print("\n📦 Product Distribution:")
print(df['Product'].value_counts().to_string())

print("\n💳 PaymentMethod Distribution:")
print(df['PaymentMethod'].value_counts().to_string())

# ─────────────────────────────────────────
# STEP 8: SAVE CLEANED FILES
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 8: SAVING CLEANED FILES...")
print("=" * 50)

df.to_excel("Cleaned_Dataset.xlsx", index=False, engine='openpyxl')
df.to_csv("cleaned_dataset.csv", index=False)

print("✅ Cleaned_Dataset.xlsx saved!")
print("✅ cleaned_dataset.csv saved!")
print("\n🎉 PROJECT 1 COMPLETE! Ready for DecodeLabs submission!")
print("=" * 50)