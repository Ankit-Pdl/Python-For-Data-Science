import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 1:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 40)
    print("       🔐 Password Generator")
    print("=" * 40)

    length = get_positive_int("Password length: ")
    use_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    print()

    while True:
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")

        again = get_yes_no("\nGenerate another password with same settings? (y/n): ")
        if not again:
            break

    print("\nGoodbye! Stay secure. 🔒")


if __name__ == "__main__":
    main()