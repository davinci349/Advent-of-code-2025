import csv

with open("test.csv", "w", newline="") as f:    # newline="" means that Do NOT automatically add extra newline characters (\n)
    writer = csv.writer(f, delimiter= ",")      # delimiter= "," means that Join values with a comma when writing to the file
    writer.writerow(["Craig Lou", "Taiwan"])
    writer.writerow(["Name", "City"])
  

with open("test.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")      # delimiter= "," means that split each line wherever you see a comma
    for row in reader:
        print(row)
    


