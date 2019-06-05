#programa main (base) que executa outros programas necessarios (servidor-5002 e ocr)

import threading
from _thread import *
import sys
sys.path.insert(0, '/home/daniel/Desktop/ProjetoIntegrado/Servidor')
sys.path.insert(0, '/home/daniel/Desktop/ProjetoIntegrado/OCR')



import servinho
#import ocr

if __name__ == '__main__':
    
    #criacao de thread do servidor
    threadsrv = threading.Thread(target = servinho.main)
    threadsrv.start()
    #criacao de thread do OCR (bug no tesseract)
    #threadocr = threading.Thread(target = ocr.main)
    #threadocr.start()

    #servinho.main()
    #ocr.main()
