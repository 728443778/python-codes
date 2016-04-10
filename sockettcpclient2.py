#-*- coding:utf-8 -*-
"""
author:侯成华
email:728443778@qq.com
时间:2016年4月10日16:55:41
描述:主要用于测试，该python程序 有2个线程，主线程为写线程，副线程为读线程
另外，我学习python也是在1年前还没到成都的时候，在工作中几乎没用过python，我是一名php开发者，
如果大家对代码有什么建议的地方，请指正
"""
import socket
from sys import argv
import threading
from time import ctime,sleep

argc = len(argv)
host = '0.0.0.0'
port = 80

def recvThread(socket):
    while True:
        data = socket.recv(1024)
        if data:
            sleep(0.1)
            print ctime(), 'revc server send data:',data

if (argc < 3):
    host = None
    port = None
    while not host:
        host = raw_input('please input server ip or hostname>')
    while not port:
        port = raw_input('please input server port>')
else :
    host = argv[1]
    port = argv[2]

port = int(port)
tcpSocket = None
try:
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    threading.Thread.daemon = True
    tcpSocket.connect((host, port))
    threadRead = threading.Thread(target=recvThread, args=(tcpSocket,))
    threadRead.start()
    while True:
        data = raw_input('input send server data>')
        if not data:
            continue
        tcpSocket.send(data)
        sleep(0.3)
except BaseException,e:
    print 'catch some exception:'
    raise e
finally:
    if tcpSocket:
        tcpSocket.close()
     