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
