import socket
import os

print("\nWelcome to the FTP server.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 20010
BUFFER_SIZE = 4096


class FTP_SERVER:
    def __init__(self, conn):
        self.conn = conn

    def echo(self,msg):
        """ echo message from client"""
        try:
            self.conn.send(msg)

        except:
            print("\n message could not be echoed")


    def start(self):

        while True:
            cmd = self.conn.recv(BUFFER_SIZE)

            if cmd == "QUIT":
                self.quit()
                break
            else :
                self.echo(cmd)


# main program
commandSocket = socket.socket()
commandSocket.bind((TCP_IP, TCP_PORT))
commandSocket.listen(1)
CONN, clientControlAddress = commandSocket.accept()

print("\nConnected to by client address: {}".format(clientControlAddress))  # IP address for client

client = FTP_SERVER(CONN)
client.start()
CONN.close()
