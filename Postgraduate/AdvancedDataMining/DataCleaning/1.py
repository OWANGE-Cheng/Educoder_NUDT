#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:17
# @Author  : Owange Cheng
# @File    : 1.py

import numpy as np
import pandas as pd

# 读取数据
df = pd.read_csv('/data/workspace/myshixun/step1/train.csv')

##### begin #####
# 查看列中是否存在空值
temp = df.isnull().any()
print(temp)
# 使用SimpleImputer取出缺失值所在列的数值，sklearn当中特征矩阵必须是二维才能传入 使用reshape(-1,1)升维
age = df['Age'].values.reshape(-1, 1)
# 导入模块
from sklearn.impute import SimpleImputer
# 实例化，均值填充,可改变strategy参数，实现其他填充方式
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
# fit_transform一步完成调取结果
imp = imp.fit_transform(age)
# 填充好的数据传回到 data['Age']列df_fillna=df
df_f = df
df_f['Age'] = imp
# 检验是否还有空值，为0即说明空值均已被填充
print(df_f['Age'].isnull().sum())
##### end #####


imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean = imp_mean.fit_transform(age)
df_fillna = df
df_fillna['Age'] = imp_mean

# 正太分布离群点检测
##### begin #####
# 计算均值
u = df['Age'].mean()
# 计算标准差
std = df['Age'].std()
# 识别异常值
error = df[np.abs(df['Age'] - u) > 3 * std]
##### end #####
print(error)
