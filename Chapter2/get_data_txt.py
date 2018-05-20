# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:30:30 2018

@author: 724719274@qq.com
"""

from urllib.request import urlopen

# 获取源数据
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# path为存储路径，可自由更改
save_path = r'C:\Users\Administrator\Desktop\ETPA\Chapter2\data.txt'

# 打开文件并写入数据后关闭文件,将该部分抽象成函数
def write_txt(target_url, save_path):
    data = urlopen(target_url)
    f = open(save_path,'w')  
    for line in data:
        f.write(line.decode('utf-8'))
    f.close()

# 将txt的字符串格式转化为列表    
def read_as_list(save_path):
    xList = []
    with open(save_path, 'r') as data:
        for line in data:
            row = line.strip().split(",")
            xList.append(row)
    return xList

