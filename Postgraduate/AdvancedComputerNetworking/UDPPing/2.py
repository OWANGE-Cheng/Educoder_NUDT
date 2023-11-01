#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:32
# @Author  : Owange Cheng
# @File    : 2.py

from socket import *

# 创建UDP套接字
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 绑定本机IP地址和端口号
serverSocket.bind(('127.0.0.1', 12000))

########## Begin ##########
# 接收客户端消息
message, address = serverSocket.recvfrom(1024)
# 将数据包消息转换为大写
message = message.upper()
# 将消息传回给客户端
serverSocket.sendto(message, address)
########## End ##########
