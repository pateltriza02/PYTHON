file = open("Task 8/data.txt", "r")

text = file.read().lower()

words = text.split()

word_count = {}

for word in words:
    word = word.strip(".,!?")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()