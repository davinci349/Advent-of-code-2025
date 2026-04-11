import csv

with open("test.csv", "w", newline="") as f:    # newline="" means that Do NOT automatically add extra newline characters (\n)
    writer = csv.writer(f, delimiter= ",")      # delimiter= "," means that Join values with a comma when writing to the file
    writer.writerow(["Craig Lou", "Taiwan"])

  

with open("test.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")      # delimiter= "," means that split each line wherever you see a comma
    writer.writerow(["Name", "City"])
    for row in reader:
        print(row)