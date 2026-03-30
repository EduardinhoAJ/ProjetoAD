#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Cria o objeto cliente

class Cliente:
    _contador_global = 1

    def __init__(self, nome_cliente, email, password):
        self.id = Cliente._contador_global
        self.nome_cliente=nome_cliente
        self.email = email
        self.password=password
        Cliente._contador_global += 1

    def obter_id(self): 
        return self.id