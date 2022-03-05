n = int(input("Please enter a number: "))
while n > 0:
  if n % 2 == 0:
    # % check odd and even numbers
    print(n, "is a even number")
  else:
    print(n ,"is a odd number")
  # descrease number by 1 in each iteration
  n = n - 1