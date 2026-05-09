def solve(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # Make all lines same width
    width = max(len(line) for line in lines)
    # lines = [line.ljust(width) for line in lines]    # .ljust():It pads spaces (or another character) to the right side of the string so the total length becomes a specified width.

    total = 0
    c = 0

    while c < width:
        # Skip empty space columns
        if all(line[c] == " " for line in lines):    # .all(): It checks a collection (like a list, tuple, or generator) and only returns True if every single element in that collection evaluates to True.
            c += 1
            continue                                 # continue: Skip the rest of this loop iteration and go to the next loop round immediately.

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
                                  # sometimes lines may be blank,that is False So Python skips it.
            nums.append(int(s))

        # Calculate answer
        if op == "+":
            ans = sum(nums)
        elif op == "*":
            ans = 1
            for n in nums:
                ans *= n
        

        total += ans

    return total


print(solve("2025/Day6/data6.txt"))