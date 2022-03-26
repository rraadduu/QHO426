set1 = {"abc",34,True,48,"male"}
set2 = {"abc",34,True,48,"male","male",34,True}
set3 = {("abc",34,True,48,"male","male",34,True)}
set4 = set(("abc",34,True,48,"male","male",34,True))#normal definition for set

print(len(set1))
print(len(set2))
print(len(set3))
print(len(set4))