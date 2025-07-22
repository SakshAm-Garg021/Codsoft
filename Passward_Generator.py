import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print(" Welcome to the Password Generator!")
try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print("\nGenerated Password:", password)
except ValueError:
    print("Please enter a valid number.")



