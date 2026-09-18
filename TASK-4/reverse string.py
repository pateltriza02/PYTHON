def reverse_string_loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
        
    return reversed_text
print(reverse_string_loop("TRIZA"))