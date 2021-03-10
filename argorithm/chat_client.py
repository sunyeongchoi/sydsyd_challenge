# 5번 - client
# 참조 : https://lidron.tistory.com/44

import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 5000

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            if msg == '/quit':
                sock.send(msg.encode())
                break
            sock.send(msg.encode())
runChat()

