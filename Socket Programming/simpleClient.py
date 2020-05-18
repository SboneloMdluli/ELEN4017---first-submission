import socket

print("\nWelcome to the FTP client.")

SERVER_TCP_IP = "127.0.1.1"  # local address
SERVER_TCP_PORT = 20017
BUFFER_SIZE = 4096

class FTP_CLIENT:

    def __init__(self, conn, SERVER_UDPADDR):
        self.conn = conn
        self.SERVER_UDPADDR = SERVER_UDPADDR

    def echomsg(self, msg):
        """ECHO message to server"""

        try:
            self.conn.sendto(str.encode(msg), SERVER_UDPADDR)
            print("\nmessage sent")
            svrmag = self.conn.recvfrom(BUFFER_SIZE)[0]
            print("\nechoed message from the server: {}".format(svrmag))
            print("\n-----------------------------------------")
        except:
            print("\n message could not be sent")

    def quit(self):
        self.conn.close()
        print("Stop connection")


    def start(self):
        while True:
            # Listen for a command
            msg = raw_input("\nEnter a message: ")

            if msg == "QUIT":
                self.quit()
                break
            else:
                self.echomsg(msg)


# main program
clientSocket = socket.socket(type=socket.SOCK_DGRAM)
SERVER_UDPADDR = (SERVER_TCP_IP,SERVER_TCP_PORT)
print("\nConnected to by sever: {}".format(SERVER_UDPADDR))  # IP address for client
serverInterface = FTP_CLIENT(clientSocket,SERVER_UDPADDR)
serverInterface.start()
