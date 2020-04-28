'''
Course: COSC 4320 01 System Modeling and Simulation
Bonus assignment
Author: Nghia Dang
Date created: 04/27/2020
Python version: 2.7
'''
K = 1
Dt = 1.5

from pylab import *

def initialize():
    global x, result, t, timesteps
    x = 0.1
    result = [x]
    t = 0.
    timesteps = [t]
    
def observe():
    global x, result, t, timesteps
    result.append(x)
    timesteps.append(t)
    
def update():
    global x, result, t, timesteps
    x = x + r * x * (1 - x / K) * Dt
    t = t + Dt

def plot_phase_space():
    initialize()
    for t in xrange(30):
        update()
        observe()
    plot(result)
    ylim(0, 2)
    title('r = ' + str(r))

rs = [0.1, 0.5, 1.0, 1.1, 1.5, 1.6]
for i in xrange(len(rs)):
    subplot(2, 3, i + 1)
    r = rs[i]
    plot_phase_space()

show()