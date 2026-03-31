from servidor.skeleton import Skeleton

class Processador:

    def __init__(self):
        self.skeleton = Skeleton()

    def get_loja(self):
        # opcional: acesso direto à loja (útil para testes/admin)
        return self.skeleton.get_loja()

    def processa(self, pedido):
        """
        Recebe um pedido RPC já desserializado:
        Ex: ["CRIA_CATEGORIA", "fruta"]
        """

        # validação mínima de segurança
        if not isinstance(pedido, list) or len(pedido) == 0:
            return ["NOK", "Pedido inválido"]

        # delega tudo ao skeleton
        return self.skeleton.processar(pedido)