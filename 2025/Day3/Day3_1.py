def max_joltage(line):
    digits = list(map(int, line.strip()))

    max_left = -1      # best first digit seen so far
    max_value = 0

    for d in digits:
        if max_left != -1:
            max_value = max(max_value, max_left * 10 + d)

        max_left = max(max_left, d)

    return max_value


def total_joltage(filename):
    total = 0

    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                total += max_joltage(line)

    return total


# Run
print(total_joltage("input.txt"))