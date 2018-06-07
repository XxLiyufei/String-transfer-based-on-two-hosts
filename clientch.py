#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: client.py
socket client
"""

import socket
import sys


def socket_client(): ##创建客户端
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET建立服务器间网络通信，socket.SOCK_STREAM为流式socket，for TCP
        s.connect(('192.168.125.139', 6666)) #连接到服务器，端口号为6666
    except socket.error as msg: 
        print msg
        sys.exit(1)
    print s.recv(1024)
    while 1:
        data = raw_input('请输入需要传输的字符: ')
        s.send(data) #发送数据
        print s.recv(1024)
        if data == 'exit':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
