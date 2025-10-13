#### Exception Handling Exercises


# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    number1 = float(input("Bo'linuvchi raqamni kiriting:"))
    number2 = float(input("Bo'luvchi raqamni kiriting:"))
    result = number1 / number2
    print(f"{number1} ÷ {number2} =", result)
except ZeroDivisionError:
    print("Bo'luvchi raqam 0 bo'lmasligi kerak!")
finally:
    print("Jarayon yakunlandi.")

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    raqam = float(input("Istalgan raqam kiriting:"))
    print(f"Siz {raqam} raqamini kiritdingiz")
except ValueError:
    print("Siz raqam o'rniga boshqa simvol kiritdingiz.")

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open("file.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Yuklanuvchi fayl topilmadi!")
finally:
    print("Jarayon yakunlandi...")

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    a = input("1-sonni kiriting:")
    b = input("2-sonni kiriting:")

    # Sonlarni float-ga o'tkazish
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Xato: Faqat son kiritish kerak")

    # if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
    #     raise TypeError("Xato: son bo'lishi kerak")

    print(f"Yig'indi: {a} + {b} = {a + b}")

except TypeError as e:
    print(e)

# 5. Write a Python program that opens a file and handles a PermissionError exception
# if there is a permission issue.

try:
    with open('test.txt', mode='w') as file:
        print(file.read())
except PermissionError:
    print("Ruxsat etilmadi")


# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

def select_index(index):
    my_list = list(range(1, 11))
    try:
        if not isinstance(index, int):
            raise TypeError("Index butun son bo'lishi kerak!")
        return my_list[index]
    except IndexError:
        print("Xato: Index diapazondan tashqarida!")
    except TypeError as e:
        return f"Xato: {e}"


print(select_index("asd"))

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    # Son kiritamiz
    number = int(input("Iltimos, biror son kiriting: "))
    print("Siz kiritgan son:", number)

    # Agar foydalanuvchi kiritishni bekor qilsa, xato haqida xabar beramiz
except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi!")

    # Agar sondan boshqa simvol kiritilsa, xatolik qaytaramiz
except ValueError:
    print("Siz son kiritmadingiz!")

    # Har qanday vaziyatda ham bu amal bajariladi
finally:
    print("Dastur tugadi.")

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("example.txt", encoding="utf-8", errors="ignore") as f:
        content = f.read()
except UnicodeDecodeError:
    print("The file couldn't be read, it's not valid utf-8.")
else:
    print(content)

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    data = ()
    data.pop(0)
    print("O'chirildi")
except AttributeError:
    print("Bunday turdagi ma'lumot mavjud emas!")


#### Python File Input Output: Exercises, Practice, Solution

# 1. Write a Python program to read an entire text file.

try:
    file_name = input("Please enter the file name:")
    with open(file_name, mode='r') as f:
        lines = f.read()
        print(lines)
except FileNotFoundError as e:
    print(e)

# 2. Write a Python program to read first n lines of a file.

file_name = input("Foydalanmoqchi bo'lgan faylingiz nomini kiriting: ")

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines[:5]:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")

# 3. Write a Python program to append text to a file and display the text.

import os

file_name = input("Foydalanmoqchi bo'lgan faylingiz nomini kiriting: ")
text = input("Qo'shmoqchi bo'lgan matningizni kiriting: ")
try:
    # File bor bo'lsa uni yozish uchun ochish
    if os.path.exists(file_name):
        with open(file_name, "w") as file1:
            lines = file1.write(text)
    else:
        raise FileNotFoundError(f"Sizning {file_name} faylingiz topilmadi!")

    with open(file_name, "r") as file2:
        lines2 = file2.readlines()
        for line in lines2:
            print(line.strip())
except Exception:
    print("File toplimadi!")

# 4. Write a Python program to read last n lines of a file.

file_name = input("Foydalanmoqchi bo'lgan faylingiz nomini kiriting: ")

try:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines[-5:]:
                print(line.strip())
    else:
        raise FileNotFoundError(f"Faylingiz topilmadi!")
except FileNotFoundError:
    print("File topilmadi!")

# 5. Write a Python program to read a file line by line and store it into a list.

file_name = input("Foydalanmoqchi bo'lgan faylingiz nomini kiriting: ")
try:
    if os.path.exists(file_name):
        new_list = []
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                new_list.append(line)
        for item in new_list:
            print(item.strip())
    else:
        raise FileNotFoundError("Kiritgan faylingiz topilmadi!")
except FileNotFoundError:
    print(f"{file_name} nomli fayl topilmadi!")

# 6. Write a Python program to read a file line by line and store it into a variable.

file_name = input("Foydalanmoqchi bo'lgan faylingiz nomini kiriting: ")
try:
    if os.path.exists(file_name):
        # new_list = []
        variable = ""
        n = 1
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                variable += f"{n}. {line}"
                n += 1
        print("Fayldan o'qilgan ma'lumotlar:")
        print(variable)
        # for item in new_list:
        #     print(item.strip())
    else:
        raise FileNotFoundError("Kiritgan faylingiz topilmadi!")
except FileNotFoundError:
    print(f"{file_name} nomli fayl topilmadi!")

# 7. Write a Python program to read a file line by line and store it into an array.

import os

file_name = input("Fayl nomini kiriting: ")

try:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()  # barcha qatorlarni list sifatida o‘qiydi
            lines = [line.strip() for line in lines]  # \n belgilarini olib tashlaymiz

        print("\nFayldan o‘qilgan qatorlar:")
        print(lines)
    else:
        raise FileNotFoundError("Kiritilgan fayl topilmadi!")
except FileNotFoundError:
    print(f"{file_name} nomli fayl topilmadi!")


# 8. Write a Python program to find the longest words.

def find_longest_words(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                words = file.read().split()
                max_length = max(len(word) for word in words)
                longest_word = [word for word in words if len(word) == max_length]
            print(f'Fayldagi eng uzun so\'z: "{longest_word[0]}"')
        else:
            raise FileNotFoundError("Kiritilgan fayl topilmadi!")
    except FileNotFoundError:
        print(f"{file_name} nomli fayl topilmadi!")


find_longest_words('example.txt')

# 9. Write a Python program to count the number of lines in a text file.

import os


def find_longest_words(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                lines = file.readlines()
                # longest_word = [word for word in words if type(word) == int]
            print(f'Fayldagi qatorlar soni: {len(lines)}')
        else:
            raise FileNotFoundError("Kiritilgan fayl topilmadi!")
    except FileNotFoundError:
        print(f"{file_name} nomli fayl topilmadi!")


find_longest_words('example.txt')


# 10. Write a Python program to count the frequency of words in a file.

def frequency_words(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                words = file.read().split()
                frequency = {}
                for word in words:
                    word = word.lower()
                    if word in frequency:
                        frequency[word] += 1
                    else:
                        frequency[word] = 1
            return frequency
        else:
            raise FileNotFoundError(f"{file_name} fayl topilmadi!")
    except FileNotFoundError:
        print("Kiritilgan fayl topilmadi")


frequency_words("example.txt")


# 11. Write a Python program to get the file size of a plain file.

def get_file_size(file_name):
    try:
        if os.path.exists(file_name):
            file_size = os.path.getsize(file_name)
        else:
            raise FileNotFoundError(f"{file_name} fayl topilmadi!")
        # Faylni KB-ga o'tkazamiz
        return f"{round(file_size / 1024, 2)} KB"
    except FileNotFoundError:
        print("Ko'rsatilgan manzildagi file topilmadi!")


print(get_file_size("example.pdf"))


# 12. Write a Python program to write a list to a file.

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as e:
        print("Xato:", e)


write_to_file("example.txt", ["This is first", "This is second", "This is third"])


# 13. Write a Python program to copy the contents of a file to another file

def copy_files(source, destination):
    try:
        with open(source, "r") as file:
            content = file.read()

        with open(destination, "w") as file:
            dest = file.write(content)
        print(f"{source}-dagi ma'lumotlar {destination} fayliga nusxalandi!")
    except FileNotFoundError:
        print("Bunday fayllar topilmadi")


copy_files("example.txt", "newFile.txt")


# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

def combine_files(file1_name, file2_name, combined_file):
    try:
        with open(file1_name, "r") as file1, open(file2_name, "r") as file2, open(combined_file, "w") as outfile:
            for line1, line2 in zip(file1, file2):  # har ikkala fayldan bir xil vaqtda qator olish
                combined_line = line1.strip() + " " + line2.strip() + "\n"
                outfile.write(combined_line)

        print(f"'{file1_name}' va '{file2_name}' fayllar birlashtirildi va '{combined_file}' fayliga yozildi.")
    except FileNotFoundError:
        print("Fayllardan biri topilmadi!")


combine_files("example.txt", "newFile.txt", "test.txt")

# 15. Write a Python program to read a random line from a file.

import os
import random as r

file_name = input("Fayl nomini kiriting: ")

try:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()  # barcha qatorlarni list sifatida o‘qiydi

            choice = r.choice(lines)
        print(f"\n{file_name} faylidan o‘qilgan tasodifiy qator:")
        print(choice)
    else:
        raise FileNotFoundError("Kiritilgan fayl topilmadi!")
except Exception as e:
    print(f"Xatolik:", e)


# 16. Write a Python program to assess if a file is closed or not.

def check_file_closed(file_name):
    try:
        if os.path.exists(file_name):
            if file_name.closed == False:
                print("file opened!")
            else:
                print("file already closed!")
        else:
            raise FileNotFoundError(f"{file_name} nomli fayl topilmadi!")
    except Exception as e:
        print(f"Xatolik:{e}")


# 17. Write a Python program to remove newline characters from a file.

def remove_line(file_name, content):
    try:
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                lines = file.readlines()

            with open(file_name, "w") as file:
                for line in lines:
                    if content not in line:
                        file.write(line)

            print(f"{file_name} faylidan '{content}' so‘zi o‘z ichiga olgan qatorlar o‘chirildi.")
        else:
            raise FileNotFoundError("Kiritilgan fayl topilmadi!")
    except Exception as e:
        print("Xatolik:", e)


remove_line("out.txt", "This is first")

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file
# Note: Some words can be separated by a comma with no space

import os
import re  # regex bilan ishlash uchun

file_name = input("Fayl nomini kiriting: ")

try:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            text = file.read()

        # Vergul, nuqta va boshqa belgilardan tozalaymiz
        # So'zlarni topish uchun regex ishlatamiz
        words = re.findall(r"[A-Za-z0-9']+", text)

        print(f"Fayldagi so'zlar soni: {len(words)} ta")
    else:
        raise FileNotFoundError("Kiritilgan fayl topilmadi!")
except FileNotFoundError:
    print(f"'{file_name}' fayli topilmadi!")

# 19. Write a Python program to extract characters from various text files and put them into a list

import os

file_names = input("Fayl nomlarini vergul bilan kiriting (masalan: a.txt,b.txt,c.txt): ").split(",")

characters = []

try:
    for name in file_names:
        name = name.strip()
        if os.path.exists(name):
            with open(name, "r") as file:
                content = file.read()
                characters.extend(list(content))
        else:
            print(f"Fayl topilmadi: {name}")

    print("\nBarcha fayllardan o‘qilgan belgilar:")
    print(characters)

    print(f"\nUmumiy belgilar soni: {len(characters)} ta")

except Exception as e:
    print(f"Xato yuz berdi: {e}")

# 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

for harf in string.ascii_uppercase:
    with open(f"{harf}.txt", "w") as file:
        file.write(f"Bu {harf}.txt faylidir.\n")

print("26 ta fayl muvaffaqiyatli yaratildi.")

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

file_name = "alphabet.txt"
letters_per_line = int(input("Har bir qatorga nechta harf yozilsin? "))

letters = string.ascii_lowercase  # yoki string.ascii_uppercase
with open(file_name, "w") as file:
    for i in range(0, len(letters), letters_per_line):
        line = letters[i:i + letters_per_line]
        file.write(line + "\n")

print(f"{file_name} fayl yaratildi va harflar joylashtirildi.")
