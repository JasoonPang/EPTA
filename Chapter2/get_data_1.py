# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:30:30 2018

@author: Administrator
"""

from urllib.request import urlopen

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urlopen(target_url)

f = open(r'C:\Users\Administrator\Desktop\新建文件夹\data.txt','w')
for line in data:
    f.write(line.decode('utf-8'))
f.close()
