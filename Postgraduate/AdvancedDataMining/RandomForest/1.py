#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:00
# @Author  : Owange Cheng
# @File    : 1.py

# 导入相关库
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import numpy as np

# 下载数据集
iris = load_iris()
X = iris["data"]
y = iris["target"]

np.random.seed(0)
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 创建 RandomForestClassifier 对象
########## Begin ##########
clf = RandomForestClassifier()
##########  End  ##########

# 调用 fit 函数执行训练过程
clf.fit(X_train, y_train)

# 打印结果
print('训练集准确率：', accuracy_score(y_train, clf.predict(X_train)))
print('测试集准确率：', accuracy_score(y_test, clf.predict(X_test)))
