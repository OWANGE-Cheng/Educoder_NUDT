#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:29
# @Author  : Owange Cheng
# @File    : 1.py

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

data_url = "/data/workspace/myshixun/step1/train.csv"
df = pd.read_csv(data_url)

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(df.iloc[:, 5:6])
X = imp.transform(df.iloc[:, 5:6])
####### Begin ########
# 数据转换
scaler = preprocessing.scale(X)
####### End ########
# 输出转换后的前6列数据
print(scaler[:6])
