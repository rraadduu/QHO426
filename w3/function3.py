def rectangle(width, height):
  area = width * height
  perimeter = 2 * (width + height)
  print("\nArea is: %.2f" %area)
  print("\nPerimeter is: %.2f" %perimeter)

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

rectangle(width, height) # always call the function otherwise it will not work
rectangle(3, 4) # example with variables given