import socket

print("\nWelcome to the FTP server.")

TCP_IP = "127.0.1.1"  # local address
TCP_PORT = 1026
BUFFER_SIZE = 4096


class FTP_SERVER:
    def __init__(self, conn):
        self.conn = conn

    def echo(self):

        try:
            self.conn.send(msg.encode())
            print("\n message echoed")

        except:
            print("\n message could not be echoed")

    def start(self):
        self.echo()
        self.conn.close()

    def echomsg(self):
        while True:
            msg = self.conn.recv(BUFFER_SIZE).decode()
            if msg == 'close':
                break
            else:
                self.conn.send(msg.encode())


# main program
commandSocket = socket.socket()
commandSocket.bind((TCP_IP, TCP_PORT))
commandSocket.listen(1)
CONN, clientControlAddress = commandSocket.accept()

print("\nConnected to by client address: {}".format(clientControlAddress))  # IP address for client

client = FTP_SERVER(CONN)
client.start()