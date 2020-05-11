import socket
import threading

print("\nWelcome to the FTP server.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 1026
BUFFER_SIZE = 4096


class threadedSERVER(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.clntAddr = None

    def printClientMessage(self):
        """ print message from client """
        msg, self.clntAddr = self.conn.recvfrom(BUFFER_SIZE)
        print("\nRecieved message: {}".format(msg))

    def echo(self):
        """ echo message from client"""
        msg, self.clntAddr = self.conn.recvfrom(BUFFER_SIZE)

        try:
            self.conn.sendto(msg, self.clntAddr)
            print("\n message echoed")

        except:
            print("\n message could not be echoed")

    def run(self):
        runserver()

    def quit(self):
        self.conn.close()

    def runserver(self):

        while True:
            cmd = self.conn.recvfrom(BUFFER_SIZE)[0]
            if cmd == "QUIT":
                self.quit()
                break
            else:
                self.echo()


# main program
commandSocket = socket.socket(type=socket.SOCK_DGRAM)
commandSocket.bind((TCP_IP, TCP_PORT))
threadedClient = threadedSERVER(commandSocket)
threadedClient.start()