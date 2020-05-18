
import socket

print("\nWelcome to the FTP server.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 20017
BUFFER_SIZE = 4096


class FTP_SERVER:
    def __init__(self, conn):
        self.conn = conn
        self.clntAddr = None

    def printClientMessage(self):
        """ print message from client """
        msg, self.clntAd= self.conn.recvfrom(BUFFER_SIZE)
        print("\nRecieved message: {}".format(msg))

    def echo(self,msg):
        """ echo message from client"""

        try:
            self.conn.sendto(msg, self.clntAddr)
            print("\n message echoed")

        except:
            print("\n message could not be echoed")

    def quit(self):
        self.conn.close()

    def start(self):

        while True:
            cmd, self.clntAddr  = self.conn.recvfrom(BUFFER_SIZE)
         
            if cmd == "QUIT":
                self.quit()
                break
            else:
                self.echo(cmd)


# main program
commandSocket = socket.socket(type=socket.SOCK_DGRAM)
commandSocket.bind((TCP_IP, TCP_PORT))
client = FTP_SERVER(commandSocket)
client.start()
