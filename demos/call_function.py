#defined a function - i specified what it is, what it does and what name is attached to it
# parameter - data given into the function
# default parameters - some data that would be used, if not given an argument
def calc_area(h = 4, b = 6):
  # h = float(input("Enter height: "))
  # b = float(input("Enter base: "))
  area = h*b*0.5
  # print(area)
  return area

calc_area(1.2, 4) # call function
calc_area(10, 9) # call function
calc_area(100) # call function
calc_area(b=20)
calc_area()
print(calc_area(100)) #example to print area
a1 = calc_area(2, 5) # example to print area