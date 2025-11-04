import pandas as pd
import numpy as np

# Homework Assignment 1: Analyzing Sales Data
df = pd.read_csv('sales_data.csv')

# 1. Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction

# Total quantity sold.
total_sold = df.groupby("Category")['Quantity'].sum().reset_index()
print(total_sold)

# Average price per unit.
avg_price = df.groupby("Category")['Price'].mean().reset_index()
print(avg_price)

# Maximum quantity sold in a single transaction
max_quantity = df.groupby("Category")['Quantity'].max().reset_index()
print(max_quantity)

# 2. Identify the top-selling product in each category based on the total quantity sold.
total_qty = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
# total_qty
top_selling = total_qty.loc[total_qty.groupby("Category")["Quantity"].idxmax()].reset_index(drop=True)
print(top_selling)


# 3. Find the date on which the highest total sales (quantity * price) occurred.
df['Total_Sales'] = df['Quantity'] * df['Price']
daily_sales = df.groupby('Date')['Total_Sales'].sum().reset_index()
max_sales_date = daily_sales.loc[daily_sales['Total_Sales'].idxmax()]
print(max_sales_date)

# Homework Assignment 2: Examining Customer Orders
df = pd.read_csv('customer_orders.csv')

# 1. Group the data by CustomerID and filter out customers who have made less than 20 orders.
# 2. Identify customers who have ordered products with an average price per unit greater than $120.
# 3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

# 1. Group the data by CustomerID and filter out customers who have made less than 20 orders.
orders_count = df.groupby('CustomerID')['OrderID'].count()
eligible_customers = orders_count[orders_count >= 20].index
filtered_df = df[df["CustomerID"].isin(eligible_customers)]
print(filtered_df)

# 2. Identify customers who have ordered products with an average price per unit greater than $120.
avg_price_per_customer = df.groupby("CustomerID")["Price"].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer['Price'] > 120]
print(high_value_customers)


# 3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
product_summary = (
    df.groupby("Product")
    .agg(
        Total_Quantity=("Quantity", "sum"),
        Total_Price=("Price", lambda x: (df.loc[x.index, "Quantity"] * x).sum())
    )
    .reset_index()
)

filtered_products = product_summary[product_summary["Total_Quantity"] >= 5]

print(filtered_products)

# Homework Assignment 3: Population Salary Analysis
# a. "population.db" sqlite database has population table.
# b. "population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# 1. Percentage of population for each salary category;
# 2. Average salary in each salary category;
# 3. Median salary in each salary category;
# 4. Number of population in each salary category;
# c. Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.

import pandas as pd
import sqlite3
import re

# === 1. Fayl manzillarini belgilash ===
db_path = "population.db"
excel_path = "population_salary_analysis.xlsx"
output_path = "population_salary_result.xlsx"

# === 2. SQLite bazasiga ulanish va ma'lumotni olish ===
conn = sqlite3.connect(db_path)
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# === 3. Excel faylidan Salary Band ma'lumotlarini o'qish ===
salary_bands_df = pd.read_excel(excel_path)


# === 4. Bandlar oralig‘ini ajratish ===
def parse_salary_band(band):
    band = band.replace(",", "")
    if "till" in band:
        # Masalan: "till $200,000"
        max_salary = int(re.search(r"\$(\d+)", band).group(1))
        return (0, max_salary)
    elif "and over" in band:
        # Masalan: "$1,800,001 and over"
        min_salary = int(re.search(r"\$(\d+)", band).group(1))
        return (min_salary, float('inf'))
    else:
        # Masalan: "$200,001 - $400,000"
        match = re.findall(r"\$(\d+)", band)
        if len(match) == 2:
            return tuple(map(int, match))
    return (None, None)


salary_bands_df["Range"] = salary_bands_df["Salary Band"].apply(parse_salary_band)

# === 5. Har bir band uchun statistikalarni hisoblash ===
total_population = len(population_df)

percentages = []
avg_salaries = []
median_salaries = []
pop_counts = []

for _, row in salary_bands_df.iterrows():
    low, high = row["Range"]
    band_df = population_df[(population_df["salary"] >= low) & (population_df["salary"] <= high)]

    count = len(band_df)
    percentage = (count / total_population) * 100 if total_population > 0 else 0
    avg_salary = band_df["salary"].mean() if count > 0 else 0
    median_salary = band_df["salary"].median() if count > 0 else 0

    pop_counts.append(count)
    percentages.append(percentage)
    avg_salaries.append(avg_salary)
    median_salaries.append(median_salary)

# === 6. Natijalarni jadvalga qo‘shish ===
salary_bands_df["Number of population"] = pop_counts
salary_bands_df["Percentage"] = percentages
salary_bands_df["Average Salary"] = avg_salaries
salary_bands_df["Median Salary"] = median_salaries

# === 7. Yakuniy natijani yangi Excel faylga yozish ===
salary_bands_df.to_excel(output_path, index=False)

print("Natija faylda saqlandi:", output_path)

import pandas as pd
import sqlite3
import re

# === 1. Fayl manzillarini belgilash ===
db_path = "/mnt/data/population.db"
excel_path = "/mnt/data/population_salary_analysis.xlsx"
output_state_path = "/mnt/data/population_salary_by_state.xlsx"

# === 2. Ma'lumotlarni o‘qish ===
conn = sqlite3.connect(db_path)
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

salary_bands_df = pd.read_excel(excel_path)


# === 3. Daromad oraliqlarini aniqlash ===
def parse_salary_band(band):
    band = band.replace(",", "")
    if "till" in band:
        max_salary = int(re.search(r"\$(\d+)", band).group(1))
        return (0, max_salary)
    elif "and over" in band:
        min_salary = int(re.search(r"\$(\d+)", band).group(1))
        return (min_salary, float('inf'))
    else:
        match = re.findall(r"\$(\d+)", band)
        if len(match) == 2:
            return tuple(map(int, match))
    return (None, None)


salary_bands_df["Range"] = salary_bands_df["Salary Band"].apply(parse_salary_band)

# === 4. Har bir State va Salary Band uchun hisob-kitob ===
result_rows = []

for state, state_df in population_df.groupby("state"):
    total_population_state = len(state_df)
    for _, band in salary_bands_df.iterrows():
        low, high = band["Range"]
        band_df = state_df[(state_df["salary"] >= low) & (state_df["salary"] <= high)]

        count = len(band_df)
        percentage = (count / total_population_state) * 100 if total_population_state > 0 else 0
        avg_salary = band_df["salary"].mean() if count > 0 else 0
        median_salary = band_df["salary"].median() if count > 0 else 0

        result_rows.append({
            "State": state,
            "Salary Band": band["Salary Band"],
            "Number of population": count,
            "Percentage": percentage,
            "Average Salary": avg_salary,
            "Median Salary": median_salary
        })

# === 5. Yakuniy DataFrame yaratish ===
result_df = pd.DataFrame(result_rows)

# === 6. Natijani Excel faylga saqlash ===
result_df.to_excel(output_state_path, index=False)

print("Natija faylda saqlandi:", output_state_path)