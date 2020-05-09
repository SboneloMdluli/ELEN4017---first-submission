import socket
import os

print("\nWelcome to the FTP server.")

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

    def echo(self):
        """ echo message from client"""
        msg = self.conn.recv(BUFFER_SIZE)
        try:
            self.conn.send(msg)
            print("\n message echoed")

        except:
            print("\n message could not be echoed")

    def quit(self):
        self.conn.close()


    def start(self):

        while True:
            cmd = self.conn.recv(BUFFER_SIZE)
            print(cmd)
            if cmd == "QUIT":
                self.quit()
                break
            elif cmd == "ECHO":
                self.echo()


# main program
commandSocket = socket.socket()
commandSocket.bind((TCP_IP, TCP_PORT))
commandSocket.listen(1)
CONN, clientControlAddress = commandSocket.accept()

print("\nConnected to by client address: {}".format(clientControlAddress))  # IP address for client

client = FTP_SERVER(CONN)
client.start()
