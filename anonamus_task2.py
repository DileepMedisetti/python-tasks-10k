# -----------------------------------------
# Anonymous Functions (Lambda) Assignment
# -----------------------------------------

from functools import reduce

# -----------------------------------------
# Task 1: Convert a string to uppercase
# using an anonymous (lambda) function
# -----------------------------------------

uppercase = lambda text: text.upper()

print("Task 1:")
print(uppercase("python programming"))


# -----------------------------------------
# Task 2: Square all numbers in a list
# using map() and lambda
# -----------------------------------------

numbers = [1, 2, 3, 4, 5]

square_numbers = list(map(lambda x: x * x, numbers))

print("\nTask 2:")
print("Original List:", numbers)
print("Squared List:", square_numbers)


# -----------------------------------------
# Task 3: Extract even numbers
# using filter() and lambda
# -----------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nTask 3:")
print("Original List:", numbers)
print("Even Numbers:", even_numbers)


# -----------------------------------------
# Task 4: Find the product of all numbers
# using reduce() and lambda
# -----------------------------------------

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print("\nTask 4:")
print("Numbers:", numbers)
print("Product:", product)


# -----------------------------------------
# Task 5: List of dictionaries
# -----------------------------------------

people = [
    {"name": "Rahul", "age": 25},
    {"name": "Anjali", "age": 16},
    {"name": "Dileep", "age": 21},
    {"name": "Priya", "age": 17},
    {"name": "Suresh", "age": 35}
]

# Extract all names using map()
names = list(map(lambda person: person["name"], people))

# Filter people who are 18 years or older
adults = list(filter(lambda person: person["age"] >= 18, people))

# Sort people by age in descending order
sorted_people = sorted(
    people,
    key=lambda person: person["age"],
    reverse=True
)

print("\nTask 5:")

print("\nNames:")
print(names)

print("\nPeople Aged 18 and Above:")
print(adults)

print("\nPeople Sorted by Age (Descending):")
print(sorted_people)

#===================================================================================
#Sample outputs

# Task 1:
# PYTHON PROGRAMMING

# Task 2:
# Original List: [1, 2, 3, 4, 5]
# Squared List: [1, 4, 9, 16, 25]

# Task 3:
# Original List: [10, 15, 20, 25, 30, 35, 40]
# Even Numbers: [10, 20, 30, 40]

# Task 4:
# Numbers: [2, 3, 4, 5]
# Product: 120

# Task 5:

# Names:
# ['Rahul', 'Anjali', 'Dileep', 'Priya', 'Suresh']

# People Aged 18 and Above:
# [{'name': 'Rahul', 'age': 25}, {'name': 'Dileep', 'age': 21}, {'name': 'Suresh', 'age': 35}]

# People Sorted by Age (Descending):
# [{'name': 'Suresh', 'age': 35}, {'name': 'Rahul', 'age': 25}, {'name': 'Dileep', 'age': 21}, {'name': 'Priya', 'age': 17}, {'name': 'Anjali', 'age': 16}]