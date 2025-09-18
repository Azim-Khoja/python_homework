# 1. Age Calculator.
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
year = 2025
birth = int(input("Yoshingizni kiriting: "))
my_birth_year = year - birth
print(my_birth_year)
# ========================================================================================================

# 2. Extract Car Names.
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])


# 3. Extract Car Names.
# Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::-2])
print(txt[::2])
# ========================================================================================================

# 4. Extract Residence Area
# Extract the residence area from the following text:
txt = "I'm John. I am from London"
txt = txt.split(' ')
txt = txt[2:]
print(' '.join(txt))
# ========================================================================================================

# 5. Reverse String.
# Write a Python program that takes a user input string and prints it in reverse order.
txt = input("Matn kiriting: ")
rev_txt = txt[::-1]
print(rev_txt)
# ========================================================================================================

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

txt = input('Matn kiriting: ')
vowels = "AaOoUuEeIi"
count = 0
for i in txt:
    if i in vowels:
        count += 1
print("Matnda {}ta unli harf bor".format(count))












