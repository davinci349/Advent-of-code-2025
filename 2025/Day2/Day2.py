def is_invalid_id(n):
    s = str(n)
    
                                  # Must have even number of digits    
    if len(s) % 2 != 0:           # True division (/) converts numbers to floats before dividing. Ex: 7 / 4 becomes 7.0 / 4.0, resulting in 1.75.
        return False          

    
    half = len(s) // 2            # Floor division (//) computes the quotient, or the number of times divided. Ex: 7 // 4 is 1 because 4 goes
    return s[:half] == s[half:]   # into 7 one time, remainder 3.
    


data = """269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"""

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