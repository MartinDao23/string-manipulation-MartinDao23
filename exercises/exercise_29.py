# Your solution to Exercise 29
shift = int(input("Number of places shifted "))
n = input("Enter a string ")
encrypted = ""
shift = shift%26
for char in n:   
    new_ascii = ord(char) + shift
    if char.isupper() and new_ascii > 90:
        new_ascii = (new_ascii-90)+64
    if char.islower() and new_ascii > 122:
        new_ascii = (new_ascii-122)+96
    encrypted += chr(new_ascii)
print(encrypted)