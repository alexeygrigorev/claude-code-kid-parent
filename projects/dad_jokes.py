import random
import sys
import io

# Force UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DAD_JOKES = [
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("What do you call a fake noodle?", "An impasta!"),
    ("Why did the scarecrow win an award?", "He was outstanding in his field!"),
    ("What do you call a bear with no teeth?", "A gummy bear!"),
    ("Why don't eggs tell jokes?", "They'd crack each other up!"),
    ("What did the ocean say to the beach?", "Nothing, it just waved!"),
    ("Why did the bicycle fall over?", "Because it was two-tired!"),
    ("What do you call a can opener that doesn't work?", "A can't opener!"),
    ("Why did the math book look so sad?", "Because it had too many problems!"),
    ("What do you call a fish without eyes?", "A fsh!"),
    ("Why don't skeletons fight each other?", "They don't have the guts!"),
    ("What did the grape do when it got stepped on?", "Nothing, it just let out a little wine!"),
    ("Why couldn't the leopard play hide and seek?", "Because he was always spotted!"),
    ("What do you call a dinosaur that crashes their car?", "Tyrannosaurus Wrecks!"),
    ("Why did the coffee file a police report?", "It got mugged!"),
    ("What do you call a pile of cats?", "A meowtain!"),
    ("Why don't ants get sick?", "Because they have tiny anty-bodies!"),
    ("What do you call a lazy kangaroo?", "A pouch potato!"),
    ("Why did the picture go to jail?", "Because it was framed!"),
    ("What do you call a sleeping dinosaur?", "A dino-snore!"),
    ("Why did the cookie cry?", "Because his mom was a wafer so long!"),
    ("What do you call a dinosaur that knows a lot of words?", "Thesaurus!"),
    ("Why did the golfer bring two pairs of pants?", "In case he got a hole in one!"),
    ("What do you call a fish wearing a bowtie?", "Sofishticated!"),
    ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
    ("What do you call a pony with a cough?", "A little horse!"),
    ("Why couldn't the pirate learn the alphabet?", "He kept getting lost at C!"),
    ("What do you call a cow with no legs?", "Ground beef!"),
    ("Why did the chicken join a band?", "Because he had the drumsticks!"),
    ("What do you call a duck that steals?", "A robber ducky!"),
    ("Why do cows wear bells?", "Because their horns don't work!"),
]

def tell_joke():
    """Tell a random dad joke."""
    setup, punchline = random.choice(DAD_JOKES)
    print()
    print("=" * 50)
    print("       DAD JOKE TIME!")
    print("=" * 50)
    print()
    print(setup)
    print()
    input("(Press Enter for the punchline...)")
    print()
    print("    " + punchline)
    print()
    print("*groan*")
    print()
    print("=" * 50)

def main():
    print()
    print("=" * 50)
    print("       WELCOME TO THE DAD JOKE TELLER!")
    print("=" * 50)
    print()
    print("Get ready for some seriously groan-worthy jokes!")
    print()

    while True:
        choice = input("Press Enter for a joke (or 'quit' to exit): ").strip().lower()

        if choice == 'quit':
            print()
            print("Thanks for the laughs! Stay groovy!")
            break

        tell_joke()
        print()

if __name__ == "__main__":
    main()
