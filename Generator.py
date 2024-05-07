# Import the necessary modules
import random

def generate_password(length):
    # Define a simple set of characters for the password
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    # Randomly choose characters from the set and build the password
    password = ''
    for i in range(length):
        password += random.choice(characters)
    
    return password

# Set the desired password length
password_length = 12

# Call the function and print the generated password
print("\n Your new password is:", generate_password(password_length),"\n")
