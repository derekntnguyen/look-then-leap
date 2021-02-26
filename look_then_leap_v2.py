#  -*- coding: utf-8 -*-
'''
P0 Assignment
Derek Nguyen
Created: 2019-01-23
Modified: 2019-01-25
Due: 2019-01-24
'''

# %% codecell
import numpy as np
import matplotlib# used to create interactive plots in the Hydrogen package of the Atom IDE
matplotlib.use('Qt5Agg') # used to create interactive plots in the Hydrogen package of the Atom IDE
import matplotlib.pyplot as plt

numTrials,numMs = 10000,30
data = np.zeros((numTrials,numMs))

for trial in range(numTrials):
    for M in range(numMs):
        roommates = np.arange(1,numMs + 1) # create and shuffle a selection of roommates
        np.random.shuffle(roommates)

        if M == 0: # prevent indexing error of assigning look period to [0:0]
            look = roommates[M]
            leap = roommates[M:-1]
        else:
            look = roommates[:M]
            leap = roommates[M:-1]

        bestRoommate = np.amax(look)

        for potRoommate in leap: # iterate through the leap period and test the potRoommate against the bestRoommate, output the probability of selection
            if potRoommate > bestRoommate:
                data[trial,M] = potRoommate/len(roommates)
                break
            elif all(leap) < bestRoommate:
                data[trial,M] = 0

best = data == 1 # create boolean matrix of acquiring the best roommate
none = data == 0 # create boolean matrix of acquiring no roommate

best = best.sum(axis=0) / numTrials # sum and calculate the probability of acquiring the best roommate from the # of trials
none = none.sum(axis=0) / numTrials # sum and calculate the probability of acquiring no roommate from the # of trials

plt.subplot(1,2,1)
plt.plot(best)
plt.title('Look-then-Leap to get the Best')
plt.xlabel('Number of Roommates in the Look Phase (M)')
plt.ylabel('Probability of Getting the Best Roommate')

plt.subplot(1,2,2)
plt.plot(none)
plt.title('Look-then-Leap to Get None')
plt.xlabel('Number of Roommates in the Look Phase (M)')
plt.ylabel('Probability of Getting No Roommates')
