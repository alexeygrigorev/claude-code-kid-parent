import random
import sys

# Fix encoding for Windows console
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def rock_paper_scissors():
    print("🎮 ROCK PAPER SCISSORS 🎮")
    print("=" * 30)
    print("Let's play! Type your choice or 'quit' to stop.")
    print()

    choices = ["rock", "paper", "scissors"]
    emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

    while True:
        # Get player's choice
        player = input("Your choice (rock/paper/scissors): ").lower().strip()

        if player == "quit":
            print("Thanks for playing! See you next time! 👋")
            break

        if player not in choices:
            print("Hmm, that's not a valid choice! Try again! 😊")
            print()
            continue

        # Computer makes random choice
        computer = random.choice(choices)

        # Show the choices
        print(f"\nYou chose: {emojis[player]} {player}")
        print(f"Computer chose: {emojis[computer]} {computer}")

        # Determine the winner
        if player == computer:
            print("Result: It's a TIE! 🤝")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("Result: YOU WIN! 🎉🏆")
        else:
            print("Result: Computer wins! 🤖 Better luck next time!")

        print()

if __name__ == "__main__":
    rock_paper_scissors()
