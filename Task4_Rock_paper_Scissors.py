import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=" * 40)
print("     ROCK PAPER SCISSORS GAME")
print("=" * 40)

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("\nGame Over!")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")

        if user_score > computer_score:
            print("Congratulations! You won the game.")
        elif computer_score > user_score:
            print("Computer won the game.")
        else:
            print("The game is a tie.")
        break

    if choice == "1":
        user_choice = "rock"
    elif choice == "2":
        user_choice = "paper"
    elif choice == "3":
        user_choice = "scissors"
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")