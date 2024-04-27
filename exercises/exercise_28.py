# Your solution to Exercise 28
n = input("Enter a string")
words = 0
for i in range (len(n)-1):
    if n[i].isalpha() and n[i+1].isalpha() == False:
        words += 1
print(words)