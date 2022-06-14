import numpy as np
import matplotlib.pyplot as plt
import math 

# x = np.linspace(0, 5, 10, True)
# y = np.linspace(0, 10, 10)

# plt.plot(x, y, 'purple')
# plt.plot(x, y, 'o')

x = np.arange(0, 12 * np.pi, 0.01)
y = np.cos(x)
z = np.sin(x)
#t = np.tan(x)

plt.plot(x, y, 'orange')
plt.plot(x, z, 'blue')
#plt.plot(x, t, 'red')

plt.show()