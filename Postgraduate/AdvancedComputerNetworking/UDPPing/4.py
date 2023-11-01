#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:35
# @Author  : Owange Cheng
# @File    : 4.py


from socket import *

########## Begin ##########
# 创建UDP套接字，使用IPv4协议
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置套接字超时值1秒
clientSocket.settimeout(1)
########## End ##########

print(clientSocket)
print(clientSocket.gettimeout())
