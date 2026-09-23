try:
    file = open("Task 9 /data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")