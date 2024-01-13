import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111, projection='3d')
theta = np.arange(0,2*np.pi,0.01)
a = 5
z = np.arange(0,100,10)
Theta, z_ = np.meshgrid(theta,z)
# x, y en polares
x = a * np.cos(Theta)
y = a * np.sin(Theta)
ax.plot_surface(x,y,z_,color='Pink')
def plano(a):
    t = np.linspace(0,2*np.pi,100)
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = 4 - (a/2)*(np.cos(t)+np.sin(t))
    ax.plot(x,y,z)
plano(5)
plt.show()
