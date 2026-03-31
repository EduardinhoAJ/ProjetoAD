#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Cria o objeto cliente

class Cliente:

    _contador_global = 1

    def __init__(self, nome_cliente, email, password):

        self.id_cliente = Cliente._contador_global
        self.nome = nome_cliente
        self.email = email
        self.password = password

        Cliente._contador_global += 1

    def obter_id(self):
        return self.id_cliente

    def __str__(self):
        return f"{self.id_cliente} - {self.nome} ({self.email})"