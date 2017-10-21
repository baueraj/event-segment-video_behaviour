'''
plot moving average of event boundaries for adults and children superimposed
'''

#import os, sys, pdb
#import numpy as np
#np.set_printoptions(threshold = np.nan)
import matplotlib.pyplot as plt
plt.close('all')
plt.show()
#import pandas as pd
#import csv
#import analy_funs_es
#from analy_funs import *
#import init
from init_es import *


# setup
stup = {
       #'smooth_win': 5
       'smooth_win': 2
}

'''
#children and adults superimposed

aSmthSumEvtB = []
cSmthSumEvtB = []
for i in range(len(allDat['durs'])):
    aSmthSumEvtB.append(plot_mov_avg_events(allDat['aEventBounds'][i].sum(axis = 1), stup['smooth_win'], 'b', 1, 1, 1).fillna(value = 0))
    cSmthSumEvtB.append(plot_mov_avg_events(allDat['cEventBounds'][i].sum(axis = 1), stup['smooth_win'], 'r', 0.6, 1, 0).fillna(value = 0))

plt.show('all')
'''

#just adults

aSmthSumEvtB = []
for i in [1, 2]:
    aSmthSumEvtB.append(plot_mov_avg_events(allDat['aEventBounds'][i].sum(axis = 1), stup['smooth_win'], 'b', 1, 1, 1).fillna(value = 0))

plt.show('all')