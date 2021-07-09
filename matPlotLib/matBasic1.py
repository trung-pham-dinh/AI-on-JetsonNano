import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(-4,4,.1) # (-4, 4) each datapoint differs 0.1
x = np.linspace(-4,4,25) # [-4, 4] there are 25 datapoints

y = x*x
y2 = x**2 + 2
y3 = x**3 - 2

plt.grid(True) # background grid
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Basic graph')
#plt.axis([0,5, 0,11]) # range of axises
plt.plot(x,y,'b-*', linewidth = 3, markersize = 10, label = 'blue line')
plt.plot(x,y3,'r-*', linewidth = 3, markersize = 10, label = 'red line')
plt.legend(loc = 'upper center') # activate the label for lines
plt.show()