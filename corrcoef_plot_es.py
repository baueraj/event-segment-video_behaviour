'''
plot correlation matrices among individual adults and children
plot bar graphs of combined adult-child correlations, and within- and across-individual adults and children correlations
'''

import os, sys, pdb
import numpy as np
#np.set_printoptions(threshold = np.nan)
import matplotlib.pyplot as plt
from scipy.stats.stats import *
import pandas as pd
import csv
#import analy_funs
from analy_funs import *
#import init
from init import *
plt.close('all')

# setup
stup = {
       'smooth_win': 5,
       'smooth_b4plot_fl': 1
}

# correlation matrix plots among individual adults and children
aLabels1 = list(map(str, aPs))
aLabels = ['a' + i for i in aLabels1]
cLabels1 = list(map(str, cPs))
cLabels = ['c' + i for i in cLabels1]
labels = aLabels + cLabels

for i in range(len(allDat['durs'])):
    dat = pd.concat([allDat['aEventBounds'][i], allDat['cEventBounds'][i]], axis = 1)
    dat.columns = labels
    if stup['smooth_b4plot_fl']:
        dat = dat.rolling(window = stup['smooth_win']).mean()
        dat = dat.fillna(value = 0)
    plot_sim_mtx(dat.corr(), labels, title = 'cartoon-' + str(i + 1))
    plt.show()


# bar plots of correlations between and within adults and children

# correlations between pooled adult and child smoothed (across sample) data
aSumEvtB = [i.sum(axis = 1) for i in allDat['aEventBounds']]
aSmoothSumEvtB = [plot_mov_avg_events(i, stup['smooth_win'], 'b', 1, 0, 0) for i in aSumEvtB]

cSumEvtB = [i.sum(axis = 1) for i in allDat['cEventBounds']]
cSmoothSumEvtB = [plot_mov_avg_events(i, stup['smooth_win'], 'b', 1, 0, 0) for i in cSumEvtB]

corr_rp_acSmoothSumEvtB = [pearsonr(np.nan_to_num(i.values), np.nan_to_num(j.values)) for i, j in zip(aSmoothSumEvtB, cSmoothSumEvtB)]
corr_r_acSmoothSumEvtB = [i[0] for i in corr_rp_acSmoothSumEvtB]
corr_p_acSmoothSumEvtB = [i[1] for i in corr_rp_acSmoothSumEvtB]


# correlations within adult and child data
corr_r_a = [i.rolling(window = stup['smooth_win']).mean().fillna(value = 0).corr() for i in allDat['aEventBounds']]
corr_ind_a = np.triu(np.ones(corr_r_a[0].shape), 1).astype(np.bool)
corr_r_a_mean = [np.nanmean(i.where(corr_ind_a).values.flatten()) for i in corr_r_a]
corr_r_a_std = [np.nanstd(i.where(corr_ind_a).values.flatten()) for i in corr_r_a]
corr_r_a_SEM = [i / np.sqrt(len(np.where(corr_ind_a == True)[0])) for i in corr_r_a_std]

corr_r_c = [i.rolling(window = stup['smooth_win']).mean().fillna(value = 0).corr() for i in allDat['cEventBounds']]
corr_ind_c = np.triu(np.ones(corr_r_c[0].shape), 1).astype(np.bool)
corr_r_c_mean = [np.nanmean(i.where(corr_ind_c).values.flatten()) for i in corr_r_c]
corr_r_c_std = [np.nanstd(i.where(corr_ind_c).values.flatten()) for i in corr_r_c]
corr_r_c_SEM = [i / np.sqrt(len(np.where(corr_ind_c == True)[0])) for i in corr_r_c_std]

# correlations between adult and child data
# NOTE: adults MUST be listed first, for correct indexing of the corr matrix
combDat = [pd.concat([i, j], axis = 1) for i, j in zip(allDat['aEventBounds'], allDat['cEventBounds'])]
corr_r_ac = [i.rolling(window = stup['smooth_win']).mean().fillna(value = 0).corr() for i in combDat]
corr_ind_ac = np.zeros(corr_r_ac[0].shape).astype(np.bool)
corr_ind_ac[0:len(aPs), len(aPs):] = True
corr_r_ac_mean = [np.nanmean(i.where(corr_ind_ac).values.flatten()) for i in corr_r_ac]


# finally, plot the bar plots
corr_comb = [[i, j, k, l] for i, j, k, l in zip(corr_r_acSmoothSumEvtB, corr_r_ac_mean, corr_r_a_mean, corr_r_c_mean)]
pltColors = ['r', 'orange', 'b', 'g']
pltXLabels = ['bt_comb_ac', 'bt_ac', 'wi_a', 'wi_c']
for i in range(len(corr_comb)):
    plt.figure()    
    for j in range(len(corr_comb[i])):
        plt.bar(j + 1, corr_comb[i][j], width = 1, color = pltColors[j])
    plt.title(cartoonNames[i])
        
    ax = plt.gca()
    rng = np.arange(1.5, 4.5 + 1, 1)
    ax.set_xticks(rng)
    ax.set_xticklabels(pltXLabels)
    
    ax.set_ylim([-0.05, 0.5])
    rng = np.arange(-0.05, 0.5 + 0.05, 0.05)
    ax.set_yticks(rng)
    ax.set_yticklabels(rng)
    plt.show()
    
# finally, plot the bar plots (FOR TAMeG 2017)
corr_comb = [[i, j] for i, j in zip(corr_r_a_mean, corr_r_c_mean)]
corr_SEM_comb = [[i, j] for i, j in zip(corr_r_a_SEM, corr_r_c_SEM)]
pltColors = ['b', 'r']
pltXLabels = ['wi_a', 'wi_c']
for i in range(len(corr_comb)):
    plt.figure()    
    for j in range(len(corr_comb[i])):
        plt.bar(j/2 + 0.5, corr_comb[i][j], width = 0.4, align='center', color = pltColors[j])
        plt.errorbar(j/2 + 0.5, corr_comb[i][j], yerr = corr_SEM_comb[i][j], ecolor = 'k', elinewidth = 2.5)
    #plt.title(cartoonNames[i])
        
    ax = plt.gca()
    rng = np.arange(0.5, 1.5, 0.5)
    ax.set_xticks(rng)
    ax.set_xticklabels(pltXLabels)
    
    ax.set_ylim([-0.05, 0.2])
    rng = np.arange(-0.05, 0.2 + 0.05, 0.05)
    ax.set_yticks(rng)
    ax.set_yticklabels(rng, fontsize = 35)
    
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.show()
        
'''pltColors = ['r', 'o', 'b', 'g']
fig = plt.figure()
for i in range(len(corr_comb)):
    for j in range(len(corr_comb[i])):        
        plt.bar(j + 1, corr_comb[i][j], color = pltColors[j])'''
        