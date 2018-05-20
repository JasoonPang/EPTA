# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:10:42 2018

@author: Administrator
"""

from urllib.request import urlopen
import pandas as pd

# 获取源数据
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urlopen(target_url)

# 数据存储路径
path = r'C:\Users\Administrator\Desktop\ETPA\Chapter2\data_ist.csv'

# 将数据遍历写入列表
xList = []
for line in data:
    #split on comma
    row = line.decode('utf-8').strip().split(",")
    xList.append(row)

# 利用pandas将列表数据写入csv文件
dataframe = pd.DataFrame(xList)
dataframe.to_csv(path,index=False,sep=',')
