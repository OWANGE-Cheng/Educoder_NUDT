#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:04
# @Author  : Owange Cheng
# @File    : 1.py

# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
########## Begin ##########
serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen(1)
########## End ##########
print(serverSocket)
serverSocket.close()
