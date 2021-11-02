import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='THE-CROSS Client arg parser')
    parser.add_argument('--ip', type=str, help='Input Detection Server IP\n ex) 127.0.0.1',
                        default='localhost', required=False)
    parser.add_argument('--port', type=int, help='Input Detection Server Port\n ex) 7777',
                        default=7777, required=False)

    args = parser.parse_args()

    IP = args.ip
    PORT = args.port

    print('\n\n ==================== [ THE CROSS CLIENT ] ====================\n'
          '            - Initializing THE-CROSS CLIENT PROGRAM\n',
          '           - Detector Server IP : ', IP, "\n",
          '           - Detector Server PORT : ', PORT, '\n',
          '==============================================================\n\n',
          '========================= [!CAUTION!] ========================\n',
          '>>> DONT CLOSE PROGRAM UNTIL SUCCESSFULLY CAMERA CONNECTED <<<\n',
          '==============================================================\n\n')


    import main
    main.start(IP, PORT)
