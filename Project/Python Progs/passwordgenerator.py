import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Random Password Generator!")

while True:
    try:
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

        if password:
            print("Generated Password:", password)
        else:
            continue

        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    except ValueError:
        print("Please enter a valid password length (an integer).")

print("Thank you for using the Random Password Generator!")
