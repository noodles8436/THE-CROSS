import socket
import numpy
import base64
import cv2
import json

import ImageDetector


def receiveAll(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class DetectorServer:

    def __init__(self, ip, port):
        self.TCP_IP = ip
        self.TCP_PORT = port
        self.folder_num = 0
        self.socketOpen()
        self.receiveImages()

    def socketClose(self):
        self.sock.close()
        print(u'Server socket [ TCP_IP: ' + self.TCP_IP + ', TCP_PORT: ' + str(self.TCP_PORT) + ' ] is close')

    def socketOpen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.TCP_IP, self.TCP_PORT))
        self.sock.listen(1)
        print(u'Server socket [ TCP_IP: ' + self.TCP_IP + ', TCP_PORT: ' + str(self.TCP_PORT) + ' ] is open')
        self.conn, self.addr = self.sock.accept()
        print(u'Server socket [ TCP_IP: ' + self.TCP_IP + ', TCP_PORT: ' + str(
            self.TCP_PORT) + ' ] is connected with client')

    def receiveImages(self):
        try:
            while True:
                length = receiveAll(self.conn, 64)
                if length is None:
                    continue
                length1 = length.decode('utf-8')
                stringData = receiveAll(self.conn, int(length1))
                data = numpy.frombuffer(base64.b64decode(stringData), numpy.uint8)
                img = cv2.imdecode(data, 1)
                result = self.processing(img)
                self.sendResult(result)

        except Exception as e:
            print(e)
            self.socketClose()
            self.socketOpen()
            self.receiveImages()

    # data must be numpy array
    def processing(self, data):
        _, pos_result = ImageDetector.Detector(data)
        _, custom_result = ImageDetector.CustomDetector(data)
        return [pos_result, custom_result]

    def sendResult(self, result):

        print('result-->', result)

        result_encoded_json = json.dumps(result).encode('utf-8')
        length = str(len(result_encoded_json))

        self.conn.sendall(length.encode('utf-8').ljust(64))
        self.conn.send(result_encoded_json)


def main():
    server = DetectorServer('localhost', 7777)


if __name__ == "__main__":
    main()
