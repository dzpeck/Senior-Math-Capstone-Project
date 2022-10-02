from scipy import integrate as int
from mpl_toolkits import mplot3d
import math
import numpy as np
import matplotlib.pyplot as plt
plt.show()

def non_autonomous(t, x):

    """
    Given:
        t: the independent variable
       x, y: a point of interest in two dimensional space
       r, f, b, c1, beta, h, d, c2: parameters defining the system
    Returns:
       x_dot, y_dot: values of the system's partial
           derivatives at the point x, y
    """
    def deg(t):
        return math.radians(t)
    r = (3.8+0.1*math.sin(deg(t)))
    f = (2+0.1*math.sin(deg(t)))
    h = (0.05+0.01*math.sin(deg(t)))

    r = (0.8+0.1*math.sin(deg(t)))
    f = (5+0.5*math.sin(deg(t)))
    b = (0.22+0.1*math.sin(deg(t)))
    c1 = (0.6 + 0.1*math.sin(deg(t)))
    beta = (4+0.05*math.sin(deg(t)))
    d = (.06+.01*math.sin(deg(t)))
    h = (.02+.01*math.sin(deg(t)))
    c2 = (.6+.1*math.sin(deg(t)))
    x_dot = (((r * x[0]) / (1 + f * x[1])) - (b * x[0] ** 2) - ((c1 * x[0] * x[1]) / (1 + beta * x[0])))
    y_dot = (-(d * x[1]) - (h * x[1] ** 2) + ((c2 * x[0] * x[1]) / (1 + beta * x[0])))

    return [x_dot, y_dot]



# Set initial values
t0 = 0
tf = 2000
y0 = [.6, 0.8]
max_step = .01
s = 600

#Solve the system using above initial conditions and save the conditions to xs and ys.
#We also included smoother versions of the solution to make the graphs look nicer
sol = int.solve_ivp(non_autonomous,
                  (t0,tf),
                  y0,
                  max_step = max_step)
xs = sol.y[0, :]
#xs_smooth=[np.mean(xs[i-s: i+s]) for i in range(s,len(xs)-s)]
ys = sol.y[1, :]
#ys_smooth=[np.mean(ys[i-s: i+s]) for i in range(s,len(ys)-s)]

#This code plots the x and y coordinates of the solution separately against time
plt.figure(figsize=(12,6))

plt.plot(sol.t,xs,label = "Prey")
#plt.plot(sol.t[s: len(xs)-s],xs_smooth,label = "x_smooth")
plt.plot(sol.t,ys,label = "Predator")
#plt.plot(sol.t[s: len(ys)-s],ys_smooth,label = "y_smooth")
plt.xlim([0,100])
plt.legend()

plt.show()

#This code plots a phase plane showing the solution of the system
#using the initial conditions defined by t0 and y0
plt.figure(figsize=(12,12))

plt.title("Phase Plane")
plt.plot(xs,ys, linewidth = .5)
plt.xlabel("Prey")
plt.ylabel("Predator")

#This code plots The solutions against time
plt.show()
ax = plt.axes(projection='3d')
ax.plot3D(xs, ys, sol.t, lw=0.5)
ax.set_xlabel("Prey")
ax.set_ylabel("Predator")
ax.set_zlabel("Time")
ax.set_title("Populations Over Time")

plt.show()

