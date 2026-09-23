import csv

file = open("Task 8/data.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))

file.close()