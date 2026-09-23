# 1. Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


# 2. Access the third element in a tuple
print("Third element:", numbers[2])


# 3. Unpack a tuple into separate variables
a, b, c, d, e = numbers

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)


# 4. Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
print("Fruits:", fruits)


# 5. Add a new fruit to the set
fruits.add("Watermelon")
print("After adding fruit:", fruits)


# 6. Remove an element from a set
fruits.remove("Banana")
print("After removing fruit:", fruits)


# 7. Find union of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1.union(set2)
print("Union:", union)


# 8. Find intersection of two sets
intersection = set1.intersection(set2)
print("Intersection:", intersection)


# 9. Check if one set is a subset of another
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}

print("Is subset:", small_set.issubset(big_set))


# 10. Convert a list with duplicate values into a set
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = set(numbers)

print("Without duplicates:", unique_numbers)