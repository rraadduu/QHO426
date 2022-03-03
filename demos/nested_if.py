salary = float(input("What is your salary? \n"))
years = int(input("How long have you worked here? \n"))

if years > 2:
  if salary < 25000:
    salary = salary*1.1 # 10% + 100% = 110% = 110/100 = 1.1
    print(f"Your new salary will be £{salary:.2f}")
  else:
    salary = salary + 100
    print(f"Small change. Now you get £{salary:.2f} ")
elif years >= 1:
  print("No salary increase for you. Sorry :(")
else:
  if salary < 15000:
    print("Ooopsie, it's an error. You will earn £20000")
    salary = 20000
print("Lets work hard!")