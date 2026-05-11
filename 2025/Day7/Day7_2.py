from collections import Counter

def solve(filename):
    with open(filename, "r") as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = max(len(line) for line in grid)


    grid = [line.ljust(cols) for line in grid]

    start_col = grid[0].index("S")

    timelines = Counter()          # Counter(): is a special Python tool used for counting things automatically, it is similar to a dictionary, but designed for counting.
    timelines[start_col] = 1       # Store the value 1 at key start_col inside timelines.

    for r in range(1, rows):
        new_timelines = Counter()

        for c, count in timelines.items():     # 1 Loop through every key-value pair inside timelines. 2.item(): returns (key, value) pairs from a dictionary or Counter.
            if grid[r][c] == "^":
                new_timelines[c - 1] += count
                new_timelines[c + 1] += count
            else:
                new_timelines[c] += count

        timelines = new_timelines

    return sum(timelines.values())       # Add together all the values inside timelines, then return the total.


print(solve("2025/Day7/data7.txt"))