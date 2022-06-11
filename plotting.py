import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['science', 'notebook', 'grid'])

x = np.linspace(0,15,30)
y = np.sin(x) + 0.1*np.random.rand(len(x))

plt.figure(figsize=(10,3)) # Aspect ratio of the plot
plt.plot(x, y, '--o', color='red', lw=0.8, ms=1.8) # '--', '-o', '--o', 'o', Line Weight, Marker Size
plt.xlabel('Time [s]') # Labels
plt.ylabel('Voltage [V]')
plt.show()

# Following this tutorial: https://youtu.be/cTJBJH8hacc
# Necesarry installations
#pip install numpy
#pip install matplotlib
#pip install SciencePlots