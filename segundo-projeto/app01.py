import random

# numero = random.randint(1,10)

# print(numero)

def somar(n1, n2):
    return n1 + n2

try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    resultado = somar(numero1, numero2)

    print(f'A soma dos números {numero1} + {numero2} é igual a: {resultado}')
except ValueError:
    print('Erro: Digite apenas valores numéricos!')