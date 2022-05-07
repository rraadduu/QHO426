import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  global ax #define variable as global so you can change it
  ax.plot(range(frame), range(frame))#create a line

some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

plt.show()