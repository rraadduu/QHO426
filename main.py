print("How many live cables must I avoid?")
n = input(int())
while n > 0:
  if n != 0:
    print(f"Avoiding {n} cables")
    n -= 1