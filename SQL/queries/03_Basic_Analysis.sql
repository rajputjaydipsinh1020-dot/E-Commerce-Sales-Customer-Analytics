USE ecommerce_Project;

-- 1. Categories
select distinct Category 
from ecommerce;

-- 2. Payment Modes
select distinct PaymentMode
from ecommerce;

-- 3. States
select distinct State
from ecommerce;

-- 4. Category-wise Records
select
	Category,
    count(*) AS total_records
from ecommerce
group by Category;

-- 5. Sub-Categories
select distinct `Sub-Category`
from ecommerce;

-- 6. Customers
select distinct CustomerName
from ecommerce;