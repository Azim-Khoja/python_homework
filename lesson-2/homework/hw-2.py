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
# ========================================================================================================

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
sonlar = []
n = int(input("Nechta son kiritmoqchisiz?:"))
for i in range(n):
    son = int(input(f"{i + 1}-sonni kiriting:"))
    sonlar.append(son)
print(f"Siz kiritgan eng katta son: ", max(sonlar))
# ========================================================================================================

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
text = input("Matn kiriting:")
palindrome = text[::-1]
if text == palindrome:
    print("Siz kiritgan matn Palindrom")
else:
    print("Siz kiritgan matn Palindrom emas")
# ========================================================================================================

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Elektron pochta manzilingizni kiriting:")
domain = email.split("@")[-1]
print(f'Sizning elektron pochtangiz "{domain}" domenda ochilgan')
# ========================================================================================================

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    all_chars = letters + digits + special

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special)
    ]
    password += [random.choice(all_chars) for _ in range(length - 3)]
    random.shuffle(password)
    return "".join(password)

print("Generated password:", generate_password(12))

