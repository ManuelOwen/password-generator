import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    all_chars = letters
    if numbers:
        all_chars += digits
    if special_characters:
        all_chars += special

    password = ''.join(random.choice(all_chars) for _ in range(min_length))
    return password

print(generate_password(10))
