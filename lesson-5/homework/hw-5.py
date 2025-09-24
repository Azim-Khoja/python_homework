# 1. Determines whether a given year is a leap year
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(1994))
print(is_leap(2000))
print(is_leap(2020))
print(is_leap(2023))


# 2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
def numChecker(n):
    """
    Kiritilgan son shartlarga mos ravishda 'Weird' yoki 'Not Weird' chiqaradi
    """
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


n = int(input("Son kiriting: "))
numChecker(n)


# 3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
def find_even_number(n1, n2):
    if n1 % 2 != 0:
        n1 += 1
    if n2 % 2 != 0:
        n2 += 1
    if n1 > n2:
        return []
    return list(range(n1, n2 + 1, 2))


print(find_even_number(0, 40))
