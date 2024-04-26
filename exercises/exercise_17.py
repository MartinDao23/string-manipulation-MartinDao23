# Your solution to Exercise 17
n = input("Enter a phrase")
spaces = 1
for char in n:
    if char == " ":
        spaces += 1
print(spaces)