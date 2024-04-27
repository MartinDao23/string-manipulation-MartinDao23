# Your solution to Exercise 6
n = input("Enter")
if n.isalpha():
    print("Your message includes letters only")
elif n.isdigit():
    print("Your message includes only numbers")
else:
    print("Your message includes numbers and letters")