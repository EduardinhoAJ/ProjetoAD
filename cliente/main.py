#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Utiliza a class TCPSocketCliente de rede.py para conectar ao servidor, usa um loop while True para mandar mais mensagens se desejar e tem a funcionalidade de EXIT se desejar terminar a ligação

import sys
from cliente.processador_c import Processador
from shared.excepcoes_shared import ExcepcaoBase

HOST = "127.0.0.1"
PORT = 9000
PERFIL = 3
ID_UTILIZADOR = 1

if len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

print("[INFO] - Atualizei porto")

processador = Processador(HOST, PORT, PERFIL, ID_UTILIZADOR)


while True:
    msg = input("Mensagem: ")

    if msg.upper() == "EXIT":
        break

    try:
        resposta = processador.processa(msg)
        print("Recebi: %s" % resposta)

    except ExcepcaoBase as e:
        print("NOK;", e.msg)


processador.close()