# -*- coding: utf-8 -*-
"""Lab2FindS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hz01Z-tFtcjqNZ8wQAlHmkzRCqG8SBqr
"""

import pandas as pd
import numpy as np
data = pd.read_csv('datastat.csv')
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

def train(con,tar):
    for i,val in enumerate(tar):
        if val=='yes':
            specific_h = con[i].copy()
            break

    for i,val in enumerate(con):
        if tar[i]=='yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
    return specific_h

print(train(concepts,target))