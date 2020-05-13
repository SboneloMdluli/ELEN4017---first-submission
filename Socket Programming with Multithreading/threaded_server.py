import socket

TCP_PORT = 11002
BUFFER_SIZE = 4096

serverSocket = socket.socket(type=socket.SOCK_DGRAM)
serverSocket.bind(('', TCP_PORT))
print("The server is ready to receive")

import threading
class myThread (threading.Thread):
    def __init__(self, svrmsg, address):
        threading.Thread.__init__(self)
        self.address = address
        self.sentence = svrmsg
    def run(self):
        echo(self.sentence, self.address)
        print("********************")

def echo(msg, clntAddr):

    try:
        print("\nmessage echoed")
        serverSocket.sendto(msg.encode(), clntAddr)

    except:
        print("\nmessage couldnt be echoed")

threads = []
while True:
    svrmsg, clntAddr = serverSocket.recvfrom(BUFFER_SIZE)
    thread1 = myThread(svrmsg,clntAddr)
    thread1.start()# only one thread is running here
    threads.append(thread1)

# Join threads in conclusion
for thread_ in threads:
    thread_.join()

CONN.close()