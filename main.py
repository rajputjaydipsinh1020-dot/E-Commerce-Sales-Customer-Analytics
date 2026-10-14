# ----->> cleaning ALL DATA <<-----#

import pandas as pd 

# load both file

orders = pd.read_csv("data\Orders.csv")
details = pd.read_csv("data\Details.csv")

# check columns 

print("Orders columns:")
print(orders.columns)

print("\nDetails columns:")
print(details.columns)

# join both datasets using order ID 

df = pd.merge(
    orders,
    details,
    on="Order ID",
    how="inner"
)

# check result 

print("\nJoined Date:")
print(df.head())

print("\nDatasat Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# save merged dataset 

df.to_csv("data/merged_ecommerce_data.csv", index=False)
print("\nMerged file saved successfully!")

# Data Cleaning 

print("\n---Dataset Overview---")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Missing Values 

print("\n---Missing Values---")
print(df.isnull().sum())

# Duplicate Rows 

print("\n---Duplicate Rows---")
print("Number of duplicate rows:", df.duplicated().sum())

# Data Types

print("\n---Data Types---")
print(df.dtypes)

# DATE CONVERSION

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    format="mixed"
)

print("\n---After Data Conversion---")
print(df.dtypes)

# final Cleaning Check

print("\n---Final Cleaning Check---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDate Types:")
print(df.dtypes)

print("\nDataset Shapes:")
print(df.shape)

# Save Clean Data 

df.to_csv("data/Cleaned_ecommerce_data.csv",index=False)
print("\nCleaned dataset saved successfully!")