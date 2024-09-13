import string
import secrets

def generate_password(length=12):
    """
    Generate a secure random password.

    Parameters:
    length (int): The length of the password to generate. Default is 12.

    Returns:
    str: A randomly generated password string.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lowercase + uppercase + digits + symbols
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the list to prevent the first four characters from being predictable
    secrets.SystemRandom().shuffle(password)

    # Join the list into a string to form the final password
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    desired_length = 16  # You can change the desired password length here
    generated_password = generate_password(desired_length)
    print(f"Generated Password: {generated_password}")
