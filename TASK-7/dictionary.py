# 1. Create a dictionary storing student names and marks
students = {
    "Triza": 85,
    "Ronak": 78,
    "Priya": 92
}

print("Students:", students)


# 2. Add a new key-value pair to an existing dictionary
students["vyapti"] = 88

print("After adding:", students)


# 3. Delete a key-value pair from a dictionary
del students["Ronak"]

print("After deleting:", students)


# 4. Merge two dictionaries into one
dict1 = {
    "name": "Triza",
    "age": 20
}

dict2 = {
    "city": "valsad",
    "course": "BCA"
}

merged = dict1 | dict2

print("Merged dictionary:", merged)


# 5. Check if a key exists in a dictionary
if "name" in merged:
    print("Key 'name' exists")
else:
    print("Key 'name' does not exist")


# 6. Count word frequency in a given string using a dictionary
text = "apple banana apple mango banana apple"

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


# 7. Find the key with the maximum value in a dictionary
marks = {
    "Triza": 85,
    "Ronak": 78,
    "Priya": 92,
    "vyapti": 88
}

highest = max(marks, key=marks.get)

print("Highest marks:", highest)


# 8. Reverse keys and values in a dictionary
original = {
    "a": 1,
    "b": 2,
    "c": 3
}

reversed_dict = {value: key for key, value in original.items()}

print("Reversed dictionary:", reversed_dict)


# 9. Update the value for a specific key
marks["Triza"] = 95

print("Updated marks:", marks)


# 10. Convert a list of tuples into a dictionary
data = [
    ("name", "Triza"),
    ("age", 20),
    ("course", "BCA")
]

result = dict(data)

print("Dictionary:", result)