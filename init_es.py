import os, sys, pdb
import numpy as np
#np.set_printoptions(threshold = np.nan)
import pandas as pd
import csv
#import analy_funs
from analy_funs_es import *

#aPs = np.array([6, 7, 9, 10, 11, 12, 13, 14]) #USED IN ANALYSIS, DON'T ERASE RECORD
#aPs = np.hstack((np.array([1, 2]), np.array(range(11)) + 4))
aPs = np.array(range(20)) + 5
cPs = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#aPs = np.array([13])
#cPs = np.array([7])
durs = np.array([418, 439, 385, 575, 460]) + 2
dPath = '/Users/bauera/Dropbox/UofT/experiments/event-segmentation/experiment/output-from-test-rooms/'
pPath = '/Users/bauera/Dropbox/UofT/experiments/event-segmentation/experiment/participant_files/'
cartoonNames = ['DuckTales', 'Rugrats', 'BusyTown', 'ChipNDale', 'InspectGadget']

allDat = get_participant_data(aPs, cPs, durs, dPath, pPath)

'''
if len(aPs) > 1 and len(cPs) > 1:
    ac1 = allDat['aEventBounds'][0].sum(axis=1)
    ac2 = allDat['aEventBounds'][1].sum(axis=1)
    ac3 = allDat['aEventBounds'][2].sum(axis=1)
    ac4 = allDat['aEventBounds'][3].sum(axis=1)
    ac5 = allDat['aEventBounds'][4].sum(axis=1)
    cc1 = allDat['cEventBounds'][0].sum(axis=1)
    cc2 = allDat['cEventBounds'][1].sum(axis=1)
    cc3 = allDat['cEventBounds'][2].sum(axis=1)
    cc4 = allDat['cEventBounds'][3].sum(axis=1)
    cc5 = allDat['cEventBounds'][4].sum(axis=1)
elif len(aPs) > 1 and len(cPs) == 1:
    ac1 = allDat['aEventBounds'][0].sum(axis=1)
    ac2 = allDat['aEventBounds'][1].sum(axis=1)
    ac3 = allDat['aEventBounds'][2].sum(axis=1)
    ac4 = allDat['aEventBounds'][3].sum(axis=1)
    ac5 = allDat['aEventBounds'][4].sum(axis=1)
    cc1 = allDat['cEventBounds'][0]
    cc2 = allDat['cEventBounds'][1]
    cc3 = allDat['cEventBounds'][2]
    cc4 = allDat['cEventBounds'][3]
    cc5 = allDat['cEventBounds'][4]
if len(aPs) == 1 and len(cPs) > 1:
    ac1 = allDat['aEventBounds'][0]
    ac2 = allDat['aEventBounds'][1]
    ac3 = allDat['aEventBounds'][2]
    ac4 = allDat['aEventBounds'][3]
    ac5 = allDat['aEventBounds'][4]
    cc1 = allDat['cEventBounds'][0].sum(axis=1)
    cc2 = allDat['cEventBounds'][1].sum(axis=1)
    cc3 = allDat['cEventBounds'][2].sum(axis=1)
    cc4 = allDat['cEventBounds'][3].sum(axis=1)
    cc5 = allDat['cEventBounds'][4].sum(axis=1)
if len(aPs) == 1 and len(cPs) == 1:
    ac1 = allDat['aEventBounds'][0]
    ac2 = allDat['aEventBounds'][1]
    ac3 = allDat['aEventBounds'][2]
    ac4 = allDat['aEventBounds'][3]
    ac5 = allDat['aEventBounds'][4]
    cc1 = allDat['cEventBounds'][0]
    cc2 = allDat['cEventBounds'][1]
    cc3 = allDat['cEventBounds'][2]
    cc4 = allDat['cEventBounds'][3]
    cc5 = allDat['cEventBounds'][4]
'''