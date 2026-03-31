from servidor.loja import Loja
from servidor.excepcoes import (
    ExcepcaoComandoDesconhecido,
    ExcepcaoComandoNumeroArgumentosIncorreto,
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
    # MAIN ENTRY (RPC)
    # ----------------------------
    def processar_comando(self, pedido):
        try:
            # pedido já vem como lista
            if not isinstance(pedido, list) or len(pedido) == 0:
                raise Exception("Pedido inválido")

            nome = pedido[0].upper()
            args = pedido[1:]

            handler = self._get_handler(nome)
            resultado = handler(args)

            return ["OK", resultado]

        except (ExcepcaoSupermercado) as e:
            return ["NOK", str(e)]

        except Exception as e:
            return ["NOK", "Erro interno"]

    # ----------------------------
    # AUXILIARES
    # ----------------------------
    def _validar_args(self, args, n):
        if len(args) != n:
            raise ExcepcaoComandoNumeroArgumentosIncorreto(n, len(args))

    def _get_handler(self, nome):
        if nome not in self.HANDLERS:
            raise ExcepcaoComandoDesconhecido(nome)
        return self.HANDLERS[nome]

    # ----------------------------
    # HANDLERS
    # ----------------------------
    def _cmd_exit(self, args):
        self._validar_args(args, 0)
        self.loja.reset()
        return "Servidor resetado"

    def _cmd_cria_categoria(self, args):
        self._validar_args(args, 1)
        categoria = self.loja.criar_categoria(args[0])
        return f"Categoria {categoria.nome} criada com sucesso."

    def _cmd_lista_categorias(self, args):
        self._validar_args(args, 0)
        return self.loja.lista_categorias()

    def _cmd_remove_categoria(self, args):
        self._validar_args(args, 1)
        nome = self.loja.remove_categoria(args[0])
        return f"Categoria {nome} removida com sucesso."

    def _cmd_cria_produto(self, args):
        self._validar_args(args, 4)
        produto = self.loja.cria_produto(
            args[0], args[1], float(args[2]), int(args[3])
        )
        return f"Produto {produto.nome_produto} criado com sucesso."

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
        cliente = self.loja.criar_cliente(args[0], args[1], args[2])
        return f"Cliente criado com id {cliente.id}"

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