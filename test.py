def solve(filename):
    with open(filename, "r") as f:
        text = f.read().strip()

    ranges_part, ids_part = text.split("\n\n")

    ranges = []
    for line in ranges_part.splitlines():                 # .splitlines() :text = "Hello\nWorld\nPython\n" print(text.splitlines()), the output would be ['Hello', 'World', 'Python'] ,it splits the string at line breaks like: \n (newline).
        start, end = map(int, line.split("-"))                
        ranges.append((start, end))

    ids = [int(line) for line in ids_part.splitlines()]

    count = 0

    for start, end in ranges:
        for ingredient_id in ids:        
            if start <= ingredient_id <= end:
                count += 1
                

    return count


print(solve("2025/Day5/data5.txt"))