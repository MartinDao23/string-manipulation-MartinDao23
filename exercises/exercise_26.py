# Your solution to Exercise 26
a = int(input("Enter a range"))
b = int(input("Enter a range"))
c = int(input("Enter a range"))
d = int(input("Enter a range"))
for i in range (c,d+1):
    print("  ", i, end = "")
print()
for rows in range (a,b+1):
    print(rows, end = "")
    for x in range (c,d+1):
        print("  ", rows*x,end = "")
    print()