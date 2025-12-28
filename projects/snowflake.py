import random

def generate_snowflake():
    size = random.randint(7, 15)
    if size % 2 == 0:
        size += 1

    # Create a grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    center = size // 2

    # Always put a star in center
    grid[center][center] = '*'

    # Generate random snowflake pattern (6-fold symmetry)
    for _ in range(random.randint(10, 25)):
        # Random starting point in one "sector" (0-60 degrees)
        r = random.randint(1, center)
        theta = random.uniform(0, 60) * 3.14159 / 180

        # Add star in all 6 symmetric positions
        for sector in range(6):
            angle = theta + sector * 60 * 3.14159 / 180
            x = int(center + r * (2 if random.random() > 0.5 else 1) * (3.14159 / 4))
            y = int(center + r * 0.5)

            # Mirror position too
            x_mirror = 2 * center - x
            y_mirror = 2 * center - y

            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = '*'
            if 0 <= x_mirror < size and 0 <= y < size:
                grid[y][x_mirror] = '*'
            if 0 <= x < size and 0 <= y_mirror < size:
                grid[y_mirror][x] = '*'
            if 0 <= x_mirror < size and 0 <= y_mirror < size:
                grid[y_mirror][x_mirror] = '*'

    # Add some random arms
    for _ in range(6):
        direction = random.randint(0, 7)
        length = random.randint(2, center - 1)

        # 8 directions
        dx = [0, 1, 1, 1, 0, -1, -1, -1][direction]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1][direction]

        for i in range(1, length + 1):
            x = center + dx * i
            y = center + dy * i
            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = '*'

            # Mirror
            x_mirror = 2 * center - x
            y_mirror = 2 * center - y
            if 0 <= x_mirror < size and 0 <= y < size:
                grid[y][x_mirror] = '*'
            if 0 <= x < size and 0 <= y_mirror < size:
                grid[y_mirror][x] = '*'

    return grid

def print_snowflake(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    print("❄️" * 10)
    print(" SNOWFLAKE GENERATOR")
    print("❄️" * 10)
    print()

    for i in range(3):
        snowflake = generate_snowflake()
        print_snowflake(snowflake)
        print()
        print("-" * 15)
        print()
