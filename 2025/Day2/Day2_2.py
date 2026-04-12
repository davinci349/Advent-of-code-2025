def is_invalid_id(n):
    s = str(n)
    length = len(s)

    for pattern_len in range(1, length):      
        if length % pattern_len != 0:         # to divide exactly without remainder
            continue                          # Once a continue statement is hit, the current iteration stops and goes back to the top of the loop.
            
        repeat_count = length // pattern_len  

        if repeat_count < 2:                  # It should be at least double.
            continue

        pattern = s[:pattern_len]

        if pattern * repeat_count == s:
            return True

    return False


with open("2025/Day2/data2.txt", "r") as f:
    data = f.read().strip()

total = 0

for part in data.split(","):
    start, end = map(int, part.split("-"))
    for n in range(start, end + 1):
        if is_invalid_id(n):
            total += n

print(total)