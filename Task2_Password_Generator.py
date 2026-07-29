import random
import string


def generate_password(length):
    """Generate a random password."""
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 45)
    print("        PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Please enter a valid number.")
            continue

        choice = input("\nGenerate another password? (yes/no): ").strip().lower()

        if choice != "yes":
            print("\nThank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
