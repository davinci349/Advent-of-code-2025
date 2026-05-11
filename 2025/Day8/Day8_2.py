from itertools import combinations

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1

        return True


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

    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        dist2 = (
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )

        edges.append((dist2, i, j))

    edges.sort()

    dsu = DSU(n)

    for dist2, i, j in edges:
        if dsu.union(i, j):
            if dsu.components == 1:
                return points[i][0] * points[j][0]


print(solve("2025/Day8/data8.txt"))