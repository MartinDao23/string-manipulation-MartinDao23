# Your solution to Exercise 19
n = input("Enter a number")
for i in range(len(n)):
    if n[i] == ".":
        print(n[i+1])