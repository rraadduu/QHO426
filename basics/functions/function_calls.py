def box(word):
  length = len(word)
  print("#"*(length+4))
  print(f"# {word} #")
  print("#"*(length+4))

def low(word):
  print(word.lower())

def up(word):
  print(word.upper())

w = "Harry Potter"
print(w[2:11:2]) # index start from 0:2:2 - start:finish:step
print(w[::-1]) # mirror counts from end

def mirror(word):
  print(f"{word} | {word[::-1]}") # print the word in mirror

mirror("bucharest")

def repeat(word):
  n = int(input("Enter number of times to repeat: "))
  for i in range(n): # alternate between upper and lower
    if i % 2 == 0:
      low(word)
    else:
      up(word)

def run():
  w = input("Enter a word: ")
  print("Choose one of the options:\n1-Box\n2-Lower case\n3-Lower case\n4-Mirror\n5-Repetition\n")
  opt = int(input())
  if opt == 1:
    box(w)
  elif opt == 2:
    low(w)
  elif opt == 3:
    up(w)
  elif opt == 4:
    mirror(w)
  elif opt == 5:
    repeat(w)
  else:
    print("No such option.")

run()