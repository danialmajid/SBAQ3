import socket


def Main():
        host = '192.168.56.102'
        port = 8888

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))

        message = "Quote of the day sent to client "
        for i in range(1):

                s.send(message.encode())

                data = s.recv(1024)

                print('Quote of the day from server : ',str(data.decode('ascii')))

        s.close()

if __name__ == '__main__':
        Main()
