#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Cria o objeto Categoria


class Categoria:

    _contador_global = 1

    def __init__(self, nome):

        self.id_categoria = Categoria._contador_global
        self.nome = nome

        Categoria._contador_global += 1

    def obter_id(self):
        return self.id_categoria

    def __str__(self):
        return f"{self.id_categoria} - {self.nome}"