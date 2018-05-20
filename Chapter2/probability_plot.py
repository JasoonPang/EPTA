# -*- coding: utf-8 -*-
"""
Created on Sun May 20 13:26:07 2018

@author: 724719274@qq.com
"""

import pylab
import scipy.stats as stats
import get_data_txt as gt

path = gt.save_path

# 将txt的字符串格式转化为列表
xList = gt.read_as_list(path)

# 将col列的数据取出来
col = 5
colData = []
for row in xList:
    colData.append(float(row[col]))

# 将取出的数据可视化
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()
