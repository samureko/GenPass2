import string
import secrets

def generate_password(length=12, use_uppercase=True, use_digits=True, use_punctuation=True):
     characters = string.ascii_lowercase
     if use_uppercase:
         characters += string.ascii_uppercase
     if use_digits:
         characters += string.digits
     if use_punctuation:
         characters += string.punctuation

     password = ''.join(secrets.choice(characters) for _ in range(length))
     return password

def is_strong_password(password):
     # Checking password complexity (example)
     return any(c.isupper() for c in password) and any(c.isdigit() for c in password)

if __name__ == "__main__":
     while True:
         password_length = int(input("Enter password length (default 12): ") or 12)
         use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
         use_digits = input("Include digits? (y/n): ").lower() == 'y'
         use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

         generated_password = generate_password(
             length=password_length,
             use_uppercase=use_uppercase,
             use_digits=use_digits,
             use_punctuation=use_punctuation
         )

         if is_strong_password(generated_password):
             print(f"\nGenerated strong password: {generated_password}\n")
             break
         else:
             print("The generated password is not strong. Please adjust the options.\n")
