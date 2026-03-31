#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Utiliza a class TCPSocketServidor para lançar o servidor, utilizando o porto desejado
#Contém um loop em que recebe o comando do cliente, processa o comando, e envia uma resposta desse comando

import sys
import select
import socket

from servidor.skeleton import Skeleton
from servidor.rede import TCPSocketServidor
from shared.socket_utilities import PontoAcesso


def main():

    if len(sys.argv) != 2:
        print("SERVIDOR> Uso: python -m servidor.main <porto>")
        sys.exit(1)

    skeleton = Skeleton()

    ponto_acesso = PontoAcesso('localhost', int(sys.argv[1]))
    servidor = TCPSocketServidor(ponto_acesso)

    server_socket = servidor.get_socket()

    sockets = [server_socket, sys.stdin]
    clientes = {}

    while True:

        ready, _, _ = select.select(sockets, [], [])

        for s in ready:

            # NOVO CLIENTE
            if s == server_socket:
                client_socket, addr = server_socket.accept()
                print("Novo cliente:", addr)
                sockets.append(client_socket)
                clientes[client_socket] = addr

            elif s == sys.stdin:
                cmd = input()
                if cmd in ["exit", "quit"]:
                    print("A encerrar servidor...")
                    for sock in sockets:
                        sock.close()
                    return

            else:
                try:
                    pedido = servidor.receive_command(s)

                    if pedido is None:
                        sockets.remove(s)
                        s.close()
                        continue

                    resposta = skeleton.processar(pedido)
                    servidor.send_response(s, resposta)

                except Exception as e:
                    print("Erro:", e)
                    sockets.remove(s)
                    s.close()


if __name__ == "__main__":
    main()