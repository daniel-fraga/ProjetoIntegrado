#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
# BIBLIOTECAS
import random
import socket, select
import threading 
from _thread import *
from time import gmtime, strftime
from random import randint


#informacoes importantes
BUFF = 1024
HOST = '' 
PORT = 5002 	

print_lock = threading.Lock() 

# funcao thread 
def threaded(c): 
	while True: 

		# recebido do cliente
		data = c.recv(BUFF) 
		if not data: 
			print('Bye') 
			
			# aberto na saida 
			print_lock.release() 
			break

		# envia pro cliente
		c.send(data) 

	# fecha conx
	c.close() 


def Main(): 
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
	s.close() 


if __name__ == '__main__': 
	Main() 

