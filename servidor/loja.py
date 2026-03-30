#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Contém as class Loja, que por si contém as funções que são chamadas pelo processador.py. São estas as funções que fazem o comando desejado pelo cliente
#Estão separadas as funções da Template e as criadas pelos alunos


from shared.utilities import normalizar_nome
from servidor.excepcoes import ExcepcaoSupermercadoCategoriaJaExistente
from servidor.categoria import Categoria
#novos imports---------------
from servidor.produto import Produto
from servidor.cliente import Cliente
from servidor.excepcoes import ExcepcaoSupermercadoProdutoJaExiste
from servidor.excepcoes import ExcepcaoArgumentoNaoInteiro
from servidor.excepcoes import ExcepcaoComandoInvalido
from servidor.excepcoes import ExcepcaoSupermercadoProdutoNaoExiste
from servidor.excepcoes import ExcepcaoSupermercadoCategoriaNaoExistente
from servidor.excepcoes import ExcepcaoArgumentoFloatInvalido
from servidor.excepcoes import ExcepcaoSupermercadoClienteNaoExistente
from servidor.excepcoes import ExcepcaoSupermercadoStockInsuficiente
from servidor.excepcoes import ExcepcaoSupermercadoProdutoNaoExisteNocarrinho
from servidor.excepcoes import ExcepcaoSupermercadoEmailJaExiste
from servidor.excepcoes import ExcepcaoSupermercadoCarrinhoVazio
from datetime import datetime
class Loja:

    def __init__(self):
        self._categorias = {}
        self._produtos = {}
        self._clientes = {}
        self._carrinhos = {}
        self._encomendas = {}
        self._encomenda_id_counter= 1

    def reset(self): 
        Categoria._contador_global = 1
        Produto._contador_global = 1
        Cliente._contador_global = 1
        self._encomenda_id_counter= 1
        self._categorias = {}
        self._produtos = {}
        self._clientes = {}
        self._carrinhos = {}
        self._encomendas = {}
        
        # TODO: MUITO IMPORTANTE Completar esta funcao para Testes Unitários puderem executar sem problemas

        

    # -----------------------------
    # Categorias
    # -----------------------------
    def criar_categoria(self, nome):
        nome = normalizar_nome(nome)
        if self.obter_id_categoria(nome) is not None:
            raise ExcepcaoSupermercadoCategoriaJaExistente(nome)
        categoria = Categoria(nome)
        self._categorias[categoria.id] = categoria
        return categoria
    
    def obter_id_categoria(self, nome): 
        for c in self._categorias.values(): 
            if nome == c.nome: 
                return c.id
        return None

    #---------------------------------------------------------------------------------------------------------------------
    #Novas Categorias
    #---------------------------------------------------------------------------------------------------------------------

def criar_categoria(self, nome):
    nome = normalizar_nome(nome)

    if not nome:
        return [30112, []]

    if self.obter_id_categoria(nome) is not None:
        return [30110, []]

    categoria = Categoria(nome)
    self._categorias[categoria.id_categoria] = categoria

    return [20100, [categoria]]


def lista_categorias(self):
    categorias = list(self._categorias.values())
    produtos = list(self._produtos.values())

    return [20200, [categorias, produtos]]


def remove_categoria(self, nome):
    nome = normalizar_nome(nome)

    id_categoria = self.obter_id_categoria(nome)
    if id_categoria is None:
        return [30310, []]

    # verificar produtos associados
    for p in self._produtos.values():
        if p.categoria == nome and p.quantidade > 0:
            return [30311, []]

    del self._categorias[id_categoria]

    return [20300, []]





def lista_produtos(self):
        categorias = list(self._categorias.values())
        produtos = list(self._produtos.values())

        return [20500, [categorias, produtos]]
    

def aumenta_stock_produto(self, nome, quantidade):
        nome = normalizar_nome(nome)

        id_produto = self.obter_id_produto(nome)
        if id_produto is None:
            return [30610, []]

        try:
            quantidade = int(quantidade)
        except:
            return [30611, []]

        if quantidade <= 0:
            return [30611, []]

        produto = self._produtos[id_produto]
        produto.quantidade += quantidade

        return [20600, [produto]]

    
def atualiza_preco_produto(self, nome, preco):
        nome = normalizar_nome(nome)

        id_produto = self.obter_id_produto(nome)
        if id_produto is None:
            return [30710, []]

        try:
            preco = float(preco)
        except:
            return [30711, []]

        if preco <= 0:
            return [30711, []]

        produto = self._produtos[id_produto]
        produto.preco = preco

        return [20700, [produto]]




def cria_produto(self, nome, categoria, preco, quantidade):
        nome = normalizar_nome(nome)
        categoria = normalizar_nome(categoria)

        if self.obter_id_produto(nome) is not None:
            return [30410, []]

        if self.obter_id_categoria(categoria) is None:
            return [30411, []]

        try:
            preco = float(preco)
        except:
            return [30412, []]

        try:
            quantidade = int(quantidade)
        except:
            return [30413, []]

        if preco <= 0:
            return [30412, []]

        if quantidade < 0:
            return [30413, []]

        produto = Produto(nome, categoria, preco, quantidade)
        self._produtos[produto.id_produto] = produto

        return [20400, [produto]]  
    
def obter_id_produto(self, nome): 
        for p in self._produtos.values(): 
            if nome == p.nome_produto: 
                return p.id
        return None
    
    
    
    
def criar_cliente(self, nome, email, password):
        nome = normalizar_nome(nome)
        email = normalizar_nome(email)

        if self.obter_email_cliente(email) is not None:
            return [30810, []]

        cliente = Cliente(nome, email, password)
        self._clientes[cliente.id_cliente] = cliente

        return [20800, [cliente]]
        
def obter_email_cliente(self, email): 
        for cl in self._clientes.values(): 
            if email == cl.email: 
                return cl.id
        return None
    








def adiciona_produto_carrinho(self, id_cliente, nome, quantidade):
    if id_cliente not in self._clientes:
        return [31010, []]

    nome = normalizar_nome(nome)
    id_produto = self.obter_id_produto(nome)

    if id_produto is None:
        return [31011, []]

    try:
        quantidade = int(quantidade)
    except:
        return [31012, []]

    if quantidade <= 0:
        return [31012, []]

    produto = self._produtos[id_produto]

    if produto.quantidade < quantidade:
        return [31013, []]

    if id_cliente not in self._carrinhos:
        self._carrinhos[id_cliente] = {}

    carrinho = self._carrinhos[id_cliente]
    carrinho[id_produto] = carrinho.get(id_produto, 0) + quantidade

    produto.quantidade -= quantidade

    return [21000, [produto]]
    
def remove_produto_carrinho( self,id_cliente, nome_produto):
        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)
        nome_produto = normalizar_nome(nome_produto)
        id_produto = self.obter_id_produto(nome_produto)
        carrinho = self._carrinhos[id_cliente]
        if id_produto is None:
            raise ExcepcaoSupermercadoProdutoNaoExiste(nome_produto)
        produto = self._produtos[id_produto]
        if id_produto not in carrinho:
            raise ExcepcaoSupermercadoProdutoNaoExisteNocarrinho(nome_produto)
        stock_atual=int(produto.quantidade)
        quantidade_atual=int(carrinho[id_produto])
        produto.quantidade=stock_atual + quantidade_atual
        del carrinho[id_produto]
        return f"Produto {nome_produto} removido com sucesso do carrinho de compras."
    
def lista_carrinho(self, id_cliente):
    if id_cliente not in self._clientes:
        return [31210, []]

    carrinho = self._carrinhos.get(id_cliente, {})

    categorias = list(self._categorias.values())
    produtos = []

    for id_produto in carrinho:
        produtos.append(self._produtos[id_produto])

    return [21200, [categorias, produtos]]


def carrinho_checkout(self, id_cliente):
    if id_cliente not in self._clientes:
        return [31310, []]

    carrinho = self._carrinhos.get(id_cliente, {})

    if not carrinho:
        return [31311, []]

    id_encomenda = self._encomenda_id_counter
    self._encomenda_id_counter += 1

    total = 0
    produtos = []

    for id_produto, qtd in carrinho.items():
        produto = self._produtos[id_produto]
        total += produto.preco * qtd
        produtos.append(produto)

    encomenda = {
        "id_encomenda": id_encomenda,
        "id_cliente": id_cliente,
        "produtos": produtos,
        "total_preco": total
    }

    self._encomendas[id_encomenda] = encomenda
    self._carrinhos[id_cliente] = {}

    return [21300, [encomenda]]

def lista_encomendas_cliente(self, id_cliente):
        if id_cliente not in self._clientes:
            raise ExcepcaoSupermercadoClienteNaoExistente(id_cliente)
        cliente = self._clientes[id_cliente]
        encomendas_cliente = []
        for encomenda in self._encomendas.values():
            if encomenda["id_cliente"] == id_cliente:
                encomendas_cliente.append(encomenda)
        if len(encomendas_cliente) == 0:
            return "Sem Encomendas"
        total_encomendas=len(encomendas_cliente)
        total_produtos=0
        total_preco=0.00
        categorias_quantidade = {}
        lista_encomendas=""
        for encomenda in encomendas_cliente:
            id_encomenda=encomenda["id_encomenda"]
            items=encomenda["items"]
            produtos_encomenda=len(items)
            quantidade_total=0
            preco_total_encomenda=0.00
            lista_produtos=""
            for item in items:
                id_produto=item["id"]
                nome_produto=item["produto"]
                preco=item["preco"]
                quantidade=item["quantidade"]
                produto=self._produtos[id_produto]
                categoria=produto.nome_categoria
                quantidade_total+=quantidade
                preco_total_encomenda+=preco*quantidade
                if categoria not in categorias_quantidade:
                    categorias_quantidade[categoria]=0
                categorias_quantidade[categoria]+=quantidade
                lista_produtos+=f"{id_produto} - {nome_produto} ({categoria}, {preco:.2f} euros, {quantidade} unidades);\n"
            lista_encomendas+="--------------------------------------------------------------------------\n"
            lista_encomendas+=f"ID Encomenda: {id_encomenda}\n"
            lista_encomendas+=f"Total Produtos: {produtos_encomenda}\n"
            lista_encomendas+=f"Total Quantidade: {quantidade_total}\n"
            lista_encomendas+=f"Total Preço: {preco_total_encomenda:.2f} euros\n"
            lista_encomendas+=lista_produtos
            total_produtos+=produtos_encomenda
            total_preco+=preco_total_encomenda
        max_quantidade=max(categorias_quantidade.values())
        categorias_top=[]
        for categoria in categorias_quantidade:
            if categorias_quantidade[categoria]==max_quantidade:
                categorias_top.append(categoria)
        categorias_top.sort()
        categorias_top_string=", ".join(categorias_top)
        lista_final=f"Cliente: {cliente.nome_cliente} {cliente.email}\n"
        lista_final+=f"Total Encomendas: {total_encomendas}\n"
        lista_final+=f"Total Produtos: {total_produtos}\n"
        lista_final+=f"Total Preço: {total_preco:.2f} euros\n"
        lista_final+=f"Categoria Top: {categorias_top_string}\n"
        lista_final+=lista_encomendas

        return lista_final






    