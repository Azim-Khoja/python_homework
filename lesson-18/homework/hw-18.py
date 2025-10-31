import pandas as pd
import numpy as np

df = pd.read_csv('tackoverflow_qa.csv')

# Homework 2:
# 1. Find all questions that were created before 2014

filtered1 = df[df['creationdate'] <= '2014-01-01']  # case1
filtered2 = df.query('creationdate <= "2014-01-01"')

# 2. Find all questions with a score more than 50

score_over_50 = df.query('score > 50')  # filter over 50
np.min(score_over_50['score'])  # check the column for a score up to 50

# 3. Find all questions with a score between 50 and 100

filtered3 = df.query('(score > 50) & (score < 100)')

np.min(filtered3['score'])
np.max(filtered3['score'])

# 4. Find all questions answered by Scott Boston

filtered4 = df[df['ans_name'] == 'Scott Boston']  # case1
filtered4 = df.query('ans_name == "Scott Boston"')  # case2

# 5. Find all questions answered by the following 5 users:
# ["Jeff Hammerbacher", "Wes McKinney", "Josh Hemann", "Ted Petrou", "Tal Yarkoni"]

users = ["Jeff Hammerbacher", "Wes McKinney", "Josh Hemann", "Ted Petrou", "Tal Yarkoni"]
filtered5 = df.query('ans_name in ["Jeff Hammerbacher", "Wes McKinney", "Josh Hemann", "Ted Petrou", "Tal Yarkoni"]')
filtered5 = df[df['ans_name'].isin(users)]

# 6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

filtered6 = df.query('"2014-03-01" <= creationdate <= "2014-10-31" and ans_name == "Unutbu" and score < 5')

# 7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

# case1
filtered7 = df[
    (df['score'] >= 5) &
    (df['score'] <= 10) |
    (df['viewcount'] > 10000)]
# case2
filtered7 = df.where(
    (df['score'] >= 5) &
    (df['score'] <= 10) |
    (df['viewcount'] > 10000))
filtered7.dropna()

# 8. Find all questions that are not answered by Scott Boston

filtered8 = df[df['ans_name'] != 'Scott Boston']  # case1
filtered8 = df.where(df['ans_name'] != 'Scott Boston')  # case2
filtered8 = df.query('ans_name != "Scott Boston"')  # case3

# Homework 3:
df = pd.read_csv('titanic.csv')
# 1. Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

filtered1 = df.query('(Sex == "female") and (20 <= Age <= 30) and (Pclass == 1)')

# 2. Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

filtered2 = df.query('Fare >= 100')

# 3. Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

filtered3 = df.where(
    (df['Survived'] == 1) &
    (df['SibSp'] == 0) &
    (df['Parch'] == 0)
).dropna()

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

filtered4 = df[(df['Embarked'] == 'C') & (df['Fare'] >= 50)]

# 5. Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard

filtered5 = df[(df['SibSp'] == 1) & (df['Parch'] == 1)]

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

filtered6 = df[(df['Age'] < 15) & (df['Survived'] != 1)]

# 7. Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200

filtered7 = df[(df['Cabin'].notna()) & (df['Fare'] > 200)]

# 8. Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

odd = (df['PassengerId'] % 2 != 0)
filtered8 = df[odd]

# 9. Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

filtered9 = df[~df['Ticket'].duplicated(keep=False)]

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

filtered10 = df[
    (df['Name'].str.contains('Miss', case=False, na=False)) &
    (df['Pclass'] == 1)
    ]
