import socket
import threading
from _thread import *
import cv2
import base64

#informacoes importantes
BUFF = 53136
HOST = ''
PORT = 5002
view = memoryview(bytearray(53136))
print_lock = threading.Lock()


def threaded(c):
    while True:
        data = c.recv_into(view, BUFF)

        fh = open("image.jpeg", "wb")
        fh.write(base64.b64decode(view))
        fh.close()
        print(len(view))
        mat = cv2.imread("image.jpeg")

        if not data:
            print('Bye')

            print_lock.release()
            break
        cv2.imshow("Tsete", mat)
        cv2.waitKey(0)

    c.close()


def main():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        print("socket binded to post", PORT)

        # socket escuando
        s.listen(5)
        print("socket is listening")

        # loppzao
        while True:

                # aceita a conexao
                c, addr = s.accept()

                # cliente no loop lock.acquire
                print_lock.acquire()
                print('Connected to :', addr[0], ':', addr[1])

                # nova thread
                start_new_thread(threaded, (c,))


if __name__ == '__main__':
        main()
