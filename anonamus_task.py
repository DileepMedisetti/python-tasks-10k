# -----------------------------------------
# Anonymous Functions (Lambda) in Python
# -----------------------------------------

from functools import reduce

# -----------------------------------------
# Task 1: Square each number using lambda
# -----------------------------------------

numbers = [1, 2, 3, 4, 5]

square_numbers = list(map(lambda x: x * x, numbers))

print("Original Numbers:")
print(numbers)

print("\nSquare of Each Number:")
print(square_numbers)


# -----------------------------------------
# Task 2: Convert strings to uppercase
# using map() and lambda
# -----------------------------------------

fruits = ["apple", "banana", "mango", "grapes"]

uppercase_fruits = list(map(lambda x: x.upper(), fruits))

print("\nOriginal Fruits:")
print(fruits)

print("\nUppercase Fruits:")
print(uppercase_fruits)


# -----------------------------------------
# Task 3: Filter even numbers
# using filter() and lambda
# -----------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nOriginal Numbers:")
print(numbers)

print("\nEven Numbers:")
print(even_numbers)


# -----------------------------------------
# Task 4: Find the sum of numbers
# using reduce() and lambda
# -----------------------------------------

# numbers = [5, 10, 15, 20]

# total = reduce(lambda x, y: x + y, numbers)

# print("\nNumbers:")
# print(numbers)

# print("\nSum of Numbers:")
# print(total)


# # -----------------------------------------
# # Task 5: Get names of people
# # older than 30 using lambda
# # -----------------------------------------

# def get_people_above_30(people):

#     # Filter people whose age is greater than 30
#     filtered_people = list(filter(lambda person: person["age"] > 30, people))

#     # Extract names
#     names = list(map(lambda person: person["name"], filtered_people))

#     return names


# people = [
#     {"name": "Rahul", "age": 25},
#     {"name": "Dileep", "age": 31},
#     {"name": "Priya", "age": 28},
#     {"name": "Suresh", "age": 40},
#     {"name": "Anjali", "age": 35}
# ]

# result = get_people_above_30(people)

# print("\nPeople Older Than 30:")
# print(result)


# # -----------------------------------------
# # Task 6: Demonstration of Anonymous Functions
# # -----------------------------------------

# print("\n----- Demonstration -----")

# print("1. Square Numbers:")
# print(square_numbers)

# print("\n2. Uppercase Strings:")
# print(uppercase_fruits)

# print("\n3. Even Numbers:")
# print(even_numbers)

# print("\n4. Sum of Numbers:")
# print(total)

# print("\n5. Names of People Older Than 30:")
# print(result)


# # ======================================================

# # Sample outputs

# Original Numbers:
# [1, 2, 3, 4, 5]

# Square of Each Number:
# [1, 4, 9, 16, 25]

# Original Fruits:
# ['apple', 'banana', 'mango', 'grapes']

# Uppercase Fruits:
# ['APPLE', 'BANANA', 'MANGO', 'GRAPES']

# Original Numbers:
# [10, 15, 20, 25, 30, 35, 40]

# Even Numbers:
# [10, 20, 30, 40]

# Numbers:
# [5, 10, 15, 20]

# Sum of Numbers:
# 50

# People Older Than 30:
# ['Dileep', 'Suresh', 'Anjali']

# ----- Demonstration -----

# 1. Square Numbers:
# [1, 4, 9, 16, 25]

# 2. Uppercase Strings:
# ['APPLE', 'BANANA', 'MANGO', 'GRAPES']

# 3. Even Numbers:
# [10, 20, 30, 40]

# 4. Sum of Numbers:
# 50

# 5. Names of People Older Than 30:
# ['Dileep', 'Suresh', 'Anjali']