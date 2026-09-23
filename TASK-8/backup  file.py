source = open("Task 8/data.txt", "r")

content = source.read()

source.close()

backup = open("Task 8/backup.txt", "w")

backup.write(content)

backup.close()

print("Backup created successfully.")