#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#Contem a classe Processador que contem as funcoes que chamam as equivalentes funções da Loja.py para processar o que o cliente deseja, tem os Handlers dados no template para o cliente conseguir chamar a função,
#estão separadas as funções dadas no template e as novas criadas pelos alunos.
#Tem a class processar_comando que recebe o comando, obtem o handler desejado e retorna OK ou NOK dependendo se foram triggered as Exceções especificadas









import shlex
from servidor.loja import Loja

from servidor.excepcoes import (
    ExcepcaoComandoDesconhecido,
    ExcepcaoComandoNumeroArgumentosIncorreto,
    ExcepcaoComandoNaoInterpretavel,
    ExcepcaoComandoVazio,
    ExcepcaoSupermercado
)

class Processador:

    def __init__(self):
        self.loja = Loja()

        self.HANDLERS = {
            "EXIT": self._cmd_exit,
            "CRIA_CATEGORIA": self._cmd_cria_categoria,
            "LISTA_CATEGORIAS": self._cmd_lista_categorias,
            "REMOVE_CATEGORIA": self._cmd_remove_categoria,
            "CRIA_PRODUTO": self._cmd_cria_produto,
            "LISTA_PRODUTOS": self._cmd_lista_produtos,
            "AUMENTA_STOCK_PRODUTO": self._cmd_aumenta_stock,
            "ATUALIZA_PRECO_PRODUTO": self._cmd_atualiza_preco,
            "CRIA_CLIENTE": self._cmd_cria_cliente,
            "ADICIONA_PRODUTO_CARRINHO": self._cmd_add_carrinho,
            "REMOVE_PRODUTO_CARRINHO": self._cmd_remove_carrinho,
            "LISTA_CARRINHO": self._cmd_lista_carrinho,
            "CHECKOUT_CARRINHO": self._cmd_checkout,
            "LISTA_ENCOMENDAS": self._cmd_lista_encomendas
        }

    # ----------------------------
    # PARSER
    # ----------------------------
    def _dividir_comando(self, comando):
        try:
            partes = shlex.split(comando)
        except:
            raise ExcepcaoComandoNaoInterpretavel(comando)

        if not partes:
            raise ExcepcaoComandoVazio()

        return partes[0].upper(), partes[1:]

    def _validar_args(self, args, n):
        if len(args) != n:
            raise ExcepcaoComandoNumeroArgumentosIncorreto(n, len(args))

    def _get_handler(self, nome):
        if nome not in self.HANDLERS:
            raise ExcepcaoComandoDesconhecido(nome)
        return self.HANDLERS[nome]

    # ----------------------------
    # MAIN ENTRY
    # ----------------------------
    def processar_comando(self, comando):
        try:
            nome, args = self._dividir_comando(comando)
            handler = self._get_handler(nome)

            resultado = handler(args)

            return ["OK", resultado]

        except (ExcepcaoSupermercado) as e:
            return ["NOK", str(e)]

        except Exception as e:
            return ["NOK", "Erro interno"]

    # ----------------------------
    # HANDLERS BÁSICOS
    # ----------------------------
    def _cmd_exit(self, args):
        self._validar_args(args, 0)
        return self.loja.reset()

    def _cmd_cria_categoria(self, args):
        self._validar_args(args, 1)
        return self.loja.criar_categoria(args[0])

    def _cmd_lista_categorias(self, args):
        self._validar_args(args, 0)
        return self.loja.lista_categorias()

    def _cmd_remove_categoria(self, args):
        self._validar_args(args, 1)
        return self.loja.remove_categoria(args[0])

    def _cmd_cria_produto(self, args):
        self._validar_args(args, 4)
        return self.loja.cria_produto(args[0], args[1], args[2], args[3])

    def _cmd_lista_produtos(self, args):
        self._validar_args(args, 0)
        return self.loja.lista_produtos()

    def _cmd_aumenta_stock(self, args):
        self._validar_args(args, 2)
        return self.loja.aumenta_stock_produto(args[0], args[1])

    def _cmd_atualiza_preco(self, args):
        self._validar_args(args, 2)
        return self.loja.atualiza_preco_produto(args[0], args[1])

    def _cmd_cria_cliente(self, args):
        self._validar_args(args, 3)
        return self.loja.criar_cliente(args[0], args[1], args[2])

    def _cmd_add_carrinho(self, args):
        self._validar_args(args, 3)
        return self.loja.adiciona_produto_carrinho(int(args[0]), args[1], args[2])

    def _cmd_remove_carrinho(self, args):
        self._validar_args(args, 2)
        return self.loja.remove_produto_carrinho(int(args[0]), args[1])

    def _cmd_lista_carrinho(self, args):
        self._validar_args(args, 1)
        return self.loja.lista_carrinho(int(args[0]))

    def _cmd_checkout(self, args):
        self._validar_args(args, 1)
        return self.loja.carrinho_checkout(int(args[0]))

    def _cmd_lista_encomendas(self, args):
        self._validar_args(args, 1)
        return self.loja.lista_encomendas_cliente(int(args[0]))

    
