file = open("Task 8/data.txt", "a")

strings = ["Python", "Java", "C++", "JavaScript"]

for item in strings:
    file.write(item + "\n")

file.close()

print("Strings appended successfully.")
