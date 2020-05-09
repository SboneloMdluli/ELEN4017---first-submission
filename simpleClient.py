import socket

print("\nWelcome to the FTP client.")

SERVER_TCP_PORT = 1026
BUFFER_SIZE = 4096


class FTP_CLIENT:

    def __init__(self, conn):
        self.conn = conn

    def echomsg(self, msg):
        """ECHO message to server"""
        try:
            clntcmd = "ECHO"
            self.conn.send(clntcmd.encode())
        except:
            print("couldnt send cmd")

        try:
            self.conn.send(msg.encode())
            print("\n message sent")
            svrmag = self.conn.recv(BUFFER_SIZE)
            print("\nechoed message from the server: {}".format(svrmag))

        except:
            print("\n message could not be sent")

    def quit(self):
        clntcmd = "QUIT"
        self.conn.send(clntcmd.encode())

        self.conn.close()
        print("Stop connection")
        return

    def start(self):
        while True:
            # Listen for a command
            msg = raw_input("\nEnter a message: ")

            if msg[:4].upper() == "ECHO":
                print("..............")
                self.echomsg(msg[5:])
            elif msg[:4] == "QUIT":
                self.quit()
                break


# main program
s = socket.socket()
hostname = socket.gethostname()
SERVER_TCP_IP = socket.gethostbyname(hostname)
print("\nConnected to by sever: {}".format(SERVER_TCP_IP))  # IP address for client
s.connect((SERVER_TCP_IP, SERVER_TCP_PORT))
serverInterface = FTP_CLIENT(s)
serverInterface.start()