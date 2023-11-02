#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:49
# @Author  : Owange Cheng
# @File    : 1.py

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd


def Dbscan(data_url):
    """DBSCAN"""
    df = pd.read_csv(data_url)
    X = df.iloc[:, 1:5]
    X = StandardScaler().fit_transform(X)

    # 构造DBSCAN聚类器，设置半径为1，最小样本量为5
    #####Begin#####
    db = DBSCAN(eps=1, min_samples=5).fit(X)
    #####End#####
    return db.labels_


if __name__ == '__main__':
    data_url = "src/step1/data/iris_train.csv"
    result = Dbscan(data_url)
    print('DBSCAN:', result)
