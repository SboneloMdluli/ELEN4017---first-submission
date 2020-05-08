import socket

print("\nWelcome to the FTP client.")

SERVER_TCP_PORT = 1026
BUFFER_SIZE = 4096

class FTP_CLIENT:

    def __init__(self, conn):
        self.conn = conn

    def sendmsg(self, msg):
        try:
            self.conn.send(msg)
            print("\n message sent")
        except:
            print("\n message could not be sent")


# main program
s = socket.socket()
hostname = socket.gethostname()
SERVER_TCP_IP = socket.gethostbyname(hostname)
s.connect((SERVER_TCP_IP, SERVER_TCP_PORT))
serverInterface = FTP_CLIENT(s)

print("\nConnected to by sever: {}".format(SERVER_TCP_IP))  # IP address for client

msg = raw_input("\nEnter a message: ")
serverInterface.sendmsg(msg)
