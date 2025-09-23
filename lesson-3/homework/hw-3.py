# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'banana', 'cherry', 'grapes', 'grapes']
third_fruit = fruits[2]
print("Third fruit is", third_fruit)

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
nums1 = [1, 3, 5, 7, 9]
nums2 = [0, 2, 4, 6, 8]
all_nums = nums1 + nums2
print(all_nums)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First number:", nums[0])
print(f"Middle number:", nums[len(nums) // 2])
print(f"Last number:", nums[-1])

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
films = ['Titanic', 'Harry Potter', 'Aliens vs. Predators', 'Interstellar', 'Mission Impossible']
print(tuple(films))

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['Amsterdam', 'Berlin', 'New York', 'Paris', 'Ar-Riad', 'Doha']
if "Paris" in cities:
    print('Shahar ro\'yxatda mavjud')
else:
    print('Shahar ro\'yxatda mavjud emas')

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
nums = [10, 15, 20, 25, 30, 35]
duplicate_nums = nums * 2
print(f"Duplicated numbers:", duplicate_nums)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
nums = list(range(10))
nums[0], nums[-1] = nums[-1], nums[0]
print(f"First and last numbers swaped:", nums)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
nums = tuple(range(1, 11))
sliced_nums = nums[3:8]
print(f"Sliced numbers:", sliced_nums)

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ['white', 'blue', 'pink', 'green', 'gray', 'blue', 'black', 'blue']
print(f"Index of blue:", colors.count('blue'))

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animals = ('cow', 'chicken', 'lion', 'dog', 'cat', 'horse', 'sheep', 'rabbit')
print(f"The lion was on the list:", animals.index('lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
tuple1 = tuple(range(1, 10, 2))
tuple2 = tuple(range(0, 10, 2))
merge_tuple = tuple1 + tuple2
print(f"Combined number cortege:", merge_tuple)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
tuple1 = tuple(range(10, 100, 5))
list1 = list(range(1, 11, 2))
print(f"Length of the tuple:", len(tuple1))
print(f"Length of the list:", len(list1))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
tuple_nums = tuple(range(1, 10, 2))
print("Tuple numbers:", tuple_nums)
list_nums = list(tuple_nums)
print("Converted from tuple to list:", list_nums)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
nums = (41, 23, 16, 94, 54, 20, 37, 49, 62, 70)
print("Maximal number:", max(nums))
print("Minimal number:", min(nums))

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
words = ('cat', 'banana', 'blue', 'game', 'color', 'phone', 'board')
print("Words:", words)
print("Reversed words", words[::-1])
