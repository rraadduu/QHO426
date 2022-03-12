# ask user to provide dimensions
def dimensions():
  w = float(input("Enter the width: "))
  l = float(input("Enter the length: "))
  return w, l # returning a tuple

# calculate area
def calc_area(l, w):
  return w*l

# ask user to provide room name
def room_name():
  return input("Enter name of the room: ")

# calculate prices for each possibility
def price(name, area):
  if name.lower() == "bathroom":
    return 3*area
  elif name.lower() == "bedroom":
    return 2*area
  elif name.lower() == "kitchen":
    return 4*area
  elif name.lower() == "living room":
    return 2*area
  else:
    return 5*area

# 
def run():
  t_price = 0
  num = int(input("How many rooms to clean? ")) # room number to clean/ the program runs as many rooms to be cleaned
  for i in range(num):# for loop will run for num times
    name = room_name()
    x, y = dimensions()
    area = calc_area(x, y)
    t_price += price(name, area)

  print(f"Your total is £{t_price:.2f}")

run()
