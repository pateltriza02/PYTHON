old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

file = open("Task 8/data.txt", "r")

content = file.read()

file.close()

content = content.replace(old_word, new_word)

file = open("Task 8/data.txt", "w")

file.write(content)

file.close()

print("Word replaced successfully.")
