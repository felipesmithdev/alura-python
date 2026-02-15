from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
     
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # def adicionar_bebida_no_cardapio(self, Bebida):
    #     self._cardapio.append(Bebida)

    # def adicionar_prato_no_caradapio(self, Prato):
    #     self._cardapio.append(Prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco}'
            if hasattr(item, 'descricao'):
                mensagem += f' | {item.descricao}'
            else:
                mensagem += f' | {item._tamanho}'
            print(mensagem)


    

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

