import matplotlib.pyplot as plt

labels = ('Jan', 'Feb', 'Mar', 'Apr', 'May')
sizes = [15, 30, 45, 90, 55]

plt.pie(sizes, labels=labels)#pie chart
plt.show()