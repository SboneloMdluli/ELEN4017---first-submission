from socket import *
import threading

exitFlag = 0
BUFFER_SIZE = 4096
SERVER_PORT = 20072
print("The server is ready to receive")

class myThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn


    def run(self):

        self.echomsg()


    def echomsg(self):
        while True:
            msg = self.conn.recv(BUFFER_SIZE).decode()
            if msg == 'close':
                break
            else:
                self.conn.send(msg.encode())


# Setup

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', SERVER_PORT))

threads = []

while True:

    serverSocket.listen(5)
    CONN, addr = serverSocket.accept()
    thread_ = myThread(CONN)
    thread_.start()
    threads.append(thread_)

    # connectionSocket.close()

# Join threads in conclusion
for thread_ in threads:
    thread_.join()

CONN.close()