#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:51
# @Author  : Owange Cheng
# @File    : 1.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler

np.random.seed(0)
# 构建数据
n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
data_sets = [(noisy_circles, {"n_clusters": 2}),
             (noisy_moons, {"n_clusters": 2}),
             (blobs, {"n_clusters": 3})]
colors = ["#377eb8", "#ff7f00", "#4daf4a"]
linkage_list = ['single', 'average', 'complete', 'ward']
plt.figure(figsize=(20, 15))
for i_dataset, (dataset, algo_params) in enumerate(data_sets):
    # 模型参数
    params = algo_params
    # 数据
    X, y = dataset
    X = StandardScaler().fit_transform(X)
    for i_linkage, linkage_strategy in enumerate(linkage_list):
        ########## Begin ##########
        # 创建AgglomerativeCluster
        ac = cluster.AgglomerativeClustering(n_clusters=params['n_clusters'], linkage=linkage_strategy)
        # 训练
        ac.fit(X)
        # 预测
        y_pred = ac.labels_.astype(int)
        print(y_pred)
        ########## End ##########
        y_pred_colors = []
        for i in y_pred:
            y_pred_colors.append(colors[i])
        plt.subplot(3, 4, 4 * i_dataset + i_linkage + 1)
        ########## Begin ##########
        # 可视化层次聚类结果
        plt.title(linkage_strategy)
        plt.scatter(X[:, 0], X[:, 1], color=y_pred_colors)
        ########## End ##########
plt.show()
plt.savefig("/data/workspace/myshixun/step1/output/img.png")
