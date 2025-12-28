import random

FORTUNES = {
    "wise": [
        "A beautiful, smart, and loving person will be coming into your life.",
        "Your ability to accomplish tasks will follow with your ability to procrastinate.",
        "A dubious friend may be an enemy in camouflage.",
        "Your life will be happy and peaceful.",
        "It is better to deal with problems before they arise.",
        "A lifetime of happiness lies ahead of you.",
        "The philosophy of one century is the common sense of the next.",
        "Fortune Not Found: Abort, Retry, Ignore?",
        "From listening comes wisdom and from speaking repentance.",
        "The night life is for you.",
    ],
    "funny": [
        "You will be hungry again in one hour.",
        "Run.",
        "Error 404: Fortune not found.",
        "Your pet rock is plotting against you.",
        "Ask your mom.",
        "I cannot help you, for I am just a cookie.",
        "Don't eat the paper.",
        "The fortune you seek is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!",
        "This cookie contains no fortune.",
    ],
    "silly": [
        "You will find a item. The item will be nice.",
        "Yes.",
        "No.",
        "Maybe.",
        "Your lucky number is... wait, I forgot.",
        "If you think nobody cares if you're alive, try missing a couple of car payments.",
        "You have the capacity to learn from your mistakes. You will learn a lot today.",
        "The fact that no one understands you doesn't mean you're an artist.",
        "Don't worry about the world ending today. It's already tomorrow in Australia.",
        "If you can't convince them, confuse them.",
    ]
}

def print_cookie():
    print()
    print("    _______")
    print("   /       \\")
    print("  |  🥠   |")
    print("   \\_______/")
    print()

def print_fortune():
    category = random.choice(list(FORTUNES.keys()))
    fortune = random.choice(FORTUNES[category])
    label = category.upper()
    print(f"📜 [{label}] {fortune}")
    print()

def main():
    print("🥠" * 20)
    print("    FORTUNE COOKIE GENERATOR")
    print("🥠" * 20)
    print()

    count = int(input("How many fortunes? ") or "3")
    for _ in range(count):
        print_cookie()
        print_fortune()
        print("-" * 30)

if __name__ == "__main__":
    main()
