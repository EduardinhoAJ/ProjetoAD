Executamos ambos as runs de servidor e cliente, bem como os testes unitários em que obtivemos o resultado: 

MarketPlace> python -m unittest testes.py ........... ---------------------------------------------------------------------- Ran 11 tests in 0.001s OK PS C:\Users\guima\Documents\Projecto-AD-2526-1Fase-20260304T215755Z-3-001\Projecto-AD-2526-1Fase\Projecto-AD-2526-1Fase\MarketPlace>


Tivemos problemas ao lançar o teste de CRIAR_CATEGORIA, sendo a origem do problema as backslashes dadas nas class Exceptions dadas na Template.


Criamos ficheiros extra na pasta do servidor; cliente.py, produto.py, parecidos ao ficheiro da template, categoria.py;
 


Fizemos imports extra nas mains, redes, loja e processador, todas marcadas.


Não encontramos o tamanho recomendado da mensagem no enunciado, por isso tomamos liberdade de meter o tamanho maximo de 1024.

Para executar o ficheiro, lançar ambos o servidor e o cliente no porto desejado e depois mandar os comandos desejados do lado do cliente.

