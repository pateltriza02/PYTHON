def palindrome(word):
 if word == word[::-1]:
   return "Palindrome"
 return "Not Palindrome"
print(palindrome("NAN"))