def count_total_removed(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    total_removed = 0

    while True:
        to_remove = []

        # Find all accessible rolls in this round
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    neighbor_count = 0

                    # Count nearby @ rolls
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "@":
                                neighbor_count += 1

                    # Accessible if fewer than 4 neighbors
                    if neighbor_count < 4:
                        to_remove.append((r, c))

        # Stop if no rolls can be removed
        if len(to_remove) == 0:
            break

        # Remove all rolls found in this round
        for r, c in to_remove:
            grid[r][c] = "."

        total_removed += len(to_remove)

    return total_removed


print(count_total_removed("2025/Day4/Day4.txt"))