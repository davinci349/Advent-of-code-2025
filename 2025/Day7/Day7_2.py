from collections import Counter

def solve(filename):
    with open(filename, "r") as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = max(len(line) for line in grid)

    grid = [line.ljust(cols) for line in grid]

    start_col = grid[0].index("S")

    timelines = Counter()
    timelines[start_col] = 1

    for r in range(1, rows):
        new_timelines = Counter()

        for c, count in timelines.items():
            if grid[r][c] == "^":
                new_timelines[c - 1] += count
                new_timelines[c + 1] += count
            else:
                new_timelines[c] += count

        timelines = new_timelines

    return sum(timelines.values())


print(solve("2025/Day7/data7.txt"))