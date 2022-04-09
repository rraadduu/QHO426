import matplotlib.pyplot as plt#always import first

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")#name on graph on x axis
plt.ylabel("y values")#name on graph on y axis

plt.plot(x, y)#plot indicate x and y
plt.plot(x, y, "o")
plt.step(x, y)
plt.bar(x, y)
plt.savefig('combined.png')#save figure and give name plus extension: png, jpeg, pdf
plt.show()#always show function