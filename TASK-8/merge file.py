file1 = open("Task 8/file1.txt", "r")
content1 = file1.read()
file1.close()

file2 = open("Task 8/file2.txt", "r")
content2 = file2.read()
file2.close()

file3 = open("Task 8/merged.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file3.close()

print("Files merged successfully.")
