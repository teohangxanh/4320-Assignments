# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:58:18 2020

@author: Damals
"""


from pylab import *

'''
thetadot = omega
omegadot = -g/L*sin(theta)
'''

g,L = 1,1
xvalues, yvalues = meshgrid(arange(-8, 8, 0.1), arange(-3, 3, 0.1))
xdot = yvalues
ydot = -g/L*sin(xvalues)
streamplot(xvalues, yvalues, xdot, ydot)
grid(); show()