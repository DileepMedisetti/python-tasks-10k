# -----------------------------------------
# List Methods Practice Assignment
# -----------------------------------------

# Task 1: Create a list of integers from 1 to 20

numbers = []

for i in range(1, 21):
    numbers.append(i)

print("Original List:")
print(numbers)


# -----------------------------------------
# Task 2: Use append(), insert(), and remove()
# -----------------------------------------

# Append a new element
numbers.append(21)
print("\nAfter append(21):")
print(numbers)

# Insert an element at index 5
numbers.insert(5, 100)
print("\nAfter insert(5, 100):")
print(numbers)

# Remove an element
numbers.remove(100)
print("\nAfter remove(100):")
print(numbers)


# -----------------------------------------
# Task 3: Sort the list in ascending
# and descending order
# -----------------------------------------

def sort_list(my_list):

    # Ascending Order
    ascending = my_list.copy()
    ascending.sort()

    # Descending Order
    descending = my_list.copy()
    descending.sort(reverse=True)

    print("\nAscending Order:")
    print(ascending)

    print("\nDescending Order:")
    print(descending)


sort_list(numbers)


# -----------------------------------------
# Task 4: List Comprehension
# Create a list of squares
# -----------------------------------------

square_list = [num * num for num in numbers]

print("\nSquare List:")
print(square_list)


# -----------------------------------------
# Task 5: Find and Remove Duplicates
# while preserving original order
# -----------------------------------------

def remove_duplicates(my_list):

    new_list = []

    for item in my_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


# Add duplicate values for testing
numbers.append(5)
numbers.append(10)
numbers.append(15)

print("\nList with Duplicates:")
print(numbers)

unique_list = remove_duplicates(numbers)

print("\nList After Removing Duplicates:")
print(unique_list)

#Sample Outputs
""" 
Original List:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

After append(21):
[1, 2, 3, ..., 20, 21]

After insert(5, 100):
[1, 2, 3, 4, 5, 100, 6, 7, ..., 21]

After remove(100):
[1, 2, 3, 4, 5, 6, 7, ..., 21]

Ascending Order:
[1, 2, 3, ..., 21]

Descending Order:
[21, 20, 19, ..., 1]

Square List:
[1, 4, 9, 16, ..., 441]

List with Duplicates:
[1, 2, 3, ..., 21, 5, 10, 15]

List After Removing Duplicates:
[1, 2, 3, ..., 21]
"""