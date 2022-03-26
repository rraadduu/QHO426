thisset = {"abc",34,False,"True",40,"male"}

for x in thisset:
  print(x)
#the next prints will check through the list if the elements exist an will print True or False
print("abc" in thisset)#print True in console because it exist in set
print("banana" in thisset)#print False because it does not exist in set
print(False in thisset)#print True in console because it exist in set
print(True in thisset)#print False because it does not exist in set
print("True" in thisset)