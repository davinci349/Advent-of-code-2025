def solve_part2(filename):
    with open(filename, "r") as f:
        text = f.read().strip()

    ranges_part, ids_part = text.split("\n\n")

    ranges = []
    for line in ranges_part.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()

    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total = 0
    for start, end in merged:
        total += end - start + 1

    return total


print(solve_part2("2025/Day5/data5.txt"))