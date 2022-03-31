#open a file and give an alias name
with open("harry.txt") as h:
  with open("john.txt") as j:
    h_lines = h.readlines()
    j_lines = j.readlines()
for i in range (len(j_lines)):
  print(f"\033[92mJohn: {j_lines[i]}",end = "")#no space between lines
  print(f"\033[93mHarry: {h_lines[i]}", end = "")#\033[93m is the colour of text

