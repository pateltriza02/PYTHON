# 1. Create a list of 5 favorite movies
movies = ["Tare jami pe", "3 Idiots", "KGF", "Avatar", "KGF2"]
print("5 Favorite Movies:", movies)


# 2. Add a new movie to the list
movies.append("Pushpa")
print("After adding a movie:", movies)


# 3. Remove the first movie from the list
movies.pop(0)
print("After removing first movie:", movies)


# 4. Sort a list of numbers in ascending order
numbers = [50, 10, 30, 20, 40]
numbers.sort()
print("Ascending order:", numbers)


# 5. Reverse a list
numbers.reverse()
print("Reversed list:", numbers)


# 6. Find the largest number in a list
numbers = [10, 50, 20, 80, 30]
largest = max(numbers)
print("Largest number:", largest)


# 7. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print("Merged list:", merged_list)


# 8. Access the last element without using index number
numbers = [10, 20, 30, 40, 50]

last_element = numbers.pop()
print("Last element:", last_element)


# 9. Create a nested list and access a specific inner element
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Specific inner element:", nested_list[1][2])


# 10. Count how many times an element appears in a list
numbers = [10, 20, 10, 30, 10, 40]

count = numbers.count(10)
print("10 appears", count, "times")