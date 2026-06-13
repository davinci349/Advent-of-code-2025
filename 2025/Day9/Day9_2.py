def read_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            points.append((x, y))
    return points


def on_segment(px, py, ax, ay, bx, by):
    return (
        min(ax, bx) <= px <= max(ax, bx)
        and min(ay, by) <= py <= max(ay, by)
        and (bx - ax) * (py - ay) == (by - ay) * (px - ax)
    )


def inside_or_boundary(p, polygon):
    x, y = p
    inside = False
    n = len(polygon)

    for i in range(n):
        ax, ay = polygon[i]
        bx, by = polygon[(i + 1) % n]

        if on_segment(x, y, ax, ay, bx, by):
            return True

        if (ay > y) != (by > y):
            cross_x = ax + (y - ay) * (bx - ax) / (by - ay)
            if cross_x > x:
                inside = not inside

    return inside


def edge_crosses_rect_interior(edge, xmin, xmax, ymin, ymax):
    (x1, y1), (x2, y2) = edge

    # vertical edge
    if x1 == x2:
        x = x1
        if xmin < x < xmax:
            low = max(min(y1, y2), ymin)
            high = min(max(y1, y2), ymax)
            return low < high

    # horizontal edge
    if y1 == y2:
        y = y1
        if ymin < y < ymax:
            low = max(min(x1, x2), xmin)
            high = min(max(x1, x2), xmax)
            return low < high

    return False


def rectangle_valid(a, b, polygon, edges):
    x1, y1 = a
    x2, y2 = b

    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    corners = [
        (xmin, ymin),
        (xmin, ymax),
        (xmax, ymin),
        (xmax, ymax),
    ]

    for c in corners:
        if not inside_or_boundary(c, polygon):
            return False

    for edge in edges:
        if edge_crosses_rect_interior(edge, xmin, xmax, ymin, ymax):
            return False

    return True


def solve(filename):
    points = read_points(filename)

    edges = []
    n = len(points)
    for i in range(n):
        edges.append((points[i], points[(i + 1) % n]))

    best = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area <= best:
                continue

            if rectangle_valid(points[i], points[j], points, edges):
                best = area

    return best


print(solve("2025/Day9/data9.txt"))