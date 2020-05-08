import socket
import sys

print("\nWelcome to the FTP server.\n\nTo get started, connect a client.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 1026
BUFFER_SIZE = 4096

class FTP_SERVER:
    def __init__(self, conn):
        self.conn = conn

    def printClientMessage(self):
        """ print message from client """
        msg = self.conn.recv(BUFFER_SIZE)
        print("\nRecieved message: {}".format(msg))

    def start(self):
        self.printClientMessage()
        self.conn.close()


# main program
commandSocket = socket.socket()
commandSocket.bind((TCP_IP, TCP_PORT))
commandSocket.listen(1)
CONN, clientControlAddress = commandSocket.accept()

print("\nConnected to by client address: {}".format(clientControlAddress)) # IP address for client

client = FTP_SERVER(CONN)
client.start()
