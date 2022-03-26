#Once a set is created you can add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset.add("orange")#add element to your set
print(thisset)

#thisset.add("orange","aaa")#you cannot add 2 elements at a time
#you can add one set to another set
tropical = {"pineaple","mango","papaya"}
mylist = ["kiwi","orange"]
#add or update sets
thisset.update(tropical)

print(thisset)

thisset.remove("banana")#remove element from set
print(thisset)