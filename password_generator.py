"""
Password Generator (CLI)
--------------------------
Generates strong random passwords using a mix of uppercase,
lowercase, numbers, and special characters.
"""

import random
import string


def get_length():
    while True:
        value = input("Enter desired password length (8-64): ").strip()
        if not value.isdigit():
            print("Please enter a whole number.")
            continue
        length = int(value)
        if length < 8:
            print("For security, length must be at least 8.")
            continue
        if length > 64:
            print("Length must be 64 or less.")
            continue
        return length


def get_yes_no(prompt, default=True):
    suffix = "(Y/n)" if default else "(y/N)"
    value = input(f"{prompt} {suffix}: ").strip().lower()
    if value == "":
        return default
    return value == "y"


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    pools = []
    guaranteed = []

    if use_upper:
        pools.append(string.ascii_uppercase)
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        pools.append(string.ascii_lowercase)
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        pools.append(string.digits)
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
        pools.append(symbols)
        guaranteed.append(random.choice(symbols))

    if not pools:
        raise ValueError("At least one character type must be selected.")

    all_chars = "".join(pools)
    remaining_length = max(length - len(guaranteed), 0)
    password_chars = guaranteed + [random.choice(all_chars) for _ in range(remaining_length)]

    random.shuffle(password_chars)
    return "".join(password_chars[:length])


def password_strength_label(length, type_count):
    if length >= 12 and type_count >= 3:
        return "Strong"
    elif length >= 8 and type_count >= 2:
        return "Medium"
    return "Weak"


def main():
    print("===== Password Generator =====")

    while True:
        length = get_length()
        use_upper = get_yes_no("Include uppercase letters?")
        use_lower = get_yes_no("Include lowercase letters?")
        use_digits = get_yes_no("Include numbers?")
        use_symbols = get_yes_no("Include special characters?")

        type_count = sum([use_upper, use_lower, use_digits, use_symbols])

        try:
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        except ValueError as e:
            print(f"\nError: {e}. Please select at least one character type.\n")
            continue

        strength = password_strength_label(length, type_count)

        print(f"\nGenerated Password: {password}")
        print(f"Strength: {strength}")

        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
