def is_invalid_id(n):
    s = str(n)
    
    if len(s) % 2 != 0:
        return False
    
    half = len(s) // 2 
    return s[:half] == s[half:]

total = 0

with open("2025/Day2/data2.txt", "r") as f :
    data = f.read().strip()
    
    for part in data.split(","):
        start, end = map(int, part.split("-"))
        for n in range(start, end+1):
           if is_invalid_id(n):
               total += n
            
print(total)
