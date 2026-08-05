
# ==========================================
# Assignment: Recursion
# Topic: String Expansion
# Input : a10b2c2
# Output: aaaaaaaaaabbcc
# ==========================================

def expand_string(text, index):

    # Base case
    if index >= len(text):
        return ""

    # Get the character
    ch = text[index]
    index += 1

    # Read the number after the character
    number = ""

    while index < len(text) and text[index].isdigit():
        number += text[index]
        index += 1

    # Return current expansion + recursive call
    return ch * int(number) + expand_string(text, index)


# Input
text = input("Enter the string: ")

# Function call
result = expand_string(text, 0)

# Output
print("Expanded String:", result)

