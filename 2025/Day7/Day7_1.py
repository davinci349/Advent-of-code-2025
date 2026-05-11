def solve(filename):
    with open(filename, "r") as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0])

    # Find S position
    start_col = grid[0].index("S")       # index(): is a method used to find the position of an element inside a string or list.

    # active beams: columns where beams are currently moving downward
    beams = {start_col}                  # A set is a collection of unique values, do not want duplicate values.

    split_count = 0

    # Start checking from row 1 because S is on row 0
    for r in range(1, rows):
        new_beams = set()               # set(): to create an empty set.

        for c in beams:
            if c < 0 or c >= cols:
                continue

            if grid[r][c] == "^":
                split_count += 1

                # Beam splits left and right
                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < cols:
                    new_beams.add(c + 1)
            else:
                # Beam continues downward
                new_beams.add(c)

        beams = new_beams

    return split_count


answer = solve("2025/Day7/data7.txt")
print(answer)