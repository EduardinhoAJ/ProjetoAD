#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#cria o objeto produto

class Produto:
    _contador_global = 1

    def __init__(self, nome_produto, nome_categoria, preco, quantidade):
        self.id = Produto._contador_global
        self.nome_produto= nome_produto
        self.nome_categoria = nome_categoria
        self.preco = preco
        self.quantidade = quantidade
        Produto._contador_global += 1

    def obter_id(self):
        return self.id