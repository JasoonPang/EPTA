# -*- coding: utf-8 -*-
"""
Created on Sun May 20 14:30:23 2018

@author: Administrator
"""

import pandas as pd
#from pandas import DataFrame
import matplotlib.pyplot as plt
import get_data_csv as gc

path = gc.save_path
# 读取数据，index_col为列索引，header为行索引，prefix可用作无列索引时补充
rocksVMines = pd.read_csv(path, index_col = 0)

## 打印头尾
#print(rocksVMines.head())
#print(rocksVMines.tail())
#
## 打印概要描述
#summary = rocksVMines.describe()
#print(summary)

# 将数据分布可视化
for i in range(208):
    if rocksVMines.iat[i, 60] == "M":
        pcolor = 'red'
    else:
        pcolor = 'blue'    
    dataRow = rocksVMines.iloc[i, 0 : 60]
    dataRow.plot(color = pcolor)

plt.xlim = (0, 60)
plt.xlabel('Attribute Index')
plt.ylabel('Attribute Values')
plt.show()
