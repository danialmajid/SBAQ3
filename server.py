import socket
import threading
import random

# list of quotes
quotes = ["Be Yourself.", "No Pain No Gain.", "24434, Rakaat solat in a day."]

def handle_client(client_socket):

# receive data from client
    request = client_socket.recv(1024).decode()
    print(f'Received {request}')
    # send quote of the day to client
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

def main():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind(("", 8888))

        server_socket.listen(5)

        while True:
                client_socket, address = server_socket.accept()
                print("[*] Accepted connection from {}:{}".format(address[0], address[1]))
                client_handler = threading.Thread(target=handle_client, args=(client_socket,))
                client_handler.start()

if __name__ == '__main__':
    main()
