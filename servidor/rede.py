#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Contém a Class TCPSocketServidor que o main.py do servidor utiliza para criar a Socket do lado do Servidor
 

import socket
import pickle
import struct

class TCPSocketServidor:
    """
    Camada Transporte:
    - não interpreta comandos
    - não chama Loja
    - não faz validações de negócio
    - só move strings
    """


    def __init__(self, ponto_acesso):
        self.ponto_acesso = ponto_acesso

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind((ponto_acesso.endereco_ip, int(ponto_acesso.porto)))
        self.sock.listen()

        
    def receive_message(sock):
        data = sock.recv(4096)
        return pickle.loads(data)


    def get_socket(self):
        return self.sock

    #receber exatamente N bytes
    def receive_all(self, conn, length):
        data = b''
        while len(data) < length:
            packet = conn.recv(length - len(data))
            if not packet:
                return None
            data += packet
        return data

    #receber pedido (RPC)
    def receive_command(self, conn):
        try:
            # ler tamanho (4 bytes)
            header = self.receive_all(conn, 4)
            if not header:
                return None

            tamanho = struct.unpack('!I', header)[0]

            data = self.receive_all(conn, tamanho)
            if not data:
                return None

            pedido = pickle.loads(data)

            return pedido

        except:
            return None

    #enviar resposta (RPC)
    def send_response(self, conn, resposta):
        try:
            data = pickle.dumps(resposta)

            tamanho = struct.pack('!I', len(data))

            conn.sendall(tamanho + data)

        except:
            pass