USE ecommerce_Project;

-- 1. Loss-Making-Categories 

SELECT 
	Category,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by Category
having sum(Profit) < 0
order by total_profit asc;

-- 2: High Sales but Low Profit Categories
SELECT 
	Category,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by Category
having sum(Amount) > 50000
	AND sum(Profit) < 11000
order by total_sales desc;

-- 3 — Top 10 Most Profitable Sub-Categories
SELECT 
	`Sub-Category`,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by `Sub-Category`
order by total_profit DESC
LIMIT 10;

-- 4 — Profit Margin by Category

SELECT 
	Category,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit,
    (sum(Profit) / sum(Amount)) * 100 AS total_margin
from ecommerce
group by Category
order by total_margin DESC;

-- 5 — High-Value Orders with Profit 
SELECT 
	`Order ID`,
    CustomerName,
    sum(Amount) AS total_value,
	sum(Profit) AS total_profit
from ecommerce
group by `Order ID` ,CustomerName
having sum(Amount) > 5000
order by total_value desc;

-- 6 Top Customer using Subquery
SELECT
    CustomerName,
    SUM(Amount) AS total_sales
FROM ecommerce
GROUP BY CustomerName
HAVING SUM(Amount) > (
    SELECT AVG(customer_sales)
    FROM (
        SELECT
            CustomerName,
            SUM(Amount) AS customer_sales
        FROM ecommerce
        GROUP BY CustomerName
    ) AS customer_summary
)
ORDER BY total_sales DESC;

-- 7 — Customer Ranking using RANK()
SELECT 
	CustomerName,
    Sum(Amount) AS total_sales,
    rank() over(
		order by sum(Amount) desc
	) AS customer_rank
from ecommerce
group by CustomerName
order by customer_rank;

-- 8 Monthly Sales Analysis
USE ecommerce_Project;
SELECT
    DATE_FORMAT(`Order Date`, '%y-%m')
    AS order_month,
    SUM(Amount) AS total_sale
FROM ecommerce
GROUP BY order_month
ORDER BY order_month;

-- 9 — Monthly Profit Analysis
USE ecommerce_Project;

SELECT
    DATE_FORMAT(`Order Date`, '%y-%m')
    AS order_month,
    SUM(Profit) AS total_profit
FROM ecommerce
GROUP BY order_month
ORDER BY order_month;

-- 10 — Sales Growth / Business Performance Analysis

WITH monthly_sales AS (
	SELECT 
		date_format(`Order Date`, '%y-%m')
        AS order_month,
        sum(Amount) AS total_sales
	from ecommerce
    group by order_month
)

SELECT 
	order_month,
    total_sales,
    lag(total_sales) over(
		order by order_month
	) AS previous_month_sales,
    total_sales - lag(total_sales) over(
		order by order_month
    ) AS sales_change
from monthly_sales
order by order_month;