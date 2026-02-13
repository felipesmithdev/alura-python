from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Praca', 'Gourmet')
restaurante_praca = Restaurante('Pizza Express', 'Italiana')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_mexicano.alternar_estado()
restaurante_mexicano.receber_avaliacao('Felipe', 9)
restaurante_mexicano.receber_avaliacao('Maria', 8)
restaurante_mexicano.receber_avaliacao('Julia', 2)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()