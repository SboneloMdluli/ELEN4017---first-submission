import socket

print("\nWelcome to the FTP client.")

TCP_IP = "127.0.1.1"  # local address
SERVER_TCP_PORT = 20010
BUFFER_SIZE = 4096


class FTP_CLIENT:

    def __init__(self, conn):
        self.conn = conn

    def echomsg(self, msg):
        """ECHO message to server"""

        try:
            self.conn.send(msg.encode())
            print("\n message sent")
            svrmag = self.conn.recv(BUFFER_SIZE).decode()
            print("\nechoed message from the server: {}".format(svrmag))

        except:
            print("\n message could not be sent")

    def quit(self):
        self.conn.close()
        print("Stop connection")


    def start(self):
        while True:
            # Listen for a command
            msg = input("Enter a message: ")

            if msg == "QUIT":
                self.quit()
                break
            else:
                self.echomsg(msg)


# main program
s = socket.socket()
hostname = socket.gethostname()
SERVER_TCP_IP = socket.gethostbyname(hostname)
print("\nConnected to by sever: {}".format(SERVER_TCP_IP))  # IP address for client
s.connect((SERVER_TCP_IP, SERVER_TCP_PORT))
serverInterface = FTP_CLIENT(s)
serverInterface.start()