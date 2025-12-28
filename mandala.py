import random
import math
import sys
import io

# Force UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CHARS = ['@', '#', '*', '+', '.', 'o', 'O', '0', ':', '-', '~']

def mandala_char(radius, angle, layers):
    """Choose a character based on position in the mandala."""
    layer = (radius + int(angle * 10)) % len(layers)
    return layers[layer]

def generate_mandala(size=25, petals=8, layers=None):
    """Generate a mandala pattern."""
    if layers is None:
        layers = [CHARS[i % len(CHARS)] for i in range(10)]
        random.shuffle(layers)

    grid = [[' ' for _ in range(size * 2)] for _ in range(size * 2)]
    center = size

    max_radius = size - 2

    for radius in range(1, max_radius):
        for angle in range(0, 360, 5):
            rad = math.radians(angle)

            # Main point
            x = int(center + radius * math.cos(rad))
            y = int(center + radius * math.sin(rad) * 0.5)  # Flatten for aspect ratio

            if 0 <= x < size * 2 and 0 <= y < size * 2:
                # Create petal pattern
                petal_factor = math.cos(petals * rad / 2)
                if petal_factor > 0.2:
                    char_idx = int((radius / max_radius) * len(layers)) % len(layers)
                    grid[y][x] = layers[char_idx]

            # Mirror points for symmetry
            for mirror_angle in [math.pi - rad, -rad, math.pi + rad]:
                mx = int(center + radius * math.cos(mirror_angle))
                my = int(center + radius * math.sin(mirror_angle) * 0.5)

                if 0 <= mx < size * 2 and 0 <= my < size * 2:
                    petal_factor = math.cos(petals * mirror_angle / 2)
                    if petal_factor > 0.2:
                        char_idx = int((radius / max_radius) * len(layers)) % len(layers)
                        grid[my][mx] = layers[char_idx]

    # Add center
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            grid[center + dy][center + dx] = '@'

    return grid

def print_mandala(grid):
    """Print the mandala grid."""
    for row in grid:
        print(''.join(row))

def main():
    print("=" * 50)
    print("       MANDALA PATTERN GENERATOR")
    print("=" * 50)
    print()

    # Generate several unique mandalas
    for i in range(5):
        size = random.randint(15, 25)
        petals = random.choice([4, 6, 8, 12, 16])

        layers = [CHARS[i % len(CHARS)] for i in range(8)]
        random.shuffle(layers)

        mandala = generate_mandala(size, petals, layers)

        print(f"Mandala {i+1} (petals: {petals})")
        print("-" * 50)
        print_mandala(mandala)
        print()
        print()

if __name__ == "__main__":
    main()
