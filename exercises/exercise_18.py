# Your solution to Exercise 18
n = input("Enter a number")
product = 1
for char in n:
    product *= int(char)
print(product)