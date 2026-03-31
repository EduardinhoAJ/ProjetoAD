#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#cria o objeto produto

class Produto:

    _contador_global = 1

    def __init__(self, nome_produto, nome_categoria, preco, quantidade):

        self.id_produto = Produto._contador_global
        self.nome_produto = nome_produto
        self.categoria = nome_categoria
        self.preco = float(preco)
        self.quantidade = int(quantidade)

        Produto._contador_global += 1

    def obter_id(self):
        return self.id_produto

    def __str__(self):
        return f"{self.id_produto} - {self.nome_produto} ({self.categoria}) {self.preco}€ x{self.quantidade}"