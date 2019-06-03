import socket


def main():
    HOST = 'projintegrado.ddns.net'
    PORT = 5002
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        img =
        bytes = 
        sock.sendall(bytes,)
    except:
        print("Cannot connect to the server")


if __name__ == main():
    main()

