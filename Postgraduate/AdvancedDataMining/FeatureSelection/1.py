#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/2 18:33
# @Author  : Owange Cheng
# @File    : 1.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def test():
    data_url = "/data/workspace/myshixun/step1/train.csv"
    df = pd.read_csv(data_url)
    S = df[df.Survived == 1]
    D = df[df.Survived == 0]
    # 绘制根据S、D的前9列数据绘制直方图
    ########## Begin ##########
    plt.hist(S.iloc[:, 9])
    plt.hist(D.iloc[:, 9])
    ########## End ##########
    plt.savefig('/data/workspace/myshixun/step1/picture2/直方图.png')

    # sex = df.groupby('Sex')['Survived'].sum()
    # 绘制柱状图
    sexNew = df.groupby(['Sex', 'Survived'])['Survived'].count().unstack()
    ########## Begin ##########
    sexNew.plot(kind='bar')
    ########## End ##########

    plt.savefig('/data/workspace/myshixun/step1/picture2/柱状图.png')
    plt.show()

    img1 = mpimg.imread('/data/workspace/myshixun/step1/picture2/直方图.png')
    img2 = mpimg.imread('/data/workspace/myshixun/step1/picture2/柱状图.png')

    plt.subplot(121), plt.imshow(img1)
    plt.subplot(122), plt.imshow(img2)
    plt.savefig("/data/workspace/myshixun/step1/picture2/特征选择.png")
