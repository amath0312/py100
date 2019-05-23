from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
from threading import Thread
from time import sleep

class ServerMessageHandler(Thread):
    def __init__(self, client, addr):
        super().__init__()
        self._client= client
        self._addr = addr
    def run(self):
        sleep(1)
        self._client.send(('hello %s' % str(self._addr)).encode('utf8'))
        self._client.close()

def server():
    ip = '127.0.0.1'
    port = 50001
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind((ip, port))
    server.listen(16)

    while True:
        client, addr = server.accept()
        print('%s 连接到了服务器' % str(addr))
        handler = ServerMessageHandler(client, addr)
        # handler.setDaemon(True)
        handler.start()


def client():
    client = socket()
    client.connect(('127.0.0.1', 50001))
    data = client.recv(1024).decode('utf8')
    print('接收到内容：', data)


def main():
    proc_server = Process(target=server)
    proc_server.start()
    sleep(1)
    for _ in range(10):
        Thread(target=client).start()

    proc_server.join()


if __name__ == '__main__':
    main()

