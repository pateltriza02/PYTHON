file = open("Task 8/sentences.txt", "w")

for i in range(5):
    sentence = input("Enter sentence " + str(i + 1) + ": ")
    file.write(sentence + "\n")

file.close()
file =open("Task 8/data.txt", "r")
print("5 sentences written successfully.")