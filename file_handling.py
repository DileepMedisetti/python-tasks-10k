# ==========================================
# Assignment: File Handling in Python
# Topic: Absolute Path and Relative Path
# ==========================================

import os

# ------------------------------------------
# Relative Path Example
# ------------------------------------------

print("Writing using Relative Path...")

file = open("student.txt", "w")
file.write("Name: Dileep\n")
file.write("Course: Python\n")
file.write("Topic: File Handling")
file.close()

print("Data written successfully using Relative Path.")

# Read the file
file = open("student.txt", "r")
print("\nReading from Relative Path:")
print(file.read())
file.close()


# ------------------------------------------
# Absolute Path Example
# ------------------------------------------

absolute_path = os.path.abspath("student.txt")

print("\nAbsolute Path:")
print(absolute_path)

# Open file using Absolute Path
file = open(absolute_path, "a")
file.write("\nStatus: Completed")
file.close()

# Read again
file = open(absolute_path, "r")
print("\nReading using Absolute Path:")
print(file.read())
file.close()