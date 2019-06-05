import socket
import base64


def main():
    HOST = 'localhost'
    PORT = 5002
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        img = open("./../testeocr/magic.jpeg", "rb")
        str = base64.b64encode(img.read())
        print(len(str))
        sock.connect((HOST, PORT))
        flag = sock.sendall(str)

        if flag == None:
            print("Sucess")
    except:
        print("Cannot connect to the server")


if __name__ == main():
    main()
