def solve_part2(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # Normalize width
    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    total = 0
    c = 0

    while c < width:
        # Skip empty columns
        if all(line[c] == " " for line in lines):
            c += 1
            continue

        # Find a block (one problem)
        start = c
        while c < width and not all(line[c] == " " for line in lines):
            c += 1
        end = c

        block = [line[start:end] for line in lines]

        # Operator is last row
        op = block[-1].strip()

        # Build numbers column by column (RIGHT → LEFT)
        nums = []
        cols = len(block[0])

        for col in reversed(range(cols)):      # reversed(): Loop through the column numbers backward, ex:0, 1, 2, 3, 4 → 4, 3, 2, 1, 0.
            digits = []
            for row in range(len(block) - 1):  # skip operator row
                ch = block[row][col]
                if ch != " ":
                    digits.append(ch)

            if digits:
                # digits are top → bottom → need reverse
                num = int("".join(digits))     # join(): combines all items in the list into one string,then convert it into an integer.
                nums.append(num)

        # Compute result
        if op == "+":
            ans = sum(nums)
        elif op == "*":
            ans = 1
            for n in nums:
                ans *= n
        else:
            raise ValueError("Unknown operator")

        total += ans

    return total


print(solve_part2("2025/Day6/data6.txt"))