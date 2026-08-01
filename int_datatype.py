# ==========================================
# File Name: sum_even_odd_positions.py
# Task:
# Calculate the sum of digits at even
# positions and odd positions.
# ==========================================

# Get input from the user
number = input("Enter a number: ")

even_sum = 0
odd_sum = 0

# Loop through each digit
for i in range(len(number)):

    digit = int(number[i])

    # Position starts from 1
    position = i + 1

    if position % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit

# Display the result
print("\nSum of digits at odd positions:", odd_sum)
print("Sum of digits at even positions:", even_sum)