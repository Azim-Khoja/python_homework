# 1. Create your own virtual environment and install some python packages.
"""
1. In PyCharm terminal we will write:
python -m venv myenv

2. To activate (for macOS/Linux):
source myenv/bin/activate

3. Install packages:
pip install requests numpy pandas

4. View installed packages:
pip list

5. Save installed libraries to requirements.txt:
pip freeze > requirements.txt

6. This file can then be transferred to another project and used to install such packages:
pip install -r requirements.txt
"""

# 2. Create custom modules
"""
1. Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
creating:
project_folder/
│
├── math_operations.py
└── main.py
"""

from math_operations import add, subtract, divide, multiply

print("Addition:", add(10, 5))
print("Subtraction:", subtract(20, 15))
print("Division:", divide(30, 2))
print("Multiplication:", multiply(8, 4))

"""
2. Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

project_folder/
│
├── math_operations.py
├── string_utils.py   ← new modul
└── main.py
"""


# string_utils.py

def reverse_string(text):
    """Return the reversed version of the given string."""
    return text[::-1]


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in the given string."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count


# main.py

import string_utils as su

word = "Programming"

print("Original:", word)
print("Reversed:", su.reverse_string(word))
print("Vowel Count:", su.count_vowels(word))

# 3. Create custom packages.
"""
1. Create geometry package.
project_folder/
│
├── math_operations.py
├── string_utils.py
├── circle.py           ← new modul
└── main.py
"""

# circle.py

import math

def calculate_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2


def calculate_circumference(radius):
    """Return the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# main.py

import circle

r = 5

print("Radius:", r)
print("Area:", circle.calculate_area(r))
print("Circumference:", circle.calculate_circumference(r))

"""
2. Create file_operations package.
project_folder/
│
├── math_operations.py
├── string_utils.py
├── circle.py
├── main.py
└── file_operations/          ← new PACKAGE
    ├── __init__.py
    ├── file_read.py
    └── file_write.py
"""
# file_operations/__init__.py

# You can optionally import submodules here
from .file_read import read_file
from .file_write import write_file


# file_operations/file_read.py

def read_file(filename):
    """Read and return the content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# file_operations/file_write.py

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)
    return f"Data written to '{filename}' successfully."

# main.py

from file_operations import read_file, write_file

filename = "example.txt"

# Faylga yozish
print(write_file(filename, "Hello, Python Packages!"))

# Faylni o‘qish
print(read_file(filename))

"""
3. Define read_file function in file_reader.py. This function accepts one argument(file_path). 
Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).
project_folder/
│
├── math_operations.py
├── string_utils.py
├── circle.py
├── main.py
└── file_operations/
    ├── __init__.py
    ├── file_reader.py
    └── file_writer.py
"""

# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file

# file_operations/file_reader.py

def read_file(file_path):
    """Read the contents of a file and return it."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {e}"


# file_operations/file_writer.py

def write_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Data successfully written to '{file_path}'."
    except Exception as e:
        return f"An error occurred while writing to file: {e}"


# main.py

from file_operations import read_file, write_file

filename = "example.txt"

# Faylga yozish
print(write_file(filename, "Python modules and packages are awesome!"))

# Faylni o‘qish
print(read_file(filename))





