estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_final = estoque1 + estoque2
print(f'Estoque completo: \n{estoque_final}')

