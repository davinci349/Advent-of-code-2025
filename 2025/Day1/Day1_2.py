position = 50
count_zero = 0

with open("2025/Day1/data1.txt", "r") as f:
    for line in f:
        move = line.strip()
        if not move:
            continue

        direction = move[0]
        d = int(move[1:])

        if direction == "R":
            count_zero += (position + d) // 100
            position = (position + d) % 100

        else:  # L                    
            if position == 0:
                count_zero += d // 100
            elif d >= position:
                count_zero += 1 + (d - position) // 100    # An offset of 1 is added because (d - position) crosses zero exactly once.

            position = (position - d) % 100

print(count_zero)