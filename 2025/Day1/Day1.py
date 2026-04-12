position = 50
count_zero = 0

with open("2025/Day1/data1.txt", "r") as f:  # "r" opens for reading only.
    for line in f:
        move = line.strip()  # In cases where you want to get rid of a certain character on the left and right side of
                             # a string, you would use the strip method. 
        if not move:         # This checks if move is empty or "False-like": ""(empty string),0,None.
            continue

        direction = move[0]
        distance= int(move[1:])

        if direction == "L":
            position = (position - distance) % 100 # % modulo operator, -5 % 3 = 1,and the difference between -6 and -5 is 1.

        elif direction == "R":
            position = (position + distance) % 100

        if position == 0:
            count_zero += 1

print(count_zero)






