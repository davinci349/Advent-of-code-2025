def is_invalid_id(n):
    s = str(n)
    
                                  # Must have even number of digits    
    if len(s) % 2 != 0:           # True division (/) converts numbers to floats before dividing. Ex: 7 / 4 becomes 7.0 / 4.0, resulting in 1.75.
        return False          

    
    half = len(s) // 2            # Floor division (//) computes the quotient, or the number of times divided. Ex: 7 // 4 is 1 because 4 goes
    return s[:half] == s[half:]   # into 7 one time, remainder 3.
    
    

with open("2025/Day2/data.txt", "r") as f:
    data = f.read().strip()
       
total = 0

for part in data.split(","):
    start, end = map(int, part.split("-"))  # When map is called, the function begins to iterate over the the temps list passed in. As it iterates, it passed a single
                                            # item into the convertDeg function until it passes all items in. The equivalent of the process is the following:
                                            # for item in temps:
                                            #       convertDeg(item)
    for n in range(start, end + 1):
        if is_invalid_id(n):
            total += n

print(total)



