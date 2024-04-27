# Your solution to Exercise 14
n = input("Enter a phrase  ")
new_n = ""
for i in range(len(n)):
    if n[i] == " " and n[i+1] == " ":
        ""
    else:
        new_n += n[i]
new_n = new_n.strip()
print(new_n)