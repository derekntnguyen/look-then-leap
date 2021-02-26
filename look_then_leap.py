#  -*- coding: utf-8 -*-
'''
P0 Assignment
Derek Nguyen
Created: 2019-01-23
Due: 2019-01-24
'''

# %%
import numpy as np
import matplotlib.pyplot as plt

data = np.zeros((10000,30))
row,col = np.shape(data)

for trial in range(1,row):
    for M in range(1,col):
        roommates = np.arange(1,30)
        np.random.shuffle(roommates)
        look = roommates[0:M]
        leap = roommates[M:30]
        bestRoommate = np.amax(look)
        for potRoommate in leap:
            if potRoommate > bestRoommate:
                data[trial,M] = potRoommate/29
                break
            else:
                data[trial,M] = 0

best = data == 1
none = data == 0

best = best.sum(axis=0) / row
none = none.sum(axis=0) / row

plt.subplot(1,2,1)
plt.plot(best)
plt.title('Look-then-Leap to get the Best')
plt.xlabel('Number of Roommates in the Look Phase (M)')
plt.ylabel('Probability of Getting the Best Roommate')

plt.subplot(1,2,2)
plt.plot(none[2:-1])
plt.title('Look-then-Leap to Get None')
plt.xlabel('Number of Roommates in the Look Phase (M)')
plt.ylabel('Probability of Getting No Roommates')
