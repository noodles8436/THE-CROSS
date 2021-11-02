import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='THE-CROSS DetectorServer arg parser')
    parser.add_argument('--ip', type=str, help='Input Detection Server IP\n ex) 127.0.0.1',
                        default='localhost', required=False)
    parser.add_argument('--port', type=int, help='Input Detection Server Port\n ex) 7777',
                        default=7777, required=False)

    args = parser.parse_args()

    IP = args.ip
    PORT = args.port

    print('\n\n ==============================================\n'
          ' Initializing THE-CROSS DETECTOR SERVER PROGRAM\n',
          'Detector Server IP : ', IP, "\n",
          'Detector Server PORT : ', PORT, '\n',
          '==============================================\n\n',
          '*** It takes a long time, so please wait. ***\n\n')

    from DetectorServer import DetectorServer
    server = DetectorServer(IP, PORT)
