def hobbies():
  print("Enter your hobbies one after another, until you enter \"stop\"")
  s = set()
  while True:
    hobby = input()
    if hobby.lower() == "stop":
      break
    else:
      s.add(hobby)
  return s

def tinderDaSecond():
  print("First person: ")
  p1 = hobbies()
  print("Second person: ")
  p2 = hobbies()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"Yay - you are a match mate in heaven! You have {len(common)} common interests.")
  else:
    print(f"Well, I doubdt it would work :(. You have only {len(common)} hobbies in common.")

tinderDaSecond()