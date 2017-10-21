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

aSmthSumEvtB.append(plot_mov_avg_events(allDat['aEventBounds'][1].sum(axis = 1), stup['smooth_win'], 'b', 1, 1, 1).fillna(value = 0))
rugratsTones = pd.read_excel(dPath + '../../designMaterials/Tone Timing.xlsx', sheetname='BigPeople Video')
x = (rugratsTones['Elapsed Time 1 (ms)']/1000).values
y = np.ones(len(x))
plt.plot(x, y, 'yo')

x = (rugratsTones['Elapsed Time 3 (ms)']/1000).values
y = np.ones(len(x)) + 0.5
plt.plot(x, y, 'ro')

x = (rugratsTones['Elapsed Time 5 (ms)']/1000).values
y = np.ones(len(x)) + 1
plt.plot(x, y, 'go')

aSmthSumEvtB.append(plot_mov_avg_events(allDat['aEventBounds'][2].sum(axis = 1), stup['smooth_win'], 'b', 1, 1, 1).fillna(value = 0))
busyWorldTones = pd.read_excel(dPath + '../../designMaterials/Tone Timing.xlsx', sheetname='Treasure Video')
x = (busyWorldTones['Elapsed Time 2 (ms)']/1000).values
y = np.ones(len(x))
plt.plot(x, y, 'yo')

x = (busyWorldTones['Elapsed Time 4 (ms)']/1000).values
y = np.ones(len(x)) + 0.5
plt.plot(x, y, 'ro')

x = (busyWorldTones['Elapsed Time 6 (ms)']/1000).values
y = np.ones(len(x)) + 1
plt.plot(x, y, 'go')

plt.show('all')