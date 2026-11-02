import secrets
import string


def generate_password(length, selected_types, exclude_similar=False):
    characters = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "numbers": string.digits,
        "symbols": string.punctuation
    }

    similar = "0O1lI"

    # Create selected character groups
    groups = []

    for option in selected_types:
        group = characters[option]

        if exclude_similar:
            group = "".join(c for c in group if c not in similar)

        if group:
            groups.append(group)

    if len(groups) < 2:
        raise ValueError("Select at least two character types.")

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    if length < len(groups):
        raise ValueError("Password length is too short.")

    # Guarantee one character from every selected group
    password_list = [secrets.choice(group) for group in groups]

    all_characters = "".join(groups)

    # Fill the remaining positions
    while len(password_list) < length:
        password_list.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


def main():
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    selected_types = []

    options = {
        "1": ("uppercase", "Uppercase letters"),
        "2": ("lowercase", "Lowercase letters"),
        "3": ("numbers", "Numbers"),
        "4": ("symbols", "Symbols")
    }

    print("\nSelect character types:")
    for key, value in options.items():
        print(f"{key}. {value[1]}")

    while len(selected_types) < 2:
        choices = input(
            "\nEnter choices separated by commas (example: 1,2,3): "
        )

        selected_types = []

        for choice in choices.split(","):
            choice = choice.strip()

            if choice in options:
                option = options[choice][0]

                if option not in selected_types:
                    selected_types.append(option)

        if len(selected_types) < 2:
            print("Please select at least two valid types.")

    exclude = input("Exclude similar characters? (yes/no): ").lower()

    while True:
        password = generate_password(
            length,
            selected_types,
            exclude == "yes"
        )

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()