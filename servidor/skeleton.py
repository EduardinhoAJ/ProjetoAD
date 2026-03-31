from servidor.loja import Loja

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
            10900: self._lista_clientes,
            11000: self._adiciona_produto_carrinho,
            11100: self._remove_produto_carrinho,
            11200: self._lista_carrinho,
            11300: self._checkout_carrinho,
            11400: self._lista_encomendas,
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

        except Exception as e:
            return [39928, [str(e)]]

    # =========================
    # AUXILIAR
    # =========================
    def _nao_autorizado(self):
        return [39920, ["OPERACAO_NAO_AUTORIZADA"]]

    # =========================
    # CATEGORIAS
    # =========================
    def _cria_categoria(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        categoria = self.loja.criar_categoria(args[0])
        return [20100, categoria]

    def _lista_categorias(self, args, id_perfil, id_utilizador):
        categorias = self.loja.lista_categorias()
        print("DEBUG CATEGORIAS:", categorias)
        return [20200, categorias]
    
    def _remove_categoria(self, args, id_perfil, id_utilizador):
            if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
                return self._nao_autorizado()

            resultado = self.loja.remove_categoria(args[0])
            return [20300, resultado]

    # =========================
    # PRODUTOS
    # =========================
    def _cria_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        nome, categoria, preco, quantidade = args
        produto = self.loja.cria_produto(nome, categoria, float(preco), int(quantidade))
        return [20400, produto]

    def _lista_produtos(self, args, id_perfil, id_utilizador):
        produtos = self.loja.lista_produtos()
        return [20500, produtos]

    def _aumenta_stock_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        resultado = self.loja.aumenta_stock_produto(args[0], args[1])
        return [20600, resultado]

    def _atualiza_preco_produto(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        resultado = self.loja.atualiza_preco_produto(args[0], args[1])
        return [20700, resultado]

    # =========================
    # CLIENTES
    # =========================
    def _cria_cliente(self, args, id_perfil, id_utilizador):
        cliente = self.loja.criar_cliente(args[0], args[1], args[2])
        return [20800, cliente]

    def _lista_clientes(self, args, id_perfil, id_utilizador):
        if id_perfil not in (FUNCIONARIO, ADMINISTRADOR):
            return self._nao_autorizado()

        clientes = self.loja.lista_clientes()
        return [20900, clientes]

    # =========================
    # CARRINHO
    # =========================
    def _adiciona_produto_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        resultado = self.loja.adiciona_produto_carrinho(
            id_utilizador, args[0], args[1]
        )
        return [21000, resultado]

    def _remove_produto_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        resultado = self.loja.remove_produto_carrinho(id_utilizador, args[0])
        return [21100, resultado]

    def _lista_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        carrinho = self.loja.lista_carrinho(id_utilizador)
        return [21200, carrinho]

    def _checkout_carrinho(self, args, id_perfil, id_utilizador):
        if id_perfil != CLIENTE_REGISTADO:
            return self._nao_autorizado()

        encomenda = self.loja.carrinho_checkout(id_utilizador)
        return [21300, encomenda]

    # =========================
    # ENCOMENDAS
    # =========================
    def _lista_encomendas(self, args, id_perfil, id_utilizador):
        id_cliente = args[0]

        if id_perfil == CLIENTE_REGISTADO and id_cliente != id_utilizador:
            return self._nao_autorizado()

        encomendas = self.loja.lista_encomendas_cliente(id_cliente)
        return [21400, encomendas]

    # =========================
    # GET LOJA
    # =========================
    def get_loja(self):
        return self.loja