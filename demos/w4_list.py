# declare an empty list
bleh = []
meh = list()
# declare non empty list
yummy = ["Pizza", "Lasagna", "Spaghetti Bolognese"]
# print entire list
print(yummy)
# print single item using index
print(yummy[2])  # second item of list
# printing some elements
print(yummy[:2]) # from begining up to first element as number 2 is not included
# add elements to our list (expand it) - adding elements at the end of the list
print(bleh)
bleh.append("Fish")
bleh.append("Coconut")
bleh.append("Onion")
bleh.append("Chocolate")
print(bleh) # print new list
# add multiple items to the list based on user input
n = int(input("How many items to add?"))
for i in range (n):
  yummy.append(input("Enter a new yummy food: "))
print(yummy)
# adding data at any point inside the list
print(bleh)
bleh.insert(1,"Mashed Potatoes") # position 1 will be occupied bi Mashed Potatoes
print(bleh)
bleh.insert(3, "Cabage")
print(bleh)
# remove an item from list
if "Frankfurters" in bleh: # check if the item is inside the list with if statement
  bleh.remove("Frankfurters")
if "Coconut" in bleh:
  bleh.remove("Coconut")
print(bleh)
# remove item via index
x = bleh.pop(2) # remove the word indexed 2 and preserve it in x variable
print(bleh)
print(x)
# alternative way of deleting via index
del bleh[1] # cannot preserve it in a variable
print(bleh)
# extending a list / add one list at the end of another list
print(yummy)
yummy.extend(["Fish", "Bacon", "Ketchup"])
print(yummy)
# checking for particular data type within a list
lista = ["Fred", True, 6, 8, -7.88, False, "Lalala", 55]
# using for loop to acces item one at the time
for item in lista:
  if isinstance(item, str): # check if there are any string
    print(item)