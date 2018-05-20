# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:10:42 2018

@author: Administrator
"""

from urllib.request import urlopen
import pandas as pd

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urlopen(target_url)

path = r'C:\Users\Administrator\Desktop\ETPA\Chapter2\data_ist.csv'

xList = []

for line in data:
    #split on comma
    row = line.decode('utf-8').strip().split(",")
    xList.append(row)

dataframe = pd.DataFrame(xList)
dataframe.to_csv(path,index=False,sep=',')
