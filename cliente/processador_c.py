from cliente.stub import Stub
from shared.excepcoes_shared import (
    OpCodes,
    CategoriaJaExiste,
    CategoriaNaoExiste,
    CategoriaComProdutos,
    ProdutoJaExiste,
    ProdutoNaoExiste,
    ProdutoNaoExistePreco,
    PrecoInvalido,
    QuantidadeInvalida,
    IncrementoInvalido,
    EmailJaExiste,
    NomeClienteInvalido,
    EmailInvalido,
    PasswordInvalida,
    ClienteNaoExiste,
    QuantidadeCarrinhoInvalida,
    StockInsuficiente,
    ProdutoNaoNoCarrinho,
    CarrinhoVazio,
    FalhaEncomenda,
    ComandoMalFormado
)

class Processador:
    def __init__(self, HOST,PORT, PERFIL, ID):
        self.stub = Stub(HOST,PORT)
        self.perfil = PERFIL
        self.ID = ID

    def processa(self, msg):
        parts = msg.split()
        args = parts[1:]

        # -------- CRIA_CATEGORIA
        if parts[0].upper() == "CRIA_CATEGORIA":
            pedido = [OpCodes.CRIA_CATEGORIA, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                categoria = lista[0]
                return f"Categoria {categoria.nome} criada com sucesso."

            if resp_code == OpCodes.CATEGORIA_JA_EXISTE:
                raise CategoriaJaExiste(lista[0])

        # -------- LISTA_CATEGORIAS
        elif parts[0].upper() == "LISTA_CATEGORIAS":
             pedido = [OpCodes.LISTA_CATEGORIAS, args, self.perfil, self.ID]

             resp_code, lista = self.stub.processa(pedido)

             if 20000 <= resp_code < 30000:

                if not lista or lista[0] is None:
                    return "Categorias:\n- (vazio)"

                categorias = lista[0]

                resultado = "Categorias:\n"
                for c in categorias:
                    resultado += f"- {c.nome}\n"

                return resultado

        # -------- REMOVE_CATEGORIA
        elif parts[0].upper() == "REMOVE_CATEGORIA":
            pedido = [OpCodes.REMOVE_CATEGORIA, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                return "Categoria removida com sucesso."

            if resp_code == OpCodes.CATEGORIA_NAO_EXISTE:
                raise CategoriaNaoExiste(lista[0])

            if resp_code == OpCodes.CATEGORIA_COM_PRODUTOS:
                raise CategoriaComProdutos(lista[0])

        # -------- CRIA_PRODUTO
        elif parts[0].upper() == "CRIA_PRODUTO":
            pedido = [OpCodes.CRIA_PRODUTO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                produto = lista[0]
                return f"Produto {produto.nome_produto} criado com sucesso."

            if resp_code == OpCodes.PRODUTO_JA_EXISTE:
                raise ProdutoJaExiste(lista[0])

            if resp_code == OpCodes.CATEGORIA_NAO_EXISTE_PRODUTO:
                raise CategoriaNaoExiste(lista[1])

            if resp_code == OpCodes.PRECO_INVALIDO:
                raise PrecoInvalido()

            if resp_code == OpCodes.QUANTIDADE_INVALIDA:
                raise QuantidadeInvalida()

        # -------- LISTA_PRODUTOS
        elif parts[0].upper() == "LISTA_PRODUTOS":
            pedido = [OpCodes.LISTA_PRODUTOS, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                produtos = lista[0]
                return f"Lista de Produtos devolvida: {produtos}."

        # -------- AUMENTA_STOCK
        elif parts[0].upper() == "AUMENTA_STOCK":
            nome_produto = args[0]

            pedido = [OpCodes.AUMENTA_STOCK, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                return f"Stock do produto {nome_produto} atualizado com sucesso."

            if resp_code == OpCodes.PRODUTO_NAO_EXISTE:
                raise ProdutoNaoExiste(nome_produto)

            if resp_code == OpCodes.INCREMENTO_INVALIDO:
                raise IncrementoInvalido()

        # -------- ATUALIZA_PRECO
        elif parts[0].upper() == "ATUALIZA_PRECO":
            nome_produto = args[0]

            pedido = [OpCodes.ATUALIZA_PRECO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                return f"Preço do produto {nome_produto} atualizado com sucesso."

            if resp_code == OpCodes.PRODUTO_NAO_EXISTE_PRECO:
                raise ProdutoNaoExistePreco(nome_produto)

            if resp_code == OpCodes.NOVO_PRECO_INVALIDO:
                raise PrecoInvalido()

        # -------- CRIA_CLIENTE
        elif parts[0].upper() == "CRIA_CLIENTE":
            pedido = [OpCodes.CRIA_CLIENTE, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                cliente = lista[0]
                return f"Cliente {cliente.nome} criado com sucesso."

            if resp_code == OpCodes.EMAIL_JA_EXISTE:
                raise EmailJaExiste()

            if resp_code == OpCodes.NOME_CLIENTE_INVALIDO:
                raise NomeClienteInvalido()

            if resp_code == OpCodes.EMAIL_INVALIDO:
                raise EmailInvalido()

            if resp_code == OpCodes.PASSWORD_INVALIDA:
                raise PasswordInvalida()

        # -------- LISTA_CLIENTES
        elif parts[0].upper() == "LISTA_CLIENTES":
            pedido = [OpCodes.LISTA_CLIENTES, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                clientes = lista[0]
                return f"Lista de Clientes devolvida: {clientes}."

        # -------- ADICIONA_PRODUTO_CARRINHO
        elif parts[0].upper() == "ADICIONA_PRODUTO_CARRINHO":
            nome_produto = args[0]

            pedido = [OpCodes.ADICIONA_PRODUTO_CARRINHO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                return f"Produto {nome_produto} adicionado ao carrinho com sucesso."

            if resp_code == OpCodes.CLIENTE_NAO_EXISTE:
                raise ClienteNaoExiste()

            if resp_code == OpCodes.PRODUTO_NAO_EXISTE_CARRINHO:
                raise ProdutoNaoExiste(nome_produto)

            if resp_code == OpCodes.QUANTIDADE_INVALIDA_CARRINHO:
                raise QuantidadeCarrinhoInvalida()

            if resp_code == OpCodes.STOCK_INSUFICIENTE:
                raise StockInsuficiente()

        # -------- REMOVE_PRODUTO_CARRINHO
        elif parts[0].upper() == "REMOVE_PRODUTO_CARRINHO":
            nome_produto = args[0]

            pedido = [OpCodes.REMOVE_PRODUTO_CARRINHO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                return f"Produto {nome_produto} removido do carrinho com sucesso."

            if resp_code == OpCodes.CLIENTE_NAO_EXISTE_REMOVE:
                raise ClienteNaoExiste()

            if resp_code == OpCodes.PRODUTO_NAO_EXISTE_REMOVE:
                raise ProdutoNaoExiste(nome_produto)

            if resp_code == OpCodes.PRODUTO_NAO_NO_CARRINHO:
                raise ProdutoNaoNoCarrinho()

        # -------- LISTA_CARRINHO
        elif parts[0].upper() == "LISTA_CARRINHO":
            pedido = [OpCodes.LISTA_CARRINHO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                carrinho = lista[0]
                return f"Carrinho devolvido: {carrinho}."

            if resp_code == OpCodes.CLIENTE_NAO_EXISTE_LISTA:
                raise ClienteNaoExiste()

        # -------- CHECKOUT_CARRINHO
        elif parts[0].upper() == "CHECKOUT_CARRINHO":
            pedido = [OpCodes.CHECKOUT_CARRINHO, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                encomenda = lista[0]
                return f"Checkout realizado com sucesso: {encomenda}"

            if resp_code == OpCodes.CLIENTE_NAO_EXISTE_CHECKOUT:
                raise ClienteNaoExiste()

            if resp_code == OpCodes.CARRINHO_VAZIO:
                raise CarrinhoVazio()

            if resp_code == OpCodes.FALHA_ENCOMENDA:
                raise FalhaEncomenda()

        # -------- LISTA_ENCOMENDAS
        elif parts[0].upper() == "LISTA_ENCOMENDAS":
            pedido = [OpCodes.LISTA_ENCOMENDAS, args, self.perfil, self.ID]

            resp_code, lista = self.stub.processa(pedido)

            if 20000 <= resp_code < 30000:
                encomendas = lista[0]
                return f"Lista de encomendas devolvida: {encomendas}."

            if resp_code == OpCodes.CLIENTE_NAO_EXISTE_ENCOMENDAS:
                raise ClienteNaoExiste()

        else:
            raise ComandoMalFormado(parts[0])

    def close(self):
        self.stub.close()