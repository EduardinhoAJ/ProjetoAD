#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Contém as class Loja, que por si contém as funções que são chamadas pelo processador.py. São estas as funções que fazem o comando desejado pelo cliente
#Estão separadas as funções da Template e as criadas pelos alunos


from shared.utilities import normalizar_nome

from servidor.categoria import Categoria
from servidor.produto import Produto
from servidor.cliente import Cliente

from servidor.excepcoes import (
    ExcepcaoSupermercadoCategoriaJaExistente,
    ExcepcaoSupermercadoCategoriaNaoExistente,
    ExcepcaoSupermercadoProdutoJaExiste,
    ExcepcaoSupermercadoProdutoNaoExiste,
    ExcepcaoSupermercadoClienteNaoExistente,
    ExcepcaoSupermercadoEmailJaExiste,
    ExcepcaoSupermercadoCarrinhoVazio,
    ExcepcaoSupermercadoStockInsuficiente,
)

class Loja:

    def __init__(self):
        self._categorias = {}
        self._produtos = {}
        self._clientes = {}
        self._carrinhos = {}
        self._encomendas = {}
        self._encomenda_id_counter = 1

    # =========================
    # RESET (TESTES)
    # =========================
    def reset(self):
        Categoria._contador_global = 1
        Produto._contador_global = 1
        Cliente._contador_global = 1

        self._categorias = {}
        self._produtos = {}
        self._clientes = {}
        self._carrinhos = {}
        self._encomendas = {}
        self._encomenda_id_counter = 1

    # =========================
    # AUXILIARES
    # =========================
    def obter_id_categoria(self, nome):
        for c in self._categorias.values():
            if c.nome == nome:
                return c.id_categoria
        return None

    def obter_id_produto(self, nome):
        for p in self._produtos.values():
            if p.nome_produto == nome:
                return p.id_produto
        return None

    def obter_email_cliente(self, email):
        for c in self._clientes.values():
            if c.email == email:
                return c.id_cliente
        return None

    def lista_clientes(self):
        return list(self._clientes.values())

    # =========================
    # CATEGORIAS
    # =========================
    def criar_categoria(self, nome):
        nome = normalizar_nome(nome)

        if self.obter_id_categoria(nome) is not None:
            raise ExcepcaoSupermercadoCategoriaJaExistente(nome)

        categoria = Categoria(nome)
        self._categorias[categoria.id_categoria] = categoria
        return categoria

    def lista_categorias(self):
        return list(self._categorias.values())

    def remove_categoria(self, nome):
        nome = normalizar_nome(nome)

        id_cat = self.obter_id_categoria(nome)
        if id_cat is None:
            raise ExcepcaoSupermercadoCategoriaNaoExistente(nome)

        del self._categorias[id_cat]
        return nome

    # =========================
    # PRODUTOS
    # =========================
    def cria_produto(self, nome, categoria, preco, quantidade):
        nome = normalizar_nome(nome)
        categoria = normalizar_nome(categoria)

        if self.obter_id_produto(nome) is not None:
            raise ExcepcaoSupermercadoProdutoJaExiste(nome)

        if self.obter_id_categoria(categoria) is None:
            raise ExcepcaoSupermercadoCategoriaNaoExistente(categoria)

        preco = float(preco)
        quantidade = int(quantidade)

        produto = Produto(nome, categoria, preco, quantidade)
        self._produtos[produto.id_produto] = produto
        return produto

    def lista_produtos(self):
        return list(self._produtos.values())

    def aumenta_stock_produto(self, nome, quantidade):
        nome = normalizar_nome(nome)

        id_prod = self.obter_id_produto(nome)
        if id_prod is None:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome)

        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        self._produtos[id_prod].quantidade += quantidade
        return self._produtos[id_prod]

    def atualiza_preco_produto(self, nome, preco):
        nome = normalizar_nome(nome)

        id_prod = self.obter_id_produto(nome)
        if id_prod is None:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome)

        preco = float(preco)
        if preco <= 0:
            raise ValueError("Preço inválido")

        self._produtos[id_prod].preco = preco
        return self._produtos[id_prod]

    # =========================
    # CLIENTES
    # =========================
    def criar_cliente(self, nome, email, password):
        nome = normalizar_nome(nome)
        email = normalizar_nome(email)

        if self.obter_email_cliente(email) is not None:
            raise ExcepcaoSupermercadoEmailJaExiste(email)

        cliente = Cliente(nome, email, password)
        self._clientes[cliente.id_cliente] = cliente
        return cliente

    # =========================
    # CARRINHO
    # =========================
    def adiciona_produto_carrinho(self, id_cliente, nome, quantidade):

        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)

        nome = normalizar_nome(nome)
        id_prod = self.obter_id_produto(nome)

        if id_prod is None:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome)

        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        produto = self._produtos[id_prod]

        if produto.quantidade < quantidade:
            raise ExcepcaoSupermercadoStockInsuficiente(nome)

        if id_cliente not in self._carrinhos:
            self._carrinhos[id_cliente] = {}

        carrinho = self._carrinhos[id_cliente]
        carrinho[id_prod] = carrinho.get(id_prod, 0) + quantidade

        produto.quantidade -= quantidade
        return produto

    def remove_produto_carrinho(self, id_cliente, nome_produto):

        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)

        nome_produto = normalizar_nome(nome_produto)
        id_prod = self.obter_id_produto(nome_produto)

        if id_prod is None:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome_produto)

        carrinho = self._carrinhos.get(id_cliente, {})

        if id_prod not in carrinho:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome_produto)

        quantidade = carrinho[id_prod]
        self._produtos[id_prod].quantidade += quantidade

        del carrinho[id_prod]
        return nome_produto

    def lista_carrinho(self, id_cliente):

        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)

        carrinho = self._carrinhos.get(id_cliente, {})
        produtos = [self._produtos[p] for p in carrinho]

        return produtos

    def carrinho_checkout(self, id_cliente):

        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)

        carrinho = self._carrinhos.get(id_cliente, {})

        if not carrinho:
            raise ExcepcaoSupermercadoCarrinhoVazio()

        encomenda_id = self._encomenda_id_counter
        self._encomenda_id_counter += 1

        produtos = []
        total = 0

        for id_prod, qtd in carrinho.items():
            prod = self._produtos[id_prod]
            total += prod.preco * qtd
            produtos.append(prod)

        encomenda = {
            "id_encomenda": encomenda_id,
            "id_cliente": id_cliente,
            "produtos": produtos,
            "total_preco": total
        }

        self._encomendas[encomenda_id] = encomenda
        self._carrinhos[id_cliente] = {}

        return encomenda

    # =========================
    # ENCOMENDAS
    # =========================
    def lista_encomendas_cliente(self, id_cliente):

        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)

        return [
            e for e in self._encomendas.values()
            if e["id_cliente"] == id_cliente
        ]

    