
# Declare Variables of Different Datatypes and Print Their Types

# Integer
age = 21

# Float
height = 5.8

# String
name = "Dileep"

# List
subjects = ["Python", "SQL", "AI", "ML"]

# Dictionary
student = {
    "id": 101,
    "course": "AIML",
    "college": "BVCEC"
}

print("Age:", age, "-", type(age))
print("Height:", height, "-", type(height))
print("Name:", name, "-", type(name))
print("Subjects:", subjects, "-", type(subjects))
print("Student:", student, "-", type(student))


# Calculate Mean, Median, and Standard Deviation
import statistics

def calculate_statistics(numbers):
    result = {
        "Mean": statistics.mean(numbers),
        "Median": statistics.median(numbers),
        "Standard Deviation": statistics.stdev(numbers)
    }
    return result

numbers = [10, 20, 30, 40, 50]

output = calculate_statistics(numbers)

print(output)

# Count Occurrence of Each Word
text = input("Enter a sentence: ")

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Count:")

for word, count in word_count.items():
    print(word, ":", count)
    
# Person Class
class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


person1 = Person(
    "Dileep",
    21,
    {
        "City": "Amalapuram",
        "State": "Andhra Pradesh"
    }
)

person2 = Person(
    "Rahul",
    22,
    {
        "City": "Hyderabad",
        "State": "Telangana"
    }
)

print("Person 1")
print("Name:", person1.name)
print("Age:", person1.age)
print("Address:", person1.address)

print()

print("Person 2")
print("Name:", person2.name)
print("Age:", person2.age)
print("Address:", person2.address)

# Modify attributes
person1.age = 22
person1.address["City"] = "Visakhapatnam"

print("\nAfter Modification")

print("Name:", person1.name)
print("Age:", person1.age)
print("Address:", person1.address)