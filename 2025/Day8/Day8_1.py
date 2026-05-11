from itertools import combinations
from math import prod

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


def solve(filename):
    points = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(","))
                points.append((x, y, z))

    n = len(points)
    edges = []

    # Calculate distance between every pair of points
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        # Use squared distance, no need for sqrt
        dist2 = (
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )

        edges.append((dist2, i, j))

    # Sort by shortest distance
    edges.sort()

    dsu = DSU(n)

    # Connect the 1000 closest pairs
    for dist2, i, j in edges[:1000]:
        dsu.union(i, j)

    # Count circuit sizes
    circuit_sizes = {}

    for i in range(n):
        root = dsu.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    # Get three largest circuits
    largest_three = sorted(circuit_sizes.values(), reverse=True)[:3]

    return prod(largest_three)


print(solve("2025/Day8/data8.txt"))