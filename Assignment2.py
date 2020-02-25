'''Course: COSC 4320 - System modeling and simulation
Student name: Nghia Dang   Student ID: 726082
Assignment 2
Requirement: Modeling and simulating the attendance of a soccer team'''

import pylab

# I turned the ratios into scores: Win = 3, Draw = 1, Lose = 0
scores = [3, 3, 3, 3, 3, 3, 0, 3, 1, 1, 3, 0, 0, 3, 3, 0, 3, 3]
# Assumption: The attendance before the 3rd is the same: 8000
att = [8000] * len(scores)
timesteps = []
k=15000 # Capacity of the stadium
r = 1.1

for i in range(len(scores)):
    # Assumption: The attendance does not change after the first two games
    if i >= 2:
        game_before = scores[i - 1] + scores[i - 2]
        # win win
        if game_before == 6:
            # Increase logistically
            r = (r-1)*att[i-1]/(att[i-1]-k) + 1 - (r-1)*k/(att[i-1]-k)
            att[i] = att[i-1] + r * att[i-1]*(1-att[i-1]/k)

        # win draw
        elif game_before == 4:
            # Increase linearly
            att[i] = att[i-1] * r
            
        # lose lose
        elif game_before == 0:
            # Decrease geometrically
            att[i] = att[i-1] ** (0.9) # Since decay rate = 0.1 
            
        # Other results
        else:
            # Decrease linearly
            att[i] = att[i-1] * (2-r)
    timesteps.append(i+1)
      
pylab.plot(timesteps, att)
pylab.xlabel('Game')
pylab.ylabel('Attendance')
pylab.title("Modeled Anfield stadium's attendance, season 2018/2019")