import sys
import io

# Force UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def clean_text(text):
    """Remove spaces, punctuation, and convert to lowercase."""
    # Keep only letters and numbers
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned

def is_palindrome(text):
    """Check if text is a palindrome."""
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]

def main():
    print("=" * 50)
    print("       PALINDROME CHECKER")
    print("=" * 50)
    print()
    print("A palindrome reads the same forwards and backwards!")
    print("Examples: racecar, mom, wow, A man a plan a canal Panama")
    print()
    print("Type 'quit' to exit")
    print("-" * 50)

    while True:
        print()
        text = input("Enter text to check: ")

        if text.lower() == 'quit':
            print()
            print("Thanks for playing!")
            break

        if not text:
            continue

        cleaned = clean_text(text)

        if is_palindrome(text):
            print()
            print(f"  >>> YES! '{text}' is a PALINDROME! <<<")
            print(f"  Cleaned: '{cleaned}'")
            print(f"  Reversed: '{cleaned[::-1]}'")
            print()
        else:
            print()
            print(f"  >>> No, '{text}' is NOT a palindrome.")
            print(f"  Cleaned: '{cleaned}'")
            print(f"  Reversed: '{cleaned[::-1]}'")
            print()

        print("-" * 50)

if __name__ == "__main__":
    main()
