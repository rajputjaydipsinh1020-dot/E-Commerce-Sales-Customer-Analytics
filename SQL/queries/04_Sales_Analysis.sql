use ecommerce_Project;

-- 1. Total Sales
SELECT 
	sum(Amount) AS total_sales
from ecommerce;

-- 2. Total Profit
SELECT 
	sum(Profit) AS total_Profit
from ecommerce;

-- 3. total Quantity
SELECT 
	sum(Quantity) AS total_quantity
from ecommerce;

-- 4. total orders
SELECT 
	count(distinct`Order ID`) AS total_orders
from ecommerce;

-- 5. Category-wise Sales 
SELECT
	Category,
    sum(Amount) AS total_sales
from ecommerce
group by Category;

-- 6. Category-wise Profit
SELECT 
	Category,
    sum(Profit) AS total_profit
from ecommerce
group by Category;

-- 7. Category-wise sale and profit 
SELECT 
	Category,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profit
from ecommerce
group by Category;

-- 8. Highest Sales Category + Profit Category
SELECT 
	Category,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profits
from ecommerce
group by Category
order by total_sales desc;

-- 9. state-wise sales
SELECT 
	State,
	sum(Amount) AS total_sales
from ecommerce
group by State
order by total_sales desc;    

-- 10. State-wise profit
SELECT 
	State,
    sum(Profit) AS total_profits 
from ecommerce
group by State
order by total_profits desc;

-- 11. State-wise Sales + Profit 
SELECT 
	State,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profits
from ecommerce
group by State
order by total_sales desc;

-- 12. Top_10_States by Sales
SELECT 
	State,
    sum(Amount) AS total_sales
from ecommerce
group by State
order by total_sales desc
limit 10;
 
-- 13. Sub-Category-wisev Sales
SELECT 
	`Sub-Category`,
    sum(Amount) AS total_sales
From ecommerce
group by `Sub-Category`
order by total_sales DESC;

-- 14. Sub-Category-wisev Profits
SELECT 
	`Sub-Category`,
    sum(Profit) AS total_profits
From ecommerce
group by `Sub-Category`
order by total_profits DESC;

-- 15. Sub-Category-wisev Sales + Profits
SELECT 
	`Sub-Category`,
    sum(Amount) AS total_sales,
    sum(Profit) AS total_profits
From ecommerce
group by `Sub-Category`
order by total_sales DESC;

-- 16. PaymentMode-wise Sales
SELECT 
	PaymentMode,
    sum(Amount) AS total_sales
from ecommerce
group by PaymentMode
order by total_sales desc;

-- 17. PaymentMode-wise order
SELECT 
	PaymentMode,
    count(distinct `Order ID`) AS total_orders
from ecommerce
group by PaymentMode
order by total_orders desc;

-- 18. PaymentMode-wise Sales + orders
SELECT 
	PaymentMode,
    sum(Amount) AS total_sales,
    count(distinct `Order ID`) AS total_Orders
from ecommerce
group by PaymentMode
order by total_sales desc;

-- 19. Profit aur Loss Analysis
SELECT 
	CASE
		WHEN Profit > 0 THEN 'Profit'
        WHEN Profit < 0 THEN 'Loss'
        ELSE 'No Profit/Loss'
	END AS Profit_Status,
    count(*) AS total_records
from ecommerce
group by Profit_Status
order by total_records desc;

-- 20 . Loss-making Sub-Categories in Profits
SELECT 
	`Sub-Category`,
    sum(Profit) AS total_profits
from ecommerce
group by `Sub-Category`
having sum(Profit) < 0
order by total_profits desc;