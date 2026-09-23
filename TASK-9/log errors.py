import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR
)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except Exception as e:
    logging.error("Error occurred: %s", e)
    print("An error occurred. Check error.log")