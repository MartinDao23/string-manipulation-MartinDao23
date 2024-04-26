# Your solution to Exercise 27
n = input("Enter a string")
former = n[0]
count = 0
output = n[0]
for char in n:
    if char == former:
        count += 1
    else:
        output += str(count) 
        output += char
        count = 1
        former = char
output += str(count) 
print(output)