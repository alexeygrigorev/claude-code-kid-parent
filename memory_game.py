import random
import time
import sys
import io

# Force UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CARD_EMOJIS = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼']

def create_cards():
    """Create pairs of cards and shuffle them."""
    cards = CARD_EMOJIS * 2
    random.shuffle(cards)
    return cards

def display_board(cards, revealed, selected=None):
    """Display the game board."""
    print("\n    " + "   ".join([str(i) for i in range(len(cards))]))
    print("   " + "+----" * len(cards) + "+")

    row = " | "
    for i, card in enumerate(cards):
        if revealed[i]:
            row += f" {card} | "
        elif selected == i:
            row += f" ? | "
        else:
            row += "   | "

    print("   " + row)

    print("   " + "+----" * len(cards) + "+")

def get_input(prompt, max_val):
    """Get valid user input."""
    while True:
        try:
            val = input(prompt)
            num = int(val)
            if 0 <= num < max_val:
                return num
            print(f"Please enter a number between 0 and {max_val - 1}")
        except ValueError:
            print("Please enter a valid number!")

def play_game():
    """Main game loop."""
    print("=" * 50)
    print("       MEMORY CARD MATCHING GAME")
    print("=" * 50)
    print()
    print("Find all the matching pairs!")
    print("Enter card numbers to flip them over.")
    print()

    cards = create_cards()
    revealed = [False] * len(cards)
    turns = 0
    matches = 0

    while matches < len(CARD_EMOJIS):
        display_board(cards, revealed)

        # Get first card
        print()
        pick1 = get_input("Pick first card (0-15): ", len(cards))
        while revealed[pick1]:
            print("That card is already revealed!")
            pick1 = get_input("Pick first card (0-15): ", len(cards))

        # Reveal first card
        revealed[pick1] = True
        display_board(cards, revealed)

        # Get second card
        pick2 = get_input("Pick second card (0-15): ", len(cards))
        while pick2 == pick1 or revealed[pick2]:
            if pick2 == pick1:
                print("You can't pick the same card!")
            else:
                print("That card is already revealed!")
            pick2 = get_input("Pick second card (0-15): ", len(cards))

        # Reveal second card
        revealed[pick2] = True
        display_board(cards, revealed)

        turns += 1

        # Check for match
        if cards[pick1] == cards[pick2]:
            matches += 1
            print()
            print("   *** MATCH! ***")
        else:
            print()
            print(f"   {cards[pick1]} and {cards[pick2]} don't match...")
            time.sleep(1)
            revealed[pick1] = False
            revealed[pick2] = False

        print()
        print(f"Matches: {matches}/{len(CARD_EMOJIS)} | Turns: {turns}")
        print("-" * 50)

    # Game over - show final board
    display_board(cards, revealed)
    print()
    print("=" * 50)
    print(f"       YOU WON in {turns} turns!")
    print("=" * 50)
    print()
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
