import socket

print("\nWelcome to the FTP server.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 1026
BUFFER_SIZE = 4096


class FTP_SERVER:
    def __init__(self, conn):
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

    def quit(self):
        self.conn.close()

    def start(self):

        while True:
            cmd = self.conn.recvfrom(BUFFER_SIZE)[0]
            print(cmd)
            if cmd == "QUIT":
                self.quit()
                break
            elif cmd == "ECHO":
                self.echo()


# main program
commandSocket = socket.socket(type=socket.SOCK_DGRAM)
commandSocket.bind((TCP_IP, TCP_PORT))
client = FTP_SERVER(commandSocket)
client.start()
