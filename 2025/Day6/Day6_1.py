def solve(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # Make all lines same width
    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    total = 0
    c = 0

    while c < width:
        # Skip empty space columns
        if all(line[c] == " " for line in lines):
            c += 1
            continue

        # Find one problem block
        start = c
        while c < width and not all(line[c] == " " for line in lines):
            c += 1
        end = c

        # Extract this block
        block = [line[start:end] for line in lines]

        # Last line contains operator
        op = block[-1].strip()

        # Other lines contain numbers
        nums = []
        for row in block[:-1]:
            s = row.strip()
            if s:
                nums.append(int(s))

        # Calculate answer
        if op == "+":
            ans = sum(nums)
        elif op == "*":
            ans = 1
            for n in nums:
                ans *= n
        else:
            raise ValueError("Unknown operator: " + op)

        total += ans

    return total


print(solve("2025/Day6/data6.txt"))