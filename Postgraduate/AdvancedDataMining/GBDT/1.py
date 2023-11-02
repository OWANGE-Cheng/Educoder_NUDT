#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:04
# @Author  : Owange Cheng
# @File    : 1.py

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb


def gbc_t():
    data_url = "/data/workspace/myshixun/home/iris_train.csv"
    df = pd.read_csv(data_url)
    X = df.iloc[:, 1:4]
    y = df.iloc[:, 4]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # GradientBoostingClassifier:分类
    # 预估值100,学习率1,最大深度1,随机数0
    ###########Begin###########
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    ###########End#############
    clf.fit(X_train, y_train)
    acc_train = accuracy_score(y_train, clf.predict(X_train))
    acc_test = accuracy_score(y_test, clf.predict(X_test))
    return acc_train, acc_test


def make_p():
    train_csv = '/data/workspace/myshixun/home/train.csv'
    train_data = pd.read_csv(train_csv)
    train_data.drop(['Name', 'Sex', 'Ticket', 'Embarked', 'Cabin'], axis=1, inplace=True)
    train_data['Age'] = train_data['Age'].fillna(0)

    X = train_data.iloc[:, 0:6]
    y = train_data.iloc[:, 6]
    X_train, X_val, y_train, y_val = train_test_split(X.astype(float), y.astype(float), test_size=0.2, random_state=42)
    # make_pipeline(StandardScaler(),SGDRegressor())回归,参数默认就好
    ###########Begin###########
    reg = make_pipeline(StandardScaler(), SGDRegressor())
    ###########End#############
    reg.fit(X_train, y_train)
    y_val_pre = reg.predict(X_val)

    return mean_squared_error(y_val, y_val_pre)


def XGB_t():
    data_url = "/data/workspace/myshixun/home/iris_train.csv"
    df = pd.read_csv(data_url)
    X = df.iloc[:, 1:4]
    y = df.iloc[:, 4]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # XGBClassifier分类
    ###########Begin###########
    clf = XGBClassifier()
    ###########End#############
    clf.fit(X_train, y_train)
    acc_train = accuracy_score(y_train, clf.predict(X_train))
    acc_test = accuracy_score(y_test, clf.predict(X_test))

    return acc_train, acc_test


def xbg_r():
    train_csv = '/data/workspace/myshixun/home/train.csv'
    train_data = pd.read_csv(train_csv)

    train_data.drop(['Name', 'Sex', 'Ticket', 'Embarked', 'Cabin'], axis=1, inplace=True)
    train_data['Age'] = train_data['Age'].fillna(0)
    X = train_data.iloc[:, 0:6]
    y = train_data.iloc[:, 6]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    # XGBRegressor
    # 最大深度5,学习率0.1,预估160,objective='reg:linear'
    ###########Begin###########
    reg = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, objective='reg:linear')
    ###########End#############
    reg.fit(X_train, y_train)
    y_val_pre = reg.predict(X_val)

    return mean_squared_error(y_val, y_val_pre)
