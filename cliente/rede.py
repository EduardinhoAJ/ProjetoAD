#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Tem a class TCPSocketCliente que tem por si a função enviar comando, que dá a funcionalidade de conectar ao servidor e enviar mensagens com tamanaho maximo explicito

import socket


class TCPSocketCliente:
    """
    Camada Transporte:
    - apenas cria socket 
    - mantem a ligação aberta
    - fecha com input do utilizador
    """


    

    def __init__(self, host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def fechar_ligação(self):
        self.sock.close()
