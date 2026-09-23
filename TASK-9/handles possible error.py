try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Error: Invalid input. Enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program completed.")