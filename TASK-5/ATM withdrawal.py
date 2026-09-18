balance = float(input("Enter your balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
    print("Remaining balance:", balance - amount)
else:
    print("Insufficient balance")