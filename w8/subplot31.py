import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)
x = range(0, 10, 1)
y = range(0, 20, 2)

i = [1,2,3,4,5,6,7,8,9,10]
j = [t**2 for t in i]

axes[0,0].plot(x, y)
axes[1,1].plot(i, j)

plt.savefig("subplot31.png")
plt.show()