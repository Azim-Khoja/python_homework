# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {"apple": 15, "banana": 3, "cherry": 27, "kiwi": 8}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Original Dictionary:", my_dict)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
my_dict = {
    "id": 101,
    "first_name": "Vali",
    "last_name": "Aliyev",
    "age": 18,
    "status": "verified",
    "isMarried": False
}

my_dict['gender'] = 'male'
my_dict

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
my_dict = {**dic1, **dic2, **dic3}
my_dict

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input("Sonni kiriting: "))
my_dict = {x: x * x for x in range(1, n + 1)}
print(f"{n} gacha bõlgan sonlarning kvadrati:", my_dict)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
my_dict = {x: x * x for x in range(1, 16)}
print("1 dan 16 gacha bõlgan sonlarning kvadrati:", my_dict)

# Set Exercises

# 1. Create a Set
# Write a Python program to create a set.
my_set1 = set(range(0, 10, 2))
my_set2 = set(range(1, 11, 2))

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.
print(my_set1.union(my_set2))
print(my_set1 | my_set2)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
animals = {'dog', 'fish', 'sheep', 'lion', 'tiger', 'bear'}
animals.add('snake')
animals.add('wolf')
animals.add('cat')
print(animals)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
colors = {'red', 'green', 'yellow', 'white', 'blue', 'gray', 'pink'}
colors.remove('white') # Removing
colors.discard('yellow') # Discarding

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

my_set = set(list(range(1, 11)))
num = int(input("'set()'dan o'chirish uchun 1 dan 10 gacha bo'lgan son kiriting: "))
if num in my_set:
    my_set.remove(num)
    print(f"{num} soni o'chirildi!")
    print(f"Qolgan sonlar: {my_set}")
else:
    print(f"{num} soni 'set()'da mavjud emas!")
    print(f"Mavjud sonlar: {my_set}")