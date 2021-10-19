import socket
import numpy
import time
import base64
import sys


def receiveAll(sock, count):
    buf = b''
    while count:
        try:
            newbuf = sock.recv(count)
        except socket.timeout:
            return None
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def clearBuffer(sock):
    sock.settimeout(0.1)
    while True:
        try:
            sock.recv(1000)
        except socket.timeout:
            break
    sock.settimeout(0.5)


class Connector:

    def __init__(self, ip, port):
        self.notReceived_Before = False
        self.sock = socket.socket()
        self.TCP_SERVER_IP = ip
        self.TCP_SERVER_PORT = port
        self.connectCount = 0
        self.sock.settimeout(0.5)
        self.connectServer()

    def connectServer(self):
        try:
            self.sock.connect((self.TCP_SERVER_IP, self.TCP_SERVER_PORT))
            print(
                u'Client socket is connected with Server socket [ TCP_SERVER_IP: ' + self.TCP_SERVER_IP
                + ', TCP_SERVER_PORT: ' + str(self.TCP_SERVER_PORT) + ' ]')
            self.connectCount = 0
        except Exception as e:
            print(e)
            self.connectCount += 1
            if self.connectCount == 10:
                print(u'Connect fail %d times. exit program' % self.connectCount)
                sys.exit()
            print(u'%d times try to connect with server' % self.connectCount)
            self.connectServer()

    def processing(self, image):
        try:
            data = numpy.array(image)
            stringData = base64.b64encode(data)
            length = str(len(stringData))

            if self.notReceived_Before:
                clearBuffer(self.sock)

            self.sock.sendall(length.encode('utf-8').ljust(64))
            self.sock.send(stringData)

            result_len = receiveAll(self.sock, 66)
            result_len = result_len.decode('utf-8')

            if result_len is None:
                self.notReceived_Before = True
                return None

            result = receiveAll(self.sock, int(result_len))

            if len(result) == 0:
                return None

            result = numpy.frombuffer(base64.b64decode(result), numpy.uint8)
            return result

        except Exception as e:
            print(e)
            self.sock.close()
            time.sleep(1)
            self.connectServer()
            self.processing()
