# Monotonic Stack approach to find the maximum 12-digit number that can be formed by deleting some digits from the input line while maintaining the order of the remaining digits.

def max_joltage_12(line: str) -> int:
    digits = line.strip()
    k = 12

    # If the line has exactly 12 digits, just use it directly
    if len(digits) == k:
        return int(digits)

    stack = []
    to_remove = len(digits) - k   # how many digits we are allowed to delete

    for d in digits:
        # Remove smaller previous digits if current digit is bigger
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If we still have digits to remove, remove from the end
    if to_remove > 0:
        stack = stack[:-to_remove]

    # Keep exactly the first 12 digits
    result = "".join(stack[:k])
    return int(result)


def total_joltage_12(filename: str) -> int:
    total = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:   # skip empty lines
                total += max_joltage_12(line)

    return total


# Run
answer = total_joltage_12("2025/Day3/data3.txt")
print("Total output joltage:", answer)