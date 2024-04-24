# Your solution to Exercise 9
n = input("Enter a phrase")
if len(n) == 1:
    print(n)
elif len(n) == 2:
    print(n[::-1])
else:
    print(n[-1] + n[1:len(n)] + n[0])