import matplotlib.pyplot as plt
import numpy as np

a = 1.1
r = 2.8

def initialize():
    global x, result
    x = 1.
    result = [x]

def observe():
    global x, result
    result.append(x)

def f(x): ### iterative map is now defined as f(x)
    return r * x * (1 - x) 

def update():
    global x, result
    x = f(x)

initialize()
for t in range(30):
    update()
    observe()

### drawing diagonal line
xmin, xmax = 0, 20
plt.plot([xmin, xmax], [xmin, xmax], 'k')

### drawing curve
rng = np.arange(xmin, xmax, (xmax - xmin) / 100.)
# plot(rng, map(f, rng), 'k')
plt.plot(rng, rng, 'b')
plt.plot(rng, f(rng), 'r')


### drawing trajectory
horizontal = [result[0]]
vertical = [result[0]] 
for x in result[1:]:
    horizontal.append(vertical[-1])
    vertical.append(x)
    horizontal.append(x)
    vertical.append(x)    
plt.plot(horizontal, vertical, 'b')

plt.show()
