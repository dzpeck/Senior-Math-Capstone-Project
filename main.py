# This is a model of a lotka-volterra system, a barebones predator prey model

from scipy import integrate as int
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
plt.show()

def predator_prey(t, x):
    a = 5.84
    b = 1
    c = 1
    d = 1.38
    """
    Given:
       x, y: a point of interest in three dimensional space
       a, b, c, d: parameters defining the Lotka-volterra system
    Returns:
       x_dot, y_dot: Values of the Lotka Volterra system's partial derivatives
    """


    x_dot = a*x[0]-b*x[0]*x[1]
    y_dot = c*x[0]*x[1]-d*x[1]

    return [x_dot, y_dot]


# Set initial values
t0 = 0
tf = 200
y0 = [2, 6]
max_step = .01

#Solve the system and save the solutions to xs and ys variables
sol = int.solve_ivp(predator_prey,
                  (t0,tf),
                  y0,
                  max_step = max_step)
xs = sol.y[0,:]
ys = sol.y[1,:]

#This is the code for the 2-d plot
plt.figure(figsize=(12,6))

plt.plot(sol.t,xs,label = "Prey Population")
plt.plot(sol.t,ys,label = "Predator Population")

plt.xlim([0,100])
plt.legend()



plt.show()

#This is the code for the 3-d plot
ax = plt.axes(projection='3d')
ax.plot3D(xs, ys, sol.t, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("time")
ax.set_title("Lotka Volterra System")

plt.show()