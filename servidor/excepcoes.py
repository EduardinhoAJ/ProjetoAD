#Grupo 27
#Guilherme Trincheiras 60271      Eduardo Jacinto 60734
#contém as excepções utilizadas pelos vários ficheiros do servidor
#Estão separadas as excepções dadas na Template e as criadas pelos alunos 


# -----------------------------------
#   Excepções de Comando inválido
# -----------------------------------

class ExcepcaoComandoInvalido(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ExcepcaoArgumentoFloatInvalido(ExcepcaoComandoInvalido):
    def __init__(self, nome_argumento):
        super().__init__(f"O argumento '{nome_argumento}' não é um float válido.")


class ExcepcaoArgumentoNaoInteiro(ExcepcaoComandoInvalido):
    def __init__(self, nome_argumento):
        super().__init__(f"O argumento '{nome_argumento}' não é um inteiro válido.")


class ExcepcaoComandoNaoInterpretavel(ExcepcaoComandoInvalido):
    def __init__(self, comando):
        super().__init__(f"Não foi possível interpretar o comando '{comando}'.")


class ExcepcaoComandoVazio(ExcepcaoComandoInvalido):
    def __init__(self):
        super().__init__("Não é possível executar um comando vazio.")


class ExcepcaoComandoDesconhecido(ExcepcaoComandoInvalido):
    def __init__(self, nome_comando):
        super().__init__(f"O comando {nome_comando} não é conhecido.")


class ExcepcaoComandoNumeroArgumentosIncorreto(ExcepcaoComandoInvalido):
    def __init__(self, esperado, recebido):
        super().__init__(f"Número de argumentos inválido. Esperado {esperado}, recebido {recebido}.")


# ------------------------
# NEGÓCIO
# ------------------------

class ExcepcaoSupermercado(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ExcepcaoSupermercadoCategoriaJaExistente(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"A categoria {nome} já existe.")


class ExcepcaoSupermercadoCategoriaNaoExistente(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"A categoria {nome} não existe.")


class ExcepcaoSupermercadoProdutoNaoExiste(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"O produto {nome} não existe.")


class ExcepcaoSupermercadoProdutoJaExiste(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"O produto {nome} já existe.")


class ExcepcaoSupermercadoProdutoNaoExisteNocarrinho(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"O produto {nome} não existe no carrinho.")


class ExcepcaoSupermercadoClienteNaoExistente(ExcepcaoSupermercado):
    def __init__(self, id_cliente):
        super().__init__(f"O cliente com ID {id_cliente} não existe.")


class ExcepcaoSupermercadoStockInsuficiente(ExcepcaoSupermercado):
    def __init__(self, nome):
        super().__init__(f"Quantidade do produto {nome} insuficiente.")


class ExcepcaoSupermercadoCarrinhoVazio(ExcepcaoSupermercado):
    def __init__(self):
        super().__init__("O carrinho está vazio.")


class ExcepcaoSupermercadoEmailJaExiste(ExcepcaoSupermercado):
    def __init__(self, email):
        super().__init__(f"O email {email} já existe.")