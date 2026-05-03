def solve(filename):
    with open(filename, "r") as f:
        text = f.read().strip()

    ranges_part, ids_part = text.split("\n\n")

    ranges = []
    for line in ranges_part.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ids = [int(line) for line in ids_part.splitlines()]

    count = 0

    for ingredient_id in ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                count += 1
                break

    return count


print(solve("2025/Day5/data5.txt"))