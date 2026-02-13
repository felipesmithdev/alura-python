from contador import contar_palavra

frase = input('Digite uma frase: '.strip())
if not frase:
    print("Erro: Nenhuma frase foi digitada.")
else:
    resultado = contar_palavra(frase)
    if resultado:
        print("Contagem de Palavras: ")
        for palavra, quantidade in resultado.items():
            print(f"{palavra} : {quantidade}")
    else:
        print("Nehuma palavra válida foi encontrada.")