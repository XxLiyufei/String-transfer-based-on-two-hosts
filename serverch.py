#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: service.py
socket service
"""


import socket #socket模块
import threading #threading模块
import time #time模块
import sys #sys模块


def socket_service(): #创建服务端
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.125.139', 6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print '等待连接...'

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr): #接收数据及显示数据
    print '接收到新连接来自 {0}'.format(addr)
    conn.send('欢迎进入本服务器')
    while 1:
        data = conn.recv(1024)
        print '{0} 接收到来自客户端的数据为 {1}'.format(addr, data)
        #time.sleep(1)
        if data == 'exit' or not data:
            print '{0} 连接关闭'.format(addr)
            conn.send('连接已关闭')
            break
        conn.send('已传送字符串为： {0}'.format(data))
    conn.close()


if __name__ == '__main__':
    socket_service()
