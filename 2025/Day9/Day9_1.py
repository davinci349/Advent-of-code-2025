def solve(filename):
    points = []

    with open(filename, "r") as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))

    best = 0

    for i in range(len(points)):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height

            best = max(best, area)

    return best


print(solve("2025/Day9/data9.txt"))