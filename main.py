# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:57:41 2018





@author: Vincent
"""
import os
import numpy as np


def GetSignal(fname, last_n):
    # read and return the last n lines of CSV file fname
    import csv
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        nrows = len(data)

        # return last n rows of data
        return np.asarray(data[nrows-1-last_n : nrows-1])

def ProcessSignal(signal):
    # do some processing of the signal

    signal = signal[:,1:10]
    signal = signal.astype('float')

    #e.g. take average along rows
    processed_signal = np.mean(signal,0)

    # return processed signal
    return processed_signal

def InitiateLights:
    # initiate lights





fname = 'C:\\Users\\Vincent\\Documents\\GitHub\\rainbow_muse\\test.csv'

gsignal = GetSignal(fname,2)
psignal = ProcessSignal(gsignal)

print psignal