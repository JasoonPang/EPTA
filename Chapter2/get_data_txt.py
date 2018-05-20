# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:30:30 2018

@author: Administrator
"""

from urllib.request import urlopen

# 获取源数据
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urlopen(target_url)

# path为存储路径，可自由更改
path = r'C:\Users\Administrator\Desktop\ETPA\Chapter2\data.txt'

# 打开文件并写入数据后关闭文件
f = open(path,'w')  
for line in data:
    f.write(line.decode('utf-8'))
f.close()