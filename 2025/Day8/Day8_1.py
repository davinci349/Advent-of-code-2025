from itertools import combinations
from math import prod

class DSU:     # Disjoint Set Union (DSU) or Union-Find data structure is a powerful tool for managing and merging disjoint sets. It provides efficient operations for finding the representative of a set and merging two sets together.
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
    for i, j in combinations(range(n), 2):              # The combinations function takes a group of items and a size (in this case, 2). It generates every possible unique pair.
        x1, y1, z1 = points[i]                          # Key Feature: Order does not matter. If it gives you (0, 1), it will not give you (1, 0) because that's the same pair. It also won't give you (0, 0) because you need two distinct items.
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

    dsu = DSU(n)   # Disjoint Set Union (DSU) or Union-Find data structure is a powerful tool for managing and merging disjoint sets. It provides efficient operations for finding the representative of a set and merging two sets together.

    # Connect the 1000 closest pairs
    for dist2, i, j in edges[:1000]:
        dsu.union(i, j)

    # Count circuit sizes
    circuit_sizes = {}

    for i in range(n):
        root = dsu.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1          #  dictionary.get(key, default_value) if key doesn't exist in the dictionary, it returns default_value instead of raising a KeyError. In this case, if root is not already a key in circuit_sizes, it will return 0, allowing us to start counting from 1 for that root.

    # Get three largest circuits
    largest_three = sorted(circuit_sizes.values(), reverse=True)[:3]

    return prod(largest_three)


print(solve("2025/Day8/data8.txt"))