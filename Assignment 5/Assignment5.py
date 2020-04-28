'''
Course: COSC 4320 01 System Modeling and Simulation
Assignment 5
Author: Nghia Dang
Date created: 04/27/2020
Python version: 2.7
'''

from pylab import *
import numpy as np

def initialize():
    global x, result
    x = 0.1
    result = [x]

def observe():
    global x, result
    result.append(x)

def update():
    global x, result
    x = r*x * (1 - x)

def plot_phase_space():
    initialize()
    for t in xrange(20):
        update()
        observe()
    plot(result)
    ylim(0, 2)
    title('r = ' + str(r))

rs = np.arange(0.5, 4, 0.5)
for i in xrange(len(rs)):
    subplot(3, 3, i + 1)
    r = rs[i]
    plot_phase_space()

show()

