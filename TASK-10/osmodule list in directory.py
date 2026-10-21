import os

path = "."

files = os.listdir(path)

print("Files and folders in the directory:")

for file in files:
    print(file)
