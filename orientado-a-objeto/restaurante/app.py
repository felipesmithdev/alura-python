from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pizza = Restaurante('Praca', 'Gourmet')
restaurante_praca = Restaurante('Pizza Express', 'Italiana')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)




# restaurante_mexicano.alternar_estado()
# restaurante_mexicano.receber_avaliacao('Felipe', 9)
# restaurante_mexicano.receber_avaliacao('Maria', 8)
# restaurante_mexicano.receber_avaliacao('Julia', 2)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()