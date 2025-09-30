# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

# Examples
# Input: hello Output: hel_lo

# Input: assalom Output: ass_alom

# Input: abcabcabcdeabcdefabcdefg Output: abc_abcab_cdeabcd_efabcdef_g

def modify_string(txt):
    vowels = "aeiouAEIOU"  # unlilar
    result = ""
    count = 0  # har uchinchi belgini sanash

    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1

        # Har uchinchi belgi bo'lsa va oxirida bo'lmasa
        if count == 3 and i != len(txt) - 1:
            # Agar belgi unli bo'lsa yoki keyin '_' bo'lsa → keyingi belgidan keyin qo'yamiz
            if txt[i] in vowels:
                result += txt[i + 1]  # keyingi belgini qo'shamiz
                result += "_"
                i += 1  # keyingi belgi ustidan sakraymiz
            else:
                result += "_"
            count = 0
        i += 1

    return result


# Testlar
print(modify_string("hello"))       # hel_lo
print(modify_string("assalom"))     # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))
# abc_abcab_cdeabcd_efabcdef_g


# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input("Son kiriting: "))
for i in range(n):
    print(i**2)

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop
n = 0
while n < 10:
    n += 1
    print(n, end=' ')

# Exercise 2: Print the following pattern
num = int(input("Enter a number: "))

for i in range(num):
    for n in range(1, i+1):
        print(n, end=' ')
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number
num = int(input("Enter number: "))
summ = 0
for i in range(1, num+1):
    summ += i
print("Sum of number:", summ)

# Exercise 4: Print multiplication table of a given number
n = int(input("Son kiriting:"))
empty = 0
while empty < n:
    empty += 2
    if empty % 2 == 0:
        print(empty)

# Exercise 5: Display numbers from a list using a loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:

# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if  (number > 50) and \
        (number <= 150) and \
        (number % 5 == 0):
            print(number)

# Exercise 6: Count the total number of digits in a number
number = input("Raqam kiriting:")
print(len(number))

# Exercise 7: Print reverse number pattern
num = int(input("Enter a number: "))

for i in range(num, 0, -1):
    for n in range(i, 0, -1):
        print(n, end=' ')
    print()

# Exercise 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected Output:

# 50
# 40
# 30
# 20
# 10

# case1
list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
    print(i)

# case2
list1 = [10, 20, 30, 40, 50]
for i in list1[::-1]:
    print(i)

# Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
n = 0
while n < 5:
    n += 1
    print(n)
print("Done!")

# Exercise 11: Print all prime numbers within a range
# Example:

# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47

for i in range(25, 50):
    if i > 1:
        tub = True
        for item in range(2, i):
            if i % item == 0:
                tub = False
                break
        if tub:
            print(i)

# Exercise 12: Display Fibonacci series up to 10 terms
# Example:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

n = 10
a, b = 0, 1

print("Fibonacci:", end=' ')
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120

number = int(input("Enter number: "))
factorial = 1
for i in range(1, number):
    factorial *= i
print(f"Factorial of {number}! is:", factorial)

list1 = [1, 1, 2]
list2 = [2, 3, 4]

def uncommon(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result

print(uncommon(list1, list2))