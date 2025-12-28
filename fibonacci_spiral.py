def fibonacci(n):
    """Generate fibonacci sequence up to n numbers."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[1:]  # Skip the initial 0

def draw_ascii_spiral(size=40):
    """Draw a simple ASCII spiral representation."""
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    cx, cy = size // 2, size // 2

    # Simple spiral drawing
    x, y = cx, cy
    step = 1
    count = 0
    total = size * size // 4

    for i in range(total):
        for _ in range(step):
            if i % 4 == 0: x += 1
            elif i % 4 == 1: y += 1
            elif i % 4 == 2: x -= 1
            else: y -= 1

            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = '*'
            count += 1
            if count >= total:
                break
        if count % 2 == 0:
            step += 1

    for row in grid:
        print(''.join(row))

def draw_fibonacci_blocks():
    """Draw Fibonacci numbers as blocks forming a spiral pattern."""
    fib = fibonacci(12)

    print("FIBONACCI SPIRAL VISUALIZER")
    print("=" * 50)
    print()
    print("Fibonacci sequence:", fib)
    print()
    print("Golden ratio (phi) approx 1.61803398875...")
    print()
    print("Watch the spiral grow:")
    print("-" * 50)

    # Draw ASCII art spiral with fibonacci numbers
    print()
    for i, num in enumerate(fib[:8]):
        indent = '  ' * i
        print(f"{indent}{'*' * (num % 20 + 5)} [{num}]")

def draw_text_spiral():
    """Draw a text-based spiral representation."""
    print()
    print("    ___")
    print("   /   \\")
    print("  |  1  |___")
    print("   \\_____/   \\")
    print("   |    |  1  |")
    print("   |  2 |___/|")
    print("   |____|   ||")
    print("   |    | 3 ||")
    print("   |  5 |___||")
    print("   |____| 8 ||")
    print("        |___|")
    print()

def main():
    print("* FIBONACCI SPIRAL VISUALIZER *")
    print("=" * 50)
    print()

    # Show Fibonacci sequence
    fib = fibonacci(15)
    print("Fibonacci Sequence:")
    for i, num in enumerate(fib):
        print(f"F{i+1:2d} = {num}")
    print()

    # Show golden ratio approximation
    if len(fib) >= 3:
        print("Golden Ratio (phi) approximations:")
        for i in range(2, min(10, len(fib))):
            ratio = fib[i] / fib[i-1]
            print(f"  {fib[i]}/{fib[i-1]} = {ratio:.15f}")
    print()

    draw_text_spiral()
    draw_fibonacci_blocks()

    print()
    print("-" * 50)
    print("ASCII Spiral:")
    print()
    draw_ascii_spiral(30)

if __name__ == "__main__":
    main()
