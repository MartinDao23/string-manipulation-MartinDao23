# Your solution to Exercise 25
n = input("Enter windows path")
for char in n:
    if char == "\\":
        print("\n")
    else:
        print(char, end = "")
print("")