#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:09
# @Author  : Owange Cheng
# @File    : 3.py

# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(("127.0.0.1", 6789))
serverSocket.listen(1)

# while True:
print('开始WEB服务...')

try:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)  # 获取客户发送的报文

    # 读取文件内容
    ######### Begin #########
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = f.read()
    ######### End #########
    print(outputdata)
    connectionSocket.close()
except IOError:

    connectionSocket.close()
serverSocket.close()
