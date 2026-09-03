num = int(input("Enter the number:"))
reverse = 0
  
for i in range (len(str(num))):
  digit = num % 10
  reverse = reverse * 10 + digit
  num = num // 10
print(reverse)    