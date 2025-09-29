import random
import string

def generate_password(length=8, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        safe_specials = "!@#$%&*-_"
        chars += safe_specials
    return ''.join(random.choice(chars) for i in range(length))

length = int(input("Enter password length: "))
use_digits = input("Use digits? (y/n): ").lower() == "y"
use_specials = input("Use special characters? (y/n): ").lower() == "y"

print("Generated password:", generate_password(length, use_digits, use_specials))