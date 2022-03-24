#Instantiate empty dictionary
dicto = {} #created dictionary
print(type(dicto))
d = dict()
#Instantiate non-empty dictionary
phonebook = {"Thomas":"0770456789", "Aga":"0773123456", "Udoh":"0777563241"}
#Print full dictionary
print(phonebook)
#Print individual elements by index
print(f' Calling {phonebook["Udoh"]}')
#Zipping two lists together
names = ["Jagoda", "Frank", "Ludovico"]
ages = [19, 72, 33]
people = dict(zip(names, ages))
print(people)
#Traverse dictionary
for i in people:
  print(i)
for i in people.values():
  print(i)
for i,j in people.items():
  print(f"Person {i} is {j} years old.")