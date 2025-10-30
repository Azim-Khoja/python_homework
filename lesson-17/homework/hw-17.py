import pandas as pd
import numpy as np

# Homework 1:
# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Fransisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.rename(columns={'First Name': 'first_name', 'Age': 'age', 'City': 'city'}, inplace=True)


def rename_columns(df, old_names, new_names):
    mapping = dict(zip(old_names, new_names))
    df.rename(columns=mapping, inplace=True)


rename_columns(df, ('First Name', 'Age'), ('first_name', 'age'))

# 2. Print the first 3 rows of the DataFrame

print(df.head(3))

# 3. Find the mean age of the individuals

print(df['age'].mean())

# 4. Select and print only the 'Name' and 'City' columns

print(df[['first_name', 'age']])

# 5. Add a new column 'Salary' with random salary values

df['Salary'] = np.random.randint(600, 1000, 4)

# 6. Display summary statistics of the DataFrame

print(df.describe())

#

# Homework 2:
# 1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses',
# representing monthly sales and expenses data. Use below table.
"""
Month	Sales	Expenses
Jan	5000	3000
Feb	6000	3500
Mar	7500	4000
Apr	8000	4500
"""

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

df = pd.DataFrame(data)

# 2. Calculate and display the maximum sales and expenses.

print(df[['Sales', 'Expenses']].max())

# 3. Calculate and display the minimum sales and expenses.

print(df[['Sales', 'Expenses']].min())

# 4. Calculate and display the average sales and expenses.

averages_sales_expenses = df[['Sales', 'Expenses']].mean()
print(averages_sales_expenses)

#

# Homework 3:
# 1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March',
# and 'April', representing monthly expenses for different categories. Use below table.

data = {
    'Category': ['Rent', 'Utilites', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df = pd.DataFrame(data)

# 2. Calculate and display the maximum expense for each category.

max_expense = df.set_index('Category').max(axis=1)
# max_expense = df.groupby('Category')[['January', 'February', 'March', 'April']].max()
print(max_expense)

# 3. Calculate and display the minimum expense for each category.

min_expense = df.set_index('Category').min(axis=1)
print(min_expense)

# 4. Calculate and display the average expense for each category.

avg_expense = df.set_index('Category').mean(axis=1)
print(avg_expense)
