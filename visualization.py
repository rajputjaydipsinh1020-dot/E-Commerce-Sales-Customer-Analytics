#----->> CHARTS OF DATA <<-----#

import matplotlib.pyplot as plt 
import pandas as pd

# load data

df = pd.read_csv("data/cleaned_ecommerce_data.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    format="mixed"
)

print("Dataset loaded successfully!")
print(df.shape)
print(df.head())   

# Category-wise Sales

category_sales = df.groupby("Category")["Amount"].sum()

plt.figure(figsize=(8, 5))

plt.bar(category_sales.index, category_sales.values)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

plt.tight_layout()

plt.savefig("charts/category_sales.png")

plt.show()

# category-wise profit 

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))

plt.bar(category_profit.index, category_profit.values)

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("charts/category_profit.png")
plt.show()

# monthly_Sales trend 

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Amount"]
    .sum()
)

# convert month index  into string

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

#  MONTHLY PROFIT TREND

monthly_profit = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Profit"]
    .sum()
)

monthly_profit.index = monthly_profit.index.astype(str)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_profit.index,
    monthly_profit.values,
    marker='o'
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/monthly_profit_trend.png")
plt.show()

#  STATE-WISE SALES

state_sales = (
    df.groupby("State")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    state_sales.index,
    state_sales.values
)

plt.title("State-wise Sales")
plt.xlabel("State")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/state_sales.png")
plt.show()

# State-wise Profit 

state_profit = (
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    state_profit.index,
    state_profit.values
)

plt.title("State-wise Profit")
plt.xlabel("State")
plt.ylabel("Sales Profit")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/states_profit.png")
plt.show()

# PAYMENT MODE SALES

payment_Sales = (
    df.groupby("PaymentMode")["Amount"]
    .sum()
)

plt.figure(figsize=(8, 8))

plt.pie(
    payment_Sales.values,
    labels=payment_Sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Paymant Mode-wise Sales")

plt.tight_layout()
plt.savefig("charts/paymentmode_sales.png")
plt.show()

# TOP 10 CUSTOMERS BY SALES

top_customers = (
    df.groupby("CustomerName")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.bar(
    top_customers.index,
    top_customers.values
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/Top_10_Customer_Sales")
plt.show()


#SUB-CATEGORY SALES

subcategory_sales = (
    df.groupby("Sub-Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    subcategory_sales.index,
    subcategory_sales.values
)

plt.title("Sub-Category-wise Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/Sub_Category-wise_Sales")
plt.show()

# Sub-Category Profit 

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    subcategory_profit.index,
    subcategory_profit.values
)

plt.title("Sub-Category-wise Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/Sub_category-wise_Profit")

plt.show()

# Category-wise Quantity Sold

category_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    category_quantity.index,
    category_quantity.values
)

plt.title("Category-wise Quantity Sold")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")

plt.tight_layout()
plt.savefig("charts/Category-wise_Quantity_Sold")   

plt.show()
