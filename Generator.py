import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("\nGenerated Password:", generated_password,"\n")
