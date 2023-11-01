#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:29
# @Author  : Owange Cheng
# @File    : 1.py

from socket import *

########## Begin ##########

serverSocket = socket(AF_INET, SOCK_DGRAM)
host = '0.0.0.0'
port = 12000
serverSocket.bind((host, port))

########## End ##########

print(serverSocket)
