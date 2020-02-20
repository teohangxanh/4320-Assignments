'''Course: COSC 4320 - System modeling and simulation
Student name: Nghia Dang   Student ID: 726082
Assignment 2
Requirement: Modeling and simulating the attendance of a soccer team'''

from pylab import plot, show

# I turned the rate into scores: Win = 3, Draw = 1, Lose = 0
scores = [3, 3, 3, 3, 3, 3, 0, 3, 1, 1, 3, 0, 0, 3, 3, 0, 3, 3]
# Assumption: The attendance before 3rd is the same: 8000
att = [8000] * len(scores)
timesteps = []
k=15000
r = 0.1
first_growth = True
note = ''
for i in range(len(scores)):
    if i >= 2:
        game_before = scores[i - 1] + scores[i - 2]
        # WW
        if game_before == 6:
            if first_growth:
                r = 0.1
                first_growth = False
            else:
                r = (att[i-1] - att[i-2])/att[i-2]
            # Increase logistically
            att[i] = att[i-1] + r * att[i-1]*(1-att[i-1]/k)
            note = 'Increase logistically'
                
        # WD
        elif game_before == 4:
            if first_growth:
                r = 0.1
                first_growth = False
            else:
                # Increase linearly
                (att[i-1] - att[i-2])/att[i-2]
            att[i] = att[i-1] * (1+r)
            note = 'Increase linearly'
            
        # LL
        elif game_before == 0:
            # Decrease geometrically
            att[i] = 0.9 * att[i-1]
            note = 'Decrease geometrically'
            
        # Other results
        else:
            # Decrease linearly
            (att[i-1] - att[i-2])/att[i-2]
            att[i] = att[i-1] * (1+r)
            note = 'Decrease linearly'
    timesteps.append(i)
    print(note, end=' ')
    print(r, end=' ')
    print(att[i])
      
# print(timesteps)
# print(att)
plot(timesteps, att)
show()


'''r = 0.1
K = 15000
# Dt = 0.01
x=8000
result=[]
timesteps=[]
t=0

def initialize():
    global x, result, t, timesteps
    x = 8000
    result = [x]
    t = 0
    timesteps = [t]
    
def observe():
    global x, result, t, timesteps
    result.append(x)
    timesteps.append(t)

def update():
    global x, result, t, timesteps
    x = x + r * x * (1 - x / K)
    t = t + Dt

initialize()
    while t < 50:
    update()
    observe()
 
plot(timesteps, result)
show()'''
