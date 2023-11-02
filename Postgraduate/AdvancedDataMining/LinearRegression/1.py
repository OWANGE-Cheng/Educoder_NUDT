#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 16:09
# @Author  : Owange Cheng
# @File    : 1.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def data_astype(x):
    """数据类型转换"""
    x['hour'] = x['hour'].astype('float32')
    x['DEWP'] = x['DEWP'].astype('float32')
    x['TEMP'] = x['TEMP'].astype('float32')
    x['PRES'] = x['PRES'].astype('float32')
    x['Iws'] = x['Iws'].astype('float32')
    x['Is'] = x['Is'].astype('float32')
    x['Ir'] = x['Ir'].astype('float32')
    x['cbwd_NE'] = x['cbwd_NE'].astype('float32')
    x['cbwd_NW'] = x['cbwd_NW'].astype('float32')
    x['cbwd_SE'] = x['cbwd_SE'].astype('float32')
    x['cbwd_cv'] = x['cbwd_cv'].astype('float32')
    x['year'] = x['year'].astype('float32')
    x['month'] = x['month'].astype('float32')
    x['day'] = x['day'].astype('float32')
    x['week'] = x['week'].astype('float32')


if __name__ == "__main__":
    # 加载数据
    x = pd.read_csv('src/step1/data/pm25_data.csv', encoding='utf-8')
    data_astype(x)
    # 加载标签
    y = pd.read_csv('src/step1/data/result.csv')['pm2.5']

    # 对数据进行线性回归预测
    #####Begin#####
    reg = LinearRegression()
    reg.fit(x, y)
    #####End#####

    # 加载未来18天的数据
    x_val = pd.read_csv('src/step1/data/test_1.csv')
    # 预测
    y_val_pre = reg.predict(x_val)
    print('未来18天的pm25预测值：', y_val_pre)
