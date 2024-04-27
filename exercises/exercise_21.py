# Your solution to Exercise 21
n = input("Enter a date in the format mm/dd/yyyy")
month = n[0:2]
if month == "01":
    month = "January"
elif month == "02":   
    month = "February"
elif month == "03":
    month = "March"
elif month == "04":
    month = "April"
elif month == "05":
    month = "May"
elif month == "06":
    month = "June"
elif month == "07":
    month = "July"
elif month == "08":
    month = "August"
elif month == "09":
    month = "September"
elif month == "10":
    month = "October"
elif month == "11":
    month = "November"
else:
    month = "December"
print(f"{month}{n[3:5]},{n[6:10]}")