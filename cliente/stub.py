from shared.RCP import send_message, receive_message
from cliente.rede import TCPSocketCliente   # OU shared.rede
import socket


class Stub:
    def __init__(self, host, port):
        self.rede = TCPSocketCliente(host, port)

    def processa(self, pedido):
        send_message(self.rede.sock, pedido)

        resposta = receive_message(self.rede.sock)

        return resposta

    def close(self):
        self.rede.fechar_ligacao()