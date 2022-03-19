def Average(list):
  return sum(list) / len(list)

#Driver code
list = [15, 9, 55, 41, 99, 29, 62, 49]
average = Average(list)

#Printing average to the list
print("Average=", round(average, 3)) # round for result and number for how many decimals after point