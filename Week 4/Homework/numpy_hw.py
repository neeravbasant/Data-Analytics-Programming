# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 22:27:38 2014

@author: Neerav Basant
"""

import numpy as np
import random
random.seed(1)

numTrials = 10000
trialLength = 100
startingStake = 20

np.set_printoptions(precision=1)

unifProbs = np.random.rand(numTrials,20,trialLength)
winProbs = unifProbs > (18.0/37.0)

state = np.zeros((numTrials,20))
state[:] = startingStake # initial values

newState = np.zeros((numTrials,20))
average = []

for i in xrange(10000):
    for j in xrange(20):
        for k in xrange(100):
            if winProbs[i][j][k]:
                if k == 0:
                    newState[i][j] = state[i][j] + (j + 1)
                else:
                    newState[i][j] = newState[i][j] + (j + 1)
            else:
                if k == 0:
                    newState[i][j] = state[i][j] - (j + 1)
                else:
                    newState[i][j] = newState[i][j] - (j + 1)
            
            if newState[i][j] > j:
                continue
            else:
                break
            
print newState.mean(axis = 0)
                    