# Your solution to Exercise 15
n = input("Enter an arithmetic expression")
num1 = ""
num2 = ""
operator = ""
for char in n:
    if char.isdigit():
        num1 += char
    else:
        operator = char
        break
operator_position = n.find(operator)
for i in range (operator_position+1,len(n)):
    num2 += n[i]
if operator == "+":
    value = int(num1) + int(num2)
elif operator == "-":
    value = int(num1) - int(num2)
else:
    value = int(num1) * int(num2)
print(value)