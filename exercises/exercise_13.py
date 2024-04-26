# Your solution to Exercise 13
n = input("Enter a phrase  ")
digits = ""
for char in n:
    if char.isdigit():
        digits += char
print(digits)