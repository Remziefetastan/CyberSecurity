import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # Creating a character pool
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Creating a password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to Password Generator!")

# Get length of password
length = int(input("Enter your password length "))

# Get type of characters
include_uppercase = input("Upper case? (Y/N): ").strip().lower() == 'y'
include_numbers = input("Numbers? (Y/N): ").strip().lower() == 'y'
include_symbols = input("Symbols? (Y/N): ").strip().lower() == 'y'

# Create of password and print
password = generate_password(length, include_uppercase, include_numbers, include_symbols)
print(f"Created password: {password}")

# Get file name to save
file_name = input("Enter file name to save (with '.txt'): ")

description = input(" Add description: ")

# Add password to file
with open(file_name, 'a', encoding='utf-8') as file:
    file.write(description +'\t' + password + '\n')

print(file_name + " Password written.")
