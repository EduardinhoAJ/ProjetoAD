from loja import Loja
from excepcoes import (
    ExcepcaoSupermercadoCategoriaJaExiste,
    ExcepcaoSupermercadoCategoriaNaoExiste,
    ExcepcaoSupermercadoProdutoJaExiste,
    ExcepcaoSupermercadoProdutoNaoExiste,
    ExcepcaoSupermercadoClienteJaExiste,
    ExcepcaoSupermercadoClienteNaoExiste,
    ExcepcaoSupermercadoCarrinhoVazio,
    ExcepcaoSupermercadoQuantidadeInvalida,
    ExcepcaoSupermercadoStockInsuficiente,
)


CLIENTE_ANONIMO = 0
CLIENTE_REGISTADO = 1
FUNCIONARIO = 2
ADMINISTRADOR = 3


class Skeleton:
    def __init__(self):
        self.loja = Loja()
        self.handlers = {
            10100: self._cria_categoria,
            10200: self._lista_categorias,
            10300: self._remove_categoria,
            10400: self._cria_produto,
            10500: self._lista_produtos,
            10600: self._aumenta_stock_produto,
            10700: self._atualiza_preco_produto,
            10800: self._cria_cliente,
            10900: self._adiciona_produto_carrinho,
            11000: self._remove_produto_carrinho,
            11100: self._lista_carrinho,
            11200: self._checkout_carrinho,
            11300: self._lista_encomendas,
        }

    def processar(self, pedido):
        if not isinstance(pedido, list) or len(pedido) != 4:
            return [39902, ["MENSAGEM_MAL_FORMADA"]]

        op_code, args, id_perfil, id_utilizador = pedido

        if not isinstance(args, list):
            return [39902, ["MENSAGEM_MAL_FORMADA"]]

        if op_code not in self.handlers:
            return [39901, ["OP_CODE_INVALIDO"]]

        try:
            return self.handlers[op_code](args, id_perfil, id_utilizador)

        except ExcepcaoSupermercadoCategoriaJaExiste as e:
            return [30110, [str(e)]]
        except ExcepcaoSupermercadoCategoriaNaoExiste as e:
            return [30310, [str(e)]]
        except ExcepcaoSupermercadoProdutoJaExiste as e:
            return [30410, [str(e)]]
        except ExcepcaoSupermercadoProdutoNaoExiste as e:
            return [30510, [str(e)]]
        except ExcepcaoSupermercadoClienteJaExiste as e:
            return [30810, [str(e)]]
        except ExcepcaoSupermercadoClienteNaoExiste as e:
            return [30910, [str(e)]]
        except ExcepcaoSupermercadoCarrinhoVazio as e:
            return [31210, [str(e)]]
        except ExcepcaoSupermercadoQuantidadeInvalida as e:
            return [39930, [str(e)]]
        except ExcepcaoSupermercadoStockInsuficiente as e:
            return [39931, [str(e)]]
        except Exception as e:
            return [39999, [str(e)]]

    def _nao_autorizado(self):
        return [39920, ["OPERACAO_NAO_AUTORIZADA"]]

    def _cria_categoria(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome_categoria = args[0]
        categoria = self.loja.criar_categoria(nome_categoria)
        return [20100, [str(categoria)]]

    def _lista_categorias(self, args, id_perfil, id_utilizador):
        categorias = self.loja.lista_categorias()
        return [20200, [categorias]]

    def _remove_categoria(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome_categoria = args[0]
        resultado = self.loja.remove_categoria(nome_categoria)
        return [20300, [resultado]]

    def _cria_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome_produto, nome_categoria, preco, quantidade = args
        produto = self.loja.cria_produto(nome_produto, nome_categoria, preco, quantidade)
        return [20400, [str(produto)]]

    def _lista_produtos(self, args, id_perfil, id_utilizador):
        produtos = self.loja.lista_produtos()
        return [20500, [produtos]]

    def _aumenta_stock_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome_produto, quantidade = args
        resultado = self.loja.aumenta_stock_produto(nome_produto, quantidade)
        return [20600, [resultado]]

    def _atualiza_preco_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome_produto, novo_preco = args
        resultado = self.loja.atualiza_preco_produto(nome_produto, novo_preco)
        return [20700, [resultado]]

    def _cria_cliente(self, args, id_perfil, id_utilizador):
        nome, email, password = args
        cliente = self.loja.criar_cliente(nome, email, password)
        return [20800, [str(cliente)]]

    def _adiciona_produto_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        nome_produto, quantidade = args
        resultado = self.loja.adiciona_produto_carrinho(id_utilizador, nome_produto, quantidade)
        return [20900, [resultado]]

    def _remove_produto_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        nome_produto = args[0]
        resultado = self.loja.remove_produto_carrinho(id_utilizador, nome_produto)
        return [21000, [resultado]]

    def _lista_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        carrinho = self.loja.lista_carrinho(id_utilizador)
        return [21100, [carrinho]]

    def _checkout_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        resultado = self.loja.carrinho_checkout(id_utilizador)
        return [21200, [resultado]]

    def _lista_encomendas(self, args, id_perfil, id_utilizador):
        id_cliente = args[0]

        if id_perfil == CLIENTE_REGISTADO and id_cliente != id_utilizador:
            return self._nao_autorizado()

        encomendas = self.loja.lista_encomendas_cliente(id_cliente)
        return [21300, [encomendas]]