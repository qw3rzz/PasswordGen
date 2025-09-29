import random
import string

def generate_password(length=8, use_digits=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    return ''.join(random.choice(chars) for i in range(length))

length = int(input("Enter password length: "))
use_digits = input("Use digits? (y/n): ").lower() == "y"

print("Generated password:", generate_password(length, use_digits))