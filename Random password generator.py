import random
import string
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_specials):
    if not (use_lowercase or use_uppercase or use_numbers or use_specials):
        return "Error: At least one character type must be selected."
    
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if characters:
        return ''.join(random.choices(characters, k=length))
    else:
        return "Error: No character types available."

print(generate_password(10, True, True, True, True)) 
