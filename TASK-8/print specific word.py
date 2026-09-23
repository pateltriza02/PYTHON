word = input("Enter the word to search: ")

file = open("Task 8/data.txt", "r")

for line in file:
    if word.lower() in line.lower():
        print(line, end="")

file.close()

