# DataFrame 1: Student Grades
import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

print(df1)

# Exercise 2: Find the student with the highest average grade.
top_student = df1.loc[df1['Average'].idxmax()]

print(top_student)

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

print(df1)
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
subject_means = df1[['Math', 'English', 'Science']].mean()

# Bar chart
plt.figure(figsize=(6,4))
plt.bar(subject_means.index, subject_means.values)
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.title("Average Grades in Each Subject")
plt.tight_layout()
plt.show()

# DataFrame 2: Sales Data

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(total_sales)

# Exercise 2: Find the date with the highest total sales.
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax()]
print(highest_sales_date)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
pct_change_df = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print(pct_change_df)

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
plt.figure(figsize=(8,5))
plt.plot(df2['Date'], df2['Product_A'])
plt.plot(df2['Date'], df2['Product_B'])
plt.plot(df2['Date'], df2['Product_C'])

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trends for Each Product Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# DataFrame 3: Employee Information

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
print(df3.groupby('Department').agg(average_salary=('Salary','mean')))

# Exercise 2: Find the employee with the most experience.
print(df3.loc[df3['Experience (Years)'].idxmax()])

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print(df3)

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
dept_counts = df3['Department'].value_counts()

# Plot bar chart
plt.figure(figsize=(6,4))
plt.bar(dept_counts.index, dept_counts.values)
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Distribution by Department")
plt.tight_layout()
plt.show()

# DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
# Exercise 1: Calculate the total revenue from all orders.
total_revenue = df4['Total_Price'].sum()
print(total_revenue)

# Exercise 2: Find the most ordered product.
print(df4.loc[df4['Quantity'].idxmax()])

# Exercise 3: Calculate the average quantity of products ordered.
print(df4.groupby('Product').agg(avg_quantity=('Quantity', 'mean')))

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(6, 6))
plt.pie(sales_by_product,
        labels=sales_by_product.index,
        autopct='%1.1f%%')
plt.title("Sales Distribution Across Products")
plt.show()
