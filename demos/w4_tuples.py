# declare a tuple
p = ("Radu", 88, False)
y = tuple([3, 6, 9])
# print tuples
print(p)
print(y)
# print single elements
print(p[1])
# print multipl,ying 2 numbers
print(y[0]*y[2])
# cannot change values in a tuple => immutable
# y[1] = 7778
# cannot use .append
# y.append(8)

# Creating a new tuple and add it at the top of another tuple
z = p + y
print(z)
# using minimum or maximum functions
print(min(y)) # min value of tuple y
print(max(y)) # max value of tuple y
