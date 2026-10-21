#        PYTHON QUIZ GAME
# ==========================================

print("=" * 45)
print("         WELCOME TO QUIZ MASTER ")
print("=" * 45)

name = input("\nEnter your name: ")

print("\nHello", name, "!")
print("Welcome to the Quiz Master Game!")
print("-" * 45)

print("\n GAME RULES")
print("1. There are 15 questions.")
print("2. Each correct answer gives you 10 points.")
print("3. You have 3 lives.")
print("4. A wrong answer removes 1 life.")
print("5. The game ends if you lose all 3 lives.")

input("\nPress ENTER to start the quiz...")

score = 0
lives = 3
correct = 0
wrong = 0


# ==========================================
# QUESTION 1 - EASY
# ==========================================

print("\n" + "=" * 45)
print(" EASY LEVEL")
print("=" * 45)

print("\nQuestion 1:")
print("What is the capital of India?")
print("A. Mumbai")
print("B. New Delhi")
print("C. Ahmedabad")
print("D. Jaipur")

answer = input("Your answer: ").upper()

if answer == "B":
    print(" Correct!")
    score += 10
    correct += 1
else:
    print(" Wrong! Correct answer: B. New Delhi")
    lives -= 1
    wrong += 1

print("Score:", score, "|  Lives:", lives)


# ==========================================
# QUESTION 2
# ==========================================

print("\nQuestion 2:")
print("Which planet is known as the Red Planet?")
print("A. Earth")
print("B. Jupiter")
print("C. Mars")
print("D. Venus")

answer = input("Your answer: ").upper()

if answer == "C":
    print(" Correct!")
    score += 10
    correct += 1
else:
    print(" Wrong! Correct answer: C. Mars")
    lives -= 1
    wrong += 1

print("Score:", score, "|  Lives:", lives)


# ==========================================
# QUESTION 3
# ==========================================

print("\nQuestion 3:")
print("How many days are there in a week?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")

answer = input("Your answer: ").upper()

if answer == "C":
    print(" Correct!")
    score += 10
    correct += 1
else:
    print(" Wrong! Correct answer: C. 7")
    lives -= 1
    wrong += 1

print("Score:", score, "|  Lives:", lives)


# ==========================================
# QUESTION 4
# ==========================================

print("\nQuestion 4:")
print("Which animal is called the King of the Jungle?")
print("A. Tiger")
print("B. Lion")
print("C. Elephant")
print("D. Leopard")

answer = input("Your answer: ").upper()

if answer == "B":
    print(" Correct!")
    score += 10
    correct += 1
else:
    print(" Wrong! Correct answer: B. Lion")
    lives -= 1
    wrong += 1

print("Score:", score, "|  Lives:", lives)


# ==========================================
# QUESTION 5
# ==========================================

print("\nQuestion 5:")
print("What is 12 × 5?")
print("A. 50")
print("B. 55")
print("C. 60")
print("D. 65")

answer = input("Your answer: ").upper()

if answer == "C":
    print(" Correct!")
    score += 10
    correct += 1
else:
    print(" Wrong! Correct answer: C. 60")
    lives -= 1
    wrong += 1

print("Score:", score, "|  Lives:", lives)


# Check lives
if lives <= 0:
    print("\n GAME OVER!")
    print("You lost all your lives.")

else:

    # ==========================================
    # MEDIUM LEVEL
    # ==========================================

    print("\n" + "=" * 45)
    print(" MEDIUM LEVEL - COMPUTER & PYTHON")
    print("=" * 45)

    print("\nQuestion 6:")
    print("Who created Python?")
    print("A. James Gosling")
    print("B. Guido van Rossum")
    print("C. Dennis Ritchie")
    print("D. Elon Musk")

    answer = input("Your answer: ").upper()

    if answer == "B":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: B. Guido van Rossum")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


    # Question 7

    print("\nQuestion 7:")
    print("Which function displays output in Python?")
    print("A. display()")
    print("B. show()")
    print("C. print()")
    print("D. output()")

    answer = input("Your answer: ").upper()

    if answer == "C":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: C. print()")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


    # Question 8

    print("\nQuestion 8:")
    print("Which symbol starts a comment in Python?")
    print("A. //")
    print("B. #")
    print("C. /*")
    print("D. @")

    answer = input("Your answer: ").upper()

    if answer == "B":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: B. #")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


    # Question 9

    print("\nQuestion 9:")
    print("Which data type stores True or False?")
    print("A. int")
    print("B. str")
    print("C. bool")
    print("D. float")

    answer = input("Your answer: ").upper()

    if answer == "C":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: C. bool")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


    # Question 10

    print("\nQuestion 10:")
    print("Which keyword is used to create a function?")
    print("A. function")
    print("B. create")
    print("C. def")
    print("D. fun")

    answer = input("Your answer: ").upper()

    if answer == "C":
        print("Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: C. def")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


# ==========================================
# HARD LEVEL
# ==========================================

if lives > 0:

    print("\n" + "=" * 45)
    print(" HARD LEVEL")
    print("=" * 45)

    # Question 11

    print("\nQuestion 11:")
    print("What is the output of: print(2 ** 3)?")
    print("A. 5")
    print("B. 6")
    print("C. 8")
    print("D. 9")

    answer = input("Your answer: ").upper()

    if answer == "C":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: C. 8")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


# Question 12

if lives > 0:

    print("\nQuestion 12:")
    print("What does len('Python') return?")
    print("A. 5")
    print("B. 6")
    print("C. 7")
    print("D. Python")

    answer = input("Your answer: ").upper()

    if answer == "B":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: B. 6")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


# Question 13

if lives > 0:

    print("\nQuestion 13:")
    print("Which operator checks if two values are equal?")
    print("A. =")
    print("B. ==")
    print("C. !=")
    print("D. >")

    answer = input("Your answer: ").upper()

    if answer == "B":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: B. ==")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


# Question 14

if lives > 0:

    print("\nQuestion 14:")
    print("Which Python collection stores key-value pairs?")
    print("A. List")
    print("B. Tuple")
    print("C. Dictionary")
    print("D. String")

    answer = input("Your answer: ").upper()

    if answer == "C":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: C. Dictionary")
        lives -= 1
        wrong += 1

    print("Score:", score, "|  Lives:", lives)


# Question 15

if lives > 0:

    print("\n FINAL QUESTION ")
    print("What is the output of: 10 // 3 ?")
    print("A. 3")
    print("B. 3.33")
    print("C. 1")
    print("D. 4")

    answer = input("Your answer: ").upper()

    if answer == "A":
        print(" Correct!")
        score += 10
        correct += 1
    else:
        print(" Wrong! Correct answer: A. 3")
        lives -= 1
        wrong += 1


# ==========================================
# FINAL RESULT
# ==========================================

print("\n" + "=" * 45)
print("             FINAL RESULT ")
print("=" * 45)

print("\nPlayer:", name)
print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Final Score:", score)
print("Lives Remaining:", lives)

questions_answered = correct + wrong

if questions_answered > 0:
    percentage = (correct / questions_answered) * 100
else:
    percentage = 0

print("Accuracy:", round(percentage, 2), "%")


# ==========================================
# PLAYER RANK
# ==========================================

print("\nYour Rank:")

if score >= 130:
    print(" QUIZ MASTER!")
elif score >= 100:
    print(" Excellent Player!")
elif score >= 70:
    print(" Good Player!")
elif score >= 40:
    print(" Nice Try!")
else:
    print(" Beginner - Keep Practicing!")


# ==========================================
# END
# ==========================================

if lives <= 0:
    print("\n You lost all your lives!")
else:
    print("\n Congratulations! You completed the quiz!")

print("\nThank you for playing,", name, "!")

