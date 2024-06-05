import random
import string

#Are you actively coding by yourself
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    return length, use_uppercase, use_lowercase, use_digits, use_special

def main():
    length, use_uppercase, use_lowercase, use_digits, use_special = get_user_input()
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

