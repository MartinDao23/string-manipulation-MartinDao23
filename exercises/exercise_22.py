# Your solution to Exercise 22
n = input("Enter anything")
n = n.replace(" ","")
palindrome = True
for i in range(len(n)):
    if n[i] != n[-1-i]:
        palindrome = False
print(palindrome)