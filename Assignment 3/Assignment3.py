'''
Course: COSC 4320 01 System Modeling and Simulation
Assignment 3
Author: Nghia Dang
Date created: 04/04/2020
'''

import numpy as np
import matplotlib.pyplot as plt
import math

# Problem 1, phase-space part'''

a = 0.8
b = 0.9
start = 0
end = 10
gap = 1
length = (end - start) // gap

def f(a, b, x): 
    return x + a * (math.sin(b * x))

def func(a, b, alist): 
    return [x + a * (math.sin(b * x)) for x in alist]

x = np.linspace(start, end, length)
fig = plt.figure()
plt.plot(x, func(a, b, x), '-')
plt.xlabel('x(t)')
plt.ylabel('x(t + 1)')

'''f'(x) = 1 + ab * cos(bx)
f'(0) = 1 + ab
As a, b > 0, f'(0) > 0 => This model is not stable at the eq point
'''

# Problem 1, cobweb part
def initialize():
    global N, result
    N = 0.1
    result = [N]

def observe():
    global N, result
    result.append(N)

def update():
    global N, result
    N = f(a, b, N)

initialize()
for t in range(100):
    update()
    observe()
    
plt.plot([start, end], [start, end], 'k')
curvex = np.linspace(start, end, length)
curvey = func(a, b, curvex)
plt.plot(curvex, curvey, 'k')

horizontal = [result[0]]
vertical = [result[0]] 
for N in result[1:]:
    horizontal.append(vertical[-1])
    vertical.append(N)
    horizontal.append(N)
    vertical.append(N)    
plt.plot(horizontal, vertical, 'b')

plt.show()

''' Problem 2:
    1. Find eq points:
        When all x's = x(eq) and y's = y(eq), the system becomes
        x(eq) = x(eq) + 2x(eq)(1 - x(eq)) - x(eq)y(eq)
        y(eq) = t(eq) + 2y(eq)(1 - y(eq)) - x(eq)y(eq)
        Which is equivalent to
        x(eq)y(eq) = 2x(eq)(1 - x(eq)) (1)
        x(eq)y(eq) = 2y(eq)(1 - y(eq)) (2)
        When x(eq) = 0, we find that y(eq) = 0, 1
        When y(eq) = 0, we find that x(eq) = 0, 1
        So, there are three eq points: (0, 0), (1, 0), and (0, 1)
        After taking care of the cases when x = 0 or y = 0, 
        we can divide (1) by x(eq) and (2) by y(eq)
        y(eq) = 2(1 - x(eq))
        x(eq) = 2(1 - y(eq))
        Then, we substitute y(eq) = 2(1 - x(eq)) into x(eq):
            x(eq = 2(1 - (2(1 - x(eq))))
            ...x(eq) = 2/3
            Then, we substitute x(eq) back to y(eq) and find that y(eq) = 2/3
        So far, there are four eq points: (0, 0), (0, 1), (1, 0), and (2/3, 2/3)
        
        
    2. Calculate the Jacobian matrix at the eq point where x > 0 and y > 0
        x = x + 2x(1 - x) - xy
        d/dx = d/dx(x + 2x(1 - x) - xy)
        d/dx = d/dx(3x - 2x^2 -xy) = 3 - 4x - y = 3 - 4(2/3) - 2/3 = 1
        
        y = y + 2y(1 - y) - xy
        d/dx = d/dx(x + 2x(1 - x) - xy)
        d/dx = -y = -2/3
        
        x = x + 2x(1 - x) - xy
        d/dy = d/dy(x + 2x(1 - x) - xy)
        d/dy = -x = -2/3
        
        y = y + 2y(1 - y) - xy
        d/dy = d/dy(y + 2y(1 - y) - xy)
        d/dy = d/dy(3y - 2y^2 -xy) = 3 - 4y - x = 3 - 4(2/3) - 2/3 = 1
        
        Then, the J matrix becomes
          1    -2/3
        -2/3    1
        
    3. Calculate the Eigenvalues of the matrix obtained
        det(A - lambdaI) = 0
        (1 - lambda)(1 - lambda) - (2/3 * 2/3) = 0
        lambda^2 - 2lambda + 1 - 4/9 = 0
        lambda^2 - 2lambda + 5/9 = 0
        (lambda - 1/3)(lambda - 5/3) = 0
        Then, we find out the eigenvalues of the J matrix = 1/3, 5/3
        
    4. Determine whether the eq point is stable, unstable, or Lyapunov stable
        As the dominant Eigenvalue = 5/3 > 1,
        the system is unstable around x(eq)
'''
    