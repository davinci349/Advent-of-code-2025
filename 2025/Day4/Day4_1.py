def count_accessible_rolls(filename):
    with open(filename, "r") as f:
        grid = [line.strip() for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                neighbor_count = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            neighbor_count += 1

                if neighbor_count < 4:
                    accessible += 1

    return accessible


print(count_accessible_rolls("2025/Day4/data4.txt"))