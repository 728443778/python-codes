#-*- coding:utf-8 -*-
"""
author:侯成华
email:728443778@qq.com
时间:2016年4月10日16:55:41
描述:主要用于测试，该python程序 有三个线程，一个主线程，一个读线程，还有一个写线程
"""
import socket
from sys import argv
import threading
from time import ctime,sleep

argc = len(argv)
host = '0.0.0.0'
port = 80
def writeThread(socket):
    data = None
    try :
        while True:
            data = raw_input('input send data>')
            if not data:
                continue
            socket.send(data)
            sleep(0.5)
    except KeyboardInterrupt:
        pass

def recvThread(socket):
    try :
        data = None
        while True:
            data = socket.recv(1024)
            if data:
                print ctime(), 'revc server send data:',data
                data = None
    except KeyboardInterrupt:
        pass
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
    tcpSocket.setblocking(0)
    tcpSocket.settimeout(None)
    tcpSocket.connect((host, port))
    threadWrite = threading.Thread(target=writeThread, args=(tcpSocket,))
    threadRead = threading.Thread(target=recvThread, args=(tcpSocket,))
    threadRead.start()
    sleep(1)
    threadWrite.start()
    threadWrite.join()
    threadRead.join()
    run = True
    while run:
        run = threadWrite.is_alive and threadRead.is_alive
except BaseException,e:
    print 'catch some exception:'
    raise e
finally:
    if tcpSocket:
        tcpSocket.close()