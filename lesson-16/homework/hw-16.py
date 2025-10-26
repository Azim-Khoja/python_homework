import numpy as np


# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

def np_converter(new_list):
    if isinstance(new_list, list):
        try:
            arr = np.array(new_list)
            return arr
        except Exception as e:
            print(e)
    else:
        print("Please, give the function a 'list' data type!")

    return None


my_list = [12.23, 13.32, 100, 36.32]
print(np_converter(my_list))


# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

def matrix_3x3(a, b):
    try:
        arr = np.arange(a, b).reshape(3, 3)
        return arr
    except Exception as e:
        print(e)


print(matrix_3x3(2, 11))

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

zeros = np.zeros(10)
zeros[6] = 11
print(zeros)

# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

arr = np.arange(12, 38)
print(arr)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array [1, 2, 3, 4]

arr = [1, 2, 3, 4]  # creating array case1
arr = np.arange(1, 5)  # creating array case2
print(arr.astype(float))

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees.
# Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Fahrenheit to Celsius
fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])
celsius = (fahrenheit - 32) * 5 / 9

print("Values in Fahrenheit degrees:", fahrenheit)
print("Values in Centigrade degrees:", np.round(celsius, 2))

# Celsius to Fahrenheit
celsius2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit2 = (celsius2 * 9 / 5) + 32

print("\nValues in Centigrade degrees:", celsius2)
print("Values in Fahrenheit degrees:", np.round(fahrenheit2, 2))

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

arr1 = np.array([10, 20, 30])
arr2 = np.arange(40, 100, 10)

upd_arr = np.append(arr1, arr2)
print("Array1:", arr1)
print("Array2:", arr2)
print("Total array of first & second:", upd_arr)

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

arr = np.random.randint(10, 100, 10)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation", np.std(arr))

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

arr = np.random.randint(10, 100, (10, 10))

print("Max number:", np.min(arr))
print("Min number:", np.max(arr))

# 10. Create a 3x3x3 array with random values.

arr = np.random.randint(1, 10, 9).reshape(3, 3)
print("Array with random values:\n", arr)
