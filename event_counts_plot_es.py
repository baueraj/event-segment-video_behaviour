'''
plot event boundary counts for adults and children
'''

import os, sys, pdb
import numpy as np
#np.set_printoptions(threshold = np.nan)
import matplotlib.pyplot as plt
import pandas as pd
import csv
#import analy_funs
from analy_funs import *
#import init
from init import *
plt.close('all')

# get the count data from adults and children
aCountEvtB = [i.sum(axis = 0) for i in allDat['aEventBounds']]
cCountEvtB = [i.sum(axis = 0) for i in allDat['cEventBounds']]

# plot the count data
count_comb = [[i, j] for i, j in zip(aCountEvtB, cCountEvtB)]
pltXLabels = ['a', 'c']
for i in range(len(count_comb)):
    plt.figure()    
    plt.boxplot(count_comb[i])
    plt.title(cartoonNames[i])
    ax = plt.gca()
    ax.set_xticklabels(pltXLabels)
    plt.show()