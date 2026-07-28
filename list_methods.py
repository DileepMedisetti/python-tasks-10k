# Function to remove duplicate elements
def remove_duplicates(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Function to find maximum value and its index
def find_max(lst):
    max_value = max(lst)
    index = lst.index(max_value)

    return max_value, index


# Function to filter even numbers
def filter_even(lst):
    even_numbers = []

    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


# Function to calculate sum of elements
def sum_elements(lst):
    total = 0

    for num in lst:
        total += num

    return total


# Sample List
numbers = [10, 20, 30, 20, 40, 10, 50]

print("Original List:", numbers)

print("\nAfter Removing Duplicates:")
print(remove_duplicates(numbers))

maximum, position = find_max(numbers)

print("\nMaximum Value:", maximum)
print("Index:", position)

print("\nEven Numbers:")
print(filter_even(numbers))

print("\nSum of Elements:")
print(sum_elements(numbers))

double_values = [num * 2 for num in numbers]

print("\nDouble Values:")
print(double_values)

# Sample output
""" 
Original List: [10, 20, 30, 20, 40, 10, 50]

After Removing Duplicates:
[10, 20, 30, 40, 50]

Maximum Value: 50
Index: 6

Even Numbers:
[10, 20, 30, 20, 40, 10, 50]

Sum of Elements:
180

Double Values:
[20, 40, 60, 40, 80, 20, 100]
"""