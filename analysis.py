#----->> EDA OF ALL DATA<<-----#

import pandas as pd 

# load cleaned dataset
df = pd.read_csv("data\Cleaned_ecommerce_data.csv")

# convert order data to datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    format="mixed"
)

print("Dateset loaded successfully!")

print("\nShape:")
print(df.shape)

print("\nFiest 5 rows:")
print(df.head())

# Total Amount 

total_sales = df["Amount"].sum()

print("\nTotal Sales:")
print(total_sales)

# Total Profit

total_profit = df["Profit"].sum()

print("\nTotal Profit:")
print(total_profit)

# Total Orders 

total_orders = df["Order ID"].nunique()

print("\nTotal Orders:")
print(total_orders)

# Total Quantity

total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)

# profit margin 

profit_margin = (total_profit / total_sales) * 100

print("\nProfit Margin:")
print(round(profit_margin, 2), "%")

# Category columns list 
'''
print(df['Category'].unique())
print(df['Category'].value_counts()) '''

# Category analysis 

category_sales = df.groupby("Category")["Amount"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

category_profit = df.groupby("Category")["Profit"].sum()

print("\nCategory-wise Profit:")
print(category_profit)

# State Analysis 

state_sales  = df.groupby("State")["Amount"].sum()

print("\nState-wise Sales:")
print(state_sales)

state_profit = df.groupby("State")["Profit"].sum()

print("\nState-wise Profit:")
print(state_profit) 

# monthly Sales & profit analysis

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Amount"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

monthly_profit = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Profit"].sum()

print("\nMonthly Profit:")
print(monthly_profit)

# Top 10 Customers Analysis

Top_customers = (
    df.groupby("CustomerName")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers:")
print(Top_customers)

# sub-category analysis

subcategory_sales = (
     df.groupby("Sub-Category")["Amount"]
     .sum()
     .sort_values(ascending=False)
)

print("\nSubCategory-wise sales:")
print(subcategory_sales)

subcategory_profit = (
     df.groupby("Sub-Category")["Profit"]
     .sum()
     .sort_values(ascending=False)
)

print("\nSubCategory-wise profit:")
print(subcategory_profit)

# payment mode analysis

payment_sales = (
    df.groupby("PaymentMode")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPayment Mode-wise sales:")
print(payment_sales)


# Business Insights

print("\n================ BUSINESS INSIGHTS ================")

# highest sales category
best_category = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .index[0]   
)

print("\nHighest Sales Category:", best_category)

# highest profit category

best_profit_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .index[0]   
)       

print("\nHighest Profit Category:", best_profit_category)

# highest sales state
best_state = (
    df.groupby("State")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .index[0]   
)
print("\nHighest Sales State:", best_state) 

# highest profit state
best_profit_state = ( 
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .index[0]   
)       

print("\nHighest Profit State:", best_profit_state)

# Top Customers 

best_customer = (
    df.groupby("CustomerName")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .index[0]   
)

print("\nTop Customer:", best_customer)

# best sub-category by sales

best_subcategory = (
    df.groupby("Sub-Category")["Amount"]  
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

print("\nBest Sub-Category by Sales:", best_subcategory)

# most used payment mode

most_used_payment_mode = (
    df.groupby("PaymentMode")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)   

print("\nMost Used Payment Mode:", most_used_payment_mode)


#----->> Business Insights <<-----# 

# 1 — Best Performing Category

category_sales = df.groupby("Category")["Amount"].sum()

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\nBest performing Category:")
print("Cateogry:", best_category)
print("Sales:", best_category_sales)

# 2 — Best Performing State

state_sales = df.groupby("State")["Amount"].sum()

best_state = state_sales.idxmax()
best_state_sales = state_sales.max()

print("\nBest Performing state:")
print("States:",best_state)
print("Sales:", best_category_sales)

# 3 — Top Customer

customer_sales = df.groupby("CustomerName")["Amount"].sum()

top_customer = customer_sales.idxmax()
top_customer_sales = customer_sales.max()

print("\nTOp Customer:")
print("Customer:", top_customer)
print("Sales:",top_customer_sales)

# 4 — Most Profitable Sub-Category

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()

most_profitable_subcategory = subcategory_profit.idxmax()
most_profitable_subcategory_sales = subcategory_profit.max()

print("\nMost Profitable Category:")
print("Sub-Category:", most_profitable_subcategory)
print("Profit:", most_profitable_subcategory_sales)

# 5 — Most Used Payment Mode

payment_mode_orders = df.groupby("PaymentMode")["Order ID"].nunique()

most_used_payment_mode = payment_mode_orders.idxmax()
most_used_orders = payment_mode_orders.max()

print("\nMost Used Payment Mode:")
print("Payment Mode:", most_used_payment_mode)
print("Orders:", most_used_orders)

# 6 — Best Sales Month

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Amount"].sum()

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("\nBest Sales Month:")
print("Month:",best_month)
print("Sales:", best_month_sales)

# 7 — Loss-Making Area
#kaunsi Sub-Category me overall loss ho raha hai

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()

loss_making = subcategory_profit[subcategory_profit < 0]

print("\nLoss-Making Sub-Category:")
print(loss_making)
