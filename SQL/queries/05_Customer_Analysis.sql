-- Customer-wise Total Sales --

USE ecommerce_Project;

-- 1. Customer-wise Total Sales

SELECT 
	CustomerName,
    sum(Amount) AS total_sales
from ecommerce
group by CustomerName
order by total_sales desc;

-- 2. Top 10 Customers
SELECT 
	CustomerName,
    sum(Amount) AS total_sales
from ecommerce
group by CustomerName
order by total_sales desc
limit 10;

-- 3. Customer-wise Profit
SELECT 
	CustomerName,
    sum(Profit) AS total_profits
from ecommerce
group by CustomerName
order by total_profits desc;

-- 4. Top 10 Profitable Customers 
SELECT 
	CustomerName,
    sum(Profit) AS total_profit
from ecommerce
group by CustomerName
order by total_profit desc
limit 10;

-- 5. Customer ke Orders Count karna
SELECT 
	CustomerName,
    count(distinct `Order ID`) AS total_orders
from ecommerce
group by CustomerName
order by total_orders desc;

-- 6 Repeat Customers
SELECT 
	CustomerName,
    count(distinct `Order ID`) AS total_orders
from ecommerce
group by CustomerName
having count(distinct `Order ID`) > 1
order by total_orders desc;

-- 7 Average Order Value (AOV)
use ecommerce_Project;

SELECT 
	sum(Amount) / count(distinct `Order ID`) AS averange_order_value
from ecommerce;

-- 8 Customer-wise Sales + Orders + AOV

SELECT 
	CustomerName,
    count(distinct `Order ID`) AS total_orders,
    sum(Amount) AS total_sales,
    sum(Amount) / count(distinct `Order ID`) AS averange_order_value
from ecommerce
group by CustomerName
order by total_sales desc;

-- 9 High-Value Customers
SELECT 
	CustomerName,
    sum(Amount) AS total_sales
from ecommerce
group by CustomerName
having sum(Amount) > 6000
order by total_sales desc;

-- 10 Customer-wise Sales + Profit
SELECT 
	CustomerName,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by CustomerName
order by total_profit desc;

-- 11 — Top 10 Customers by Profit
SELECT 
	CustomerName,
    sum(Profit) AS total_profit
from ecommerce
group by CustomerName
order by total_profit desc
limit 10;

-- 12 — High-Value Orders
SELECT 
	`Order ID`,
    sum(Amount) AS order_value
from ecommerce
group by `Order ID`, CustomerName
having sum(Amount) > 5000
order by order_value desc;

-- 13 — Customer Sales + Profit + Orders
SELECT 
	CustomerName,
    count(distinct `Order ID`) AS total_orders,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by CustomerName
order by total_Sales desc;
    
-- 14 — Customer Profit Margin
SELECT 
	CustomerName, 
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit,
	(sum(Profit) / sum(Amount)) * 100 AS total_margin
from ecommerce
group by CustomerName
order by total_margin desc;

-- 15 — Repeat Customers ki Total Count
SELECT 
	count(*) AS repeat_customer_count
from(
	select
		CustomerName
	from ecommerce
    group by CustomerName
    having count(distinct `Order ID`) > 1
) AS repeat_customers;

-- 16 — Customers with high sales but low profit

SELECT 
	CustomerName,
    Sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by CustomerName
having sum(Amount) > 6000
	AND sum(Profit) < 1000
order by total_sales desc;

-- 17 Customer Ranking

SELECT
	CustomerName,
    Sum(Amount) AS total_sales,
    rank() over(
		order by sum(Amount) desc
	) AS customer_rank
from ecommerce
group by CustomerName
order by customer_rank;