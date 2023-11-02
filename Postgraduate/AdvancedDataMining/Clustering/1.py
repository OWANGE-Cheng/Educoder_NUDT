#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:47
# @Author  : Owange Cheng
# @File    : 1.py

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import pandas as pd


def Kmeans(data_url):
    """k-means"""
    df1 = pd.read_csv(data_url)
    X1 = df1.iloc[:, 1:5]
    # 构造k-means聚类器,类别为3,随机状态为9
    #####Begin#####
    estimator = KMeans(n_clusters=3, random_state=9)
    #####End#####
    return estimator.fit_predict(X1)


def Hcluster(data_url):
    """hcluster"""
    df2 = pd.read_csv(data_url)
    X2 = df2.iloc[:, 1:5]

    # 构造hcluster聚类器,类别为3
    #####Begin#####
    clustering = AgglomerativeClustering(n_clusters=3)
    #####End#####
    return clustering.fit_predict(X2)


if __name__ == '__main__':
    data_url = "src/step1/data/iris_train.csv"
    result1 = Kmeans(data_url)
    print('K-means:', result1)
    result2 = Hcluster(data_url)
    print('hcluster:', result2)
