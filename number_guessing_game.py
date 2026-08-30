import random

print("===================================")
print("   Welcome to the Number Guessing Game!")
print("===================================")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it before you run out of chances!\n")

# Difficulty selection
print("Please select the difficulty level:")
print("1. Easy   (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard   (3 chances)")

while True:
    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        difficulty = "Easy"
        chances = 10
        break
    elif choice == "2":
        difficulty = "Medium"
        chances = 5
        break
    elif choice == "3":
        difficulty = "Hard"
        chances = 3
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print(f"\nGreat! You selected {difficulty} difficulty.")
print("Let's start the game!\n")

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0

# Game loop
while attempts < chances:
    try:
        guess = int(input("Enter your guess: "))

        # Check if guess is within range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print(
                f"\nCongratulations! You guessed the correct number "
                f"in {attempts} attempts!"
            )
            break

        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}.")

        else:
            print(f"Incorrect! The number is less than {guess}.")

        # Show remaining chances
        remaining = chances - attempts

        if remaining > 0:
            print(f"You have {remaining} chance(s) left.\n")

    except ValueError:
        print("Please enter a valid number.")

# If player ran out of chances
if attempts == chances and guess != secret_number:
    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")