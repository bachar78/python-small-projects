
import string 
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password is too short (should be at least 8 characters)")
    if not any(c.islower() for c in password):
        issues.append("Password should include at least one lowercase letter")
    if not any(c.isupper() for c in password):
        issues.append("Password should include at least one uppercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("Password should include at least one digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Password should include at least one special character")
    return issues


def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = getpass.getpass("Enter your password: ")
issues = check_password_strength(password)
if issues:
    print("Your password has the following issues:")
    for issue in issues:
        print(f"- {issue}")
else:
    print("Your password is strong!")

generate = input("Do you want to generate a strong password? (y/n): ")
if generate.lower() == 'y':
    length = int(input("Enter desired password length (at least 8): "))
    try:
        strong_password = generate_strong_password(length)
        print(f"Generated strong password: {strong_password}")
    except ValueError as e:
        print(e)