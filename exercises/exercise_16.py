# Your solution to Exercise 16
n = input("Enter a character")
m = input("Enter a character")
for i in range (ord(n)+1,ord(m)):
    print(chr(i))