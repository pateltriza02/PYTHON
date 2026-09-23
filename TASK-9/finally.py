file = None

try:
    file = open("Task 9/data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    if file:
        file.close()
        print("File closed.")