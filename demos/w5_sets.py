#Initialise empty set structure
s = set()
s1  ={"Garry", "Harry"}
#print(type(s1))
#Initialise non-empty set
colours = {"blue", "orange", "yellow", "purple", "black"}
print(colours)
#Add elements to set
colours.add("white")
colours.add("red")
colours.add("green")
print(colours)
colours.add("orange")#already exist and will not be printed twice
colours.add("black")#already exist and will not be printed twice
print(colours)
#Remove items from set
if "red" in colours:
  colours.remove("red")
if "yellow" in colours:
  colours.remove("yellow")
print(colours)
#Checking membership
col = input("Enter a colour: ")
if col in colours:
  print("Yay - my favourite colour!")
else:
  print("My colour is not there!")
x = {"cyan", "purple", "burgundi", "white", "green"}
#UNION - joining 2 sets together, not keeping duplicates
c2 = colours.union(x)
print(c2)
print(x)
print(colours)
#INTERSECTION - looking at common elements
c3 = colours.intersection(x)
print(c3)
#DIFFERENCE - keep only elements of one set, but NOT in the other
c4 = colours.difference(x)
c5 = x.difference(colours)
print(c4)
print(c5)