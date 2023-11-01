#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 15:38
# @Author  : Owange Cheng
# @File    : 5.py

from socket import *
import time

serverName = '127.0.0.1'  # 服务器地址，本例中使用本机地址
serverPort = 12000  # 服务器指定的端口
clientSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字，使用IPv4协议
clientSocket.settimeout(1)  # 设置套接字超时值1秒

for i in range(0, 9):
    sendTime = time.time()
    message = ('Ping %d %s' % (i + 1, sendTime)).encode()  # 生成数据报，编码为bytes以便发送

    try:

        ########## Begin ##########
        # 将信息发送到服务器
        clientSocket.sendto(message, (serverName, serverPort))
        # 从服务器接收信息，同时也能得到服务器地址
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        ########## End ##########

        rtt = time.time() - sendTime  # 计算往返时间
        print('Sequence %d: Reply from %s    RTT = %.3fs' % (i + 1, serverName, rtt))  # 显示信息
    except Exception as e:
        print('Sequence %d: Request timed out.' % (i + 1))

clientSocket.close()  # 关闭套接字
