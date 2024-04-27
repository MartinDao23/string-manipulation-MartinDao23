# Your solution to Exercise 30
n = input("Enter the Roman Numerals")
n += "Z"
roman_numerals = {"I" : 1,
                 "V" : 5,
                 "X" : 10,
                 "L" : 50,
                 "C" : 100,
                 "D" : 500,
                 "M" : 1000,
                 "Z" : 0
}
value = 0
skip = False
for i in range(len(n)-1):
    if skip == True:
        skip = False
        continue
    if roman_numerals[n[i]] < roman_numerals[n[i+1]]:
        value += roman_numerals[n[i+1]]-roman_numerals[n[i]]
        skip = True
    else:
        value += roman_numerals[n[i]]
print(value)