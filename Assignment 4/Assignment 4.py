'''
Course: COSC 4320 01 System Modeling and Simulation
Assignment 4
Author: Nghia Dang
Date created: 04/16/2020
Python version: 2.7
'''

from pylab import *

# Problem 1
'''
thetadot = omega
omegadot = -g/L*sin(theta)
'''

g = 1
L = 1
xvalues, yvalues = meshgrid(arange(-8, 8, 0.1), arange(-3, 3, 0.1))
xdot = yvalues
ydot = -g/L*sin(xvalues)
streamplot(xvalues, yvalues, xdot, ydot, color='b', linewidth=2)
grid()
show()

#Problem 2
a = 1
b = 1
xvalues, yvalues = meshgrid(arange(-4.5, 4.5, 0.1), arange(-4.5, 4.5, 0.1))
xdot = -a*xvalues*yvalues
ydot = a*xvalues*yvalues - b*yvalues
streamplot(xvalues, yvalues, xdot, ydot, color='r', linewidth=2)
grid()
show()