#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:56
# @Author  : Owange Cheng
# @File    : 1.py

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


def knn_test():
    data_url = "/data/workspace/myshixun/home/iris_train.csv"
    df = pd.read_csv(data_url)
    X = df.iloc[:, 1:4]
    y = df.iloc[:, 4]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # 利用KNeighborsClassifier函数制作knn分类器
    # 选取最近的点的个数n_neighbors=3
    ###########Begin###########

    clf = KNeighborsClassifier(n_neighbors=3)

    ###########End#############
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = np.sum(y_test == y_pred) / X_test.shape[0]

    return acc
