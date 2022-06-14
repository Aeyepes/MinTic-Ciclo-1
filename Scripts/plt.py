import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline
x1 = np.linspace(0,10,100)

fig = plt.figure()

plt.plot(x1, np.sin(x1), '-')
plt.plot(x1, np.cos(x1), '-')

plt.show()

plt.subplot(2,2,1)
plt.plot(x1, np.sin(x1))

plt.show()

plt.plot([1, 2, 3, 4])
plt.ylabel('Numbers')
plt.xlabel('eje x')
plt.show()