import matplotlib.pyplot as plt

def small():
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')#r=red, :=doted line, o=corner dots
  
def medium():
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]
  plt.plot(x, y, 'g--s')#g=green, --=two dash lines
  
def large():
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]
  plt.plot(x, y, 'b-p')#b=blue, -=one line, p=penthagon
  
def run():
  small()
  medium()
  large()
  plt.show()
  
run()