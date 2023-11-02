#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:58
# @Author  : Owange Cheng
# @File    : 1.py

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


def test_m():
    data_url = "/data/workspace/myshixun/home/diabetes.csv"
    df = pd.read_csv(data_url)
    Xa = df.iloc[:, 0:8]
    ya = df.iloc[:, 8]
    X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(Xa, ya, test_size=0.2, random_state=0)
    # 利用MLPClassifier函数制作神经网络
    # 使用solver,hidden_layer_sizes,random_state等参数
    # 'sgd’指的是随机梯度下,使用10个隐藏层5个输出层,随机数为1
    ###########Begin###########
    clf = MLPClassifier(solver='sgd', hidden_layer_sizes=(10, 5), random_state=1)
    clf.fit(X_train_1, y_train_1)
    ###########End#############

    return accuracy_score(y_train_1, clf.predict(X_train_1)), accuracy_score(y_test_1, clf.predict(X_test_1))
