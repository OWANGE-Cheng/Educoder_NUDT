#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:06
# @Author  : Owange Cheng
# @File    : 2.py

# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(("127.0.0.1", 6789))
serverSocket.listen(1)

# while True:
# Establish the connection
print('开始WEB服务...')

try:
    ########## Begin ##########
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    ########## End ##########
    print(addr[0])
    print(message)
    connectionSocket.close()
except IOError:
    connectionSocket.close()

serverSocket.close()
