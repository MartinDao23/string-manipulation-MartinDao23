# Your solution to Exercise 24
n = input("Enter a string")
lower_case = 0
upper_case = 0
for char in n:
    if char.isalpha():
        if ord(char) >= 97 and ord(char) <= 122:
            lower_case += 1
        elif ord(char) >= 65 and ord(char) <= 90:
            upper_case += 1
total_case = upper_case + lower_case
print((lower_case/total_case)*100)
print((upper_case/total_case)*100)