#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:30
# @Author  : Owange Cheng
# @File    : 1.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_csv = '/data/workspace/myshixun/step1/pm25_data.csv'
train_data = pd.read_csv(train_csv)
train_data.drop(['hour'], axis=1, inplace=True)
f, ax = plt.subplots(figsize=(12, 8))
####### Begin #######
# 计算相关系数矩阵
corrmat = train_data.corr()
# 颜色取值的最大值0.8,使每个单元格为方形
sns.heatmap(corrmat, vmax=0.8, square=True)
####### End #######
# 输出矩阵
print(corrmat)
# 保存热力图
plt.savefig("/data/workspace/myshixun/step1/学员文件/corrmat.png")
