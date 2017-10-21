def get_participant_data(aPs, cPs, durs, dPath, pPath):
    """
    read participant data stored as csv files

    Parameters
    ----------
    aPs : vector array
        adult participant IDs
    cPs : vector array
        children participant IDs
    durs : vector array
        cartoon durations in seconds    
    dPath : string
        path to data files
    pPath : string
        path to participant files

    Returns
    -------
    allDat : dictionary
        'aTimeStamps' : adult timestamps of event boundaries
        'aTimeStampsMod' : adult timestamps reformatted (minute:second)
        'aEventBounds' : adult event boundaries in vector of timepoints
        'aDescs' : adult descriptions
        'cTimeStamps' : children timestamps
        'cTimeStampsMod' : children timestamps reformatted (minute:second)
        'cEventBounds' : children event boundaries in vector of timepoints
        'cDescs' : children descriptions
        'durs' : cartoon durations (including 0 as a timepoint)

    Notes
    -----
    assumes filename format and csv contents arrangement
    frequently used parameters and values:
        #aPs = np.array([1, 2, 5, 6, 7, 8, 9, 10, 11])
        aPs = np.array([6, 7, 9, 10, 11])
        cPs = np.array([1, 2, 3, 4, 5])
        durs = np.array([418, 439, 385, 575, 460]) + 2
        dPath = '/Users/bauera/Dropbox/UofT/experiments/event-segmentation/experiment/output-from-test-rooms/'
        pPath = '/Users/bauera/Dropbox/UofT/experiments/event-segmentation/experiment/participant_files/'
    """
    
    import os, sys, pdb
    import numpy as np
    #np.set_printoptions(threshold = np.nan)
    import pandas as pd
    import csv

    # read adult data first, then child data
    for p in ('a', 'c'):
        if p == 'a':
            iPs = aPs
        else:
            iPs = cPs
            
        for idx, i in enumerate(iPs):
            iFile = open(pPath + '/' + p + '_p' + str(i) + '.csv')
            reader = csv.reader(iFile)
            for row in reader:
                iCartoonOrder = row
            iFile.close()
    
            # ideally, I'd not use "exec" and would use 3D dataframes, but I don't know how to do this yet
            for s, c in enumerate(iCartoonOrder):
                iDat = pd.read_csv(dPath + '/' + p + '_p' + str(i) + '_s' + str(s + 1) + '_c' + c + '.csv', header = None)
                # maybe I don't need to initalize like this with a special i = 1 case
                # also, it's un-ideal to use "exec" so many times, here and below. FIX THIS in next version
                eventBounds = pd.Series(data = np.zeros(durs[int(c) - 1]))
                eventBounds[iDat[0].round()] = 1
    
                if idx == 0:
                    exec(p + 'TimeStamps_c' + c + ' = iDat[0].round()')
                    exec(p + 'TimeStampsMod_c' + c + ' = reformat_timestamp(iDat[0].values)')
                    exec(p + 'EventBounds_c' + c + ' = eventBounds')
                    exec(p + 'Descs_c' + c + ' = iDat[1]')
                else:
                    exec(p + 'TimeStamps_c' + c + ' = pd.concat([' + p + 'TimeStamps_c' + c + ', iDat[0].round()], ignore_index=False, axis = 1)')
                    exec(p + 'TimeStampsMod_c' + c + ' = pd.concat([' + p + 'TimeStampsMod_c' + c + ', reformat_timestamp(iDat[0].values)], ignore_index=False, axis = 1)')
                    exec(p + 'EventBounds_c' + c + ' = pd.concat([' + p + 'EventBounds_c' + c + ', eventBounds], ignore_index=False, axis = 1)')
                    exec(p + 'Descs_c' + c + ' = pd.concat([' + p + 'Descs_c' + c + ', iDat[1]], ignore_index=False, axis = 1)')
                
                if idx != 0:
                    #pdb.set_trace()
                    #tmpNamespace = {}
                    #exec('tmpDF = ' + p + 'TimeStamps_c' + c, tmpNamespace)
                    #tmpDFSize = tmpNamespace['tmpDF'].shape[1]
                    colNames = list(map(str, np.array(range(idx + 1))))
                    exec(p + 'TimeStamps_c' + c + '.columns = colNames')
                    exec(p + 'TimeStampsMod_c' + c + '.columns = colNames')
                    exec(p + 'EventBounds_c' + c + '.columns = colNames')
                    exec(p + 'Descs_c' + c + '.columns = colNames')

    aTimeStamps = []
    aTimeStampsMod = []
    aEventBounds = []
    aDescs = []
    
    cTimeStamps = []
    cTimeStampsMod = []
    cEventBounds = []
    cDescs = []
    
    for idx, c in enumerate(iCartoonOrder):  # just a way to get the range of cartoons, using last participant's cartoon order
        exec('aTimeStamps.append(aTimeStamps_c' + str(idx + 1) + ')')
        exec('aTimeStampsMod.append(aTimeStampsMod_c' + str(idx + 1) + ')')
        exec('aEventBounds.append(aEventBounds_c' + str(idx + 1) + ')')
        exec('aDescs.append(aDescs_c' + str(idx + 1) + ')')
        
        exec('cTimeStamps.append(cTimeStamps_c' + str(idx + 1) + ')')
        exec('cTimeStampsMod.append(cTimeStampsMod_c' + str(idx + 1) + ')')
        exec('cEventBounds.append(cEventBounds_c' + str(idx + 1) + ')')
        exec('cDescs.append(cDescs_c' + str(idx + 1) + ')')
            
    allDat = {'aTimeStamps': aTimeStamps, 'aTimeStampsMod': aTimeStampsMod, 'aEventBounds' : aEventBounds, 'aDescs': aDescs,
              'cTimeStamps': cTimeStamps, 'cTimeStampsMod': cTimeStampsMod, 'cEventBounds' : cEventBounds, 'cDescs': cDescs,
              'aPs': aPs, 'cPs': cPs, 'durs': durs}
    
    return allDat



def reformat_timestamp(ts):
    """
    reformats numerical second to string of (minutes : seconds) format

    Parameters
    ----------
    ts : numpy array
        array of numerical seconds

    Returns
    -------
    pd.Series(ts_mod) : pandas Series
        series of strings in (minutes : seconds) format

    Notes
    -----
    NOTA BENE: takes a numpy array and returns a pandas series 
    """
    
    import os, sys, pdb
    import numpy as np
    #np.set_printoptions(threshold = np.nan)
    import pandas as pd
    
    [m, s] = divmod(ts, 60)
    m2 = [str(int(x)) for x in m]
    s2 = [str(int(x)) for x in s.round()]
    ts_mod = [x + ':' + y for x, y in zip(m2, s2)]
    
    return pd.Series(ts_mod)



def plot_mov_avg_events(s, win, clr, alph, plt_fl, newFig_fl):
    """
    returns moving average (smoothing) of timeseries and optionally plots this new series

    Parameters
    ----------
    s : pandas series
        (only y-axis) data to be plotted 
    win : int
        window size (separately applied to past and future) for moving average
    clr : string
        color for plot
    alph: float/double/int?
        level (0-1)for plot fill transparency
    plt_fl: int/bool
        flag to plot figure
    newFig_fl : int/bool
        flag to create new figure for plotting or plot on current/initialized figure

    Returns
    -------
    srm : pandas series
        moving average series 

    Notes
    -----
    examples of frequently used series parameter:
        ac1=allDat['aEventBounds'][0].sum(axis=1)
    """
    
    import os, sys, pdb
    import numpy as np
    #np.set_printoptions(threshold = np.nan)
    import pandas as pd 
    import matplotlib.pyplot as plt
    
    # using 20 seconds as a non-parameterized (in function) default increment for x-ticks
    stepSize = 20
    
    sr = s.rolling(window = win)  
    srm = sr.mean()
    
    if plt_fl:
        if newFig_fl:
            plt.figure()
        ax = srm.plot.area(color = clr, alpha = alph)
        rng = np.arange(0, max(s.index) + stepSize, stepSize)
        
        #ax.set_ylim([0, 1.8])
        
        ax.set_xticks(rng)
        ax.set_xticklabels(reformat_timestamp(rng).values, rotation = -45)
        #plt.axis('off')
        #plt.xticks([], [])
        #plt.yticks([], [])

    return srm



#NOT FINISHED!
def plot_dis_mtx(mtx, labels, title=''):
    """
    plots dissimilarity matrix (assumes input is dissimilarity for now)

    Parameters
    ----------
    x

    Returns
    -------
    NONE 

    Notes
    -----
    x
    """
    
    import os, sys, pdb
    import numpy as np
    #np.set_printoptions(threshold = np.nan)
    import pandas as pd 
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.imshow(mtx, interpolation='nearest')
    plt.set_cmap('jet_r')
    plt.xticks(range(len(mtx)), labels, rotation=-45)
    plt.yticks(range(len(mtx)), labels)
    plt.title(title)
    plt.clim((0, 2))
    plt.colorbar()



def plot_sim_mtx(mtx, labels, title=''):
    """
    plots similarity matrix AND forces negative correlations to 0 in clim display
    
    Parameters
    ----------
    x

    Returns
    -------
    NONE 

    Notes
    -----
    x
    """
    
    import os, sys, pdb
    import numpy as np
    #np.set_printoptions(threshold = np.nan)
    import pandas as pd 
    import matplotlib.pyplot as plt
    
    #mtx[mtx < 0] = 0
    
    plt.figure()
    plt.imshow(mtx, interpolation='nearest')
    plt.set_cmap('jet')
    plt.xticks(range(len(mtx)), labels, rotation=-45)
    plt.yticks(range(len(mtx)), labels)
    plt.title(title)
    plt.clim((0, 1))
    plt.colorbar()



def print_empty_coding_files(allDat, bcPath='./blank-coding-files/'):
    """
    prints empty csv files for later coding

    Parameters
    ----------
    allDat : dictionary
        contains data returned from get_participant_data()
    bcPath : string
        optional path with folder name to directory where blank coding files are written

    Returns
    -------
    NONE

    Notes
    -----
    the idea is to take the generated empty files and COPY them to another location
    """

    import os, sys, pdb
    import numpy as np
    np.set_printoptions(threshold = np.nan)
    import pandas as pd
    from pandas import ExcelWriter
    from init_es import cartoonNames
    
    aPs = allDat['aPs']
    cPs = allDat['cPs']
    
    for p in ('a', 'c'):
        if p == 'a':
            iPs = aPs
        else:
            iPs = cPs
            
        tsMod_dicName = p + 'TimeStampsMod'
        desc_dicName = p + 'Descs'
        
        for iidx, i in enumerate(iPs):
            i_cdf_list = []
            writer = ExcelWriter(bcPath + p + str(i) + '.xlsx', engine='xlsxwriter')
            for cidx in range(len(allDat[tsMod_dicName])):                
                tsMod_dat = allDat[tsMod_dicName][cidx].iloc[:,iidx]
                desc_dat = allDat[desc_dicName][cidx].iloc[:,iidx]
                cdf1 = pd.concat([tsMod_dat, desc_dat], axis = 1)
                cdf1 = cdf1[pd.notnull(cdf1.iloc[:, 0])]
                cdf1.columns = ['ts', 'desc']
                cdf2 = pd.DataFrame(np.empty([len(cdf1), 6]) * np.nan, columns=['ca', 'ch', 'g', 'o', 's', 't'])
                cdf = pd.concat([cdf1, cdf2], axis = 1)
                i_cdf_list.append(cdf)                
                cdf.to_excel(writer, cartoonNames[cidx])
            writer.save()   
