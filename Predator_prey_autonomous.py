from scipy import integrate as int
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
plt.show()

def predator_prey(t, x, r=2, f=.04, b=0.5, c1=0.6, beta=2, h=0.02, d=.03, c2=0.4):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the Autonomous system's partial
           derivatives at the point x, y, z
    """


    x_dot = ((r*x[0])/(1+f*x[1])-b*x[0]**2-(c1*x[0]*x[1])/(1+beta*x[0]))
    y_dot = (-d*x[1]-h*x[1]**2+(c2*x[0]*x[1])/(1+beta*x[0]))

    return [x_dot, y_dot]

# Set initial values
t0 = 0
tf = 200
y0 = [2, 6]
max_step = .01


sol = int.solve_ivp(predator_prey,
                  (t0,tf),
                  y0, max_step = max_step)
xs = sol.y[0]
ys = sol.y[1]


plt.figure(figsize=(12,6))

plt.plot(sol.t,xs,label = "Prey Population")
plt.plot(sol.t,ys,label = "Predator Population")

plt.xlim([0,200])
plt.legend()
plt.show()

