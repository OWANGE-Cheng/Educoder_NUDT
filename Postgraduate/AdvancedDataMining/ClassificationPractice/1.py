#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:32
# @Author  : Owange Cheng
# @File    : 1.py

import sklearn
# 导入高斯朴素贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


def knn_test():
    data_url = "/data/workspace/myshixun/step1/iris_train.csv"
    df = pd.read_csv(data_url)
    X = df.iloc[:, 1:4]
    y = df.iloc[:, 4]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # 使用高斯朴素贝叶斯进行计算
    ######## Begin ########
    clf = GaussianNB()
    ######## End ########
    clf.fit(X_train, y_train)
    # 评估
    y_pred = clf.predict(X_test)
    acc = np.sum(y_test == y_pred) / X_test.shape[0]
    return acc
