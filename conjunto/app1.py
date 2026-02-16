dict1 = {"nome": "Ana", "nota": "10.0"}
dict2 = dict(nome="Maria", nota=9.4)
# dicionario = {}
# dicionario = dict()

estoque = {
    "frutas": {"maçã", "uva"},
    "verduras": {"cenoura", "alface"}
} # dicionario com conjuntos

estoque["frutas"].add("morango")

estoque["verduras"].discard("alface")

print(estoque)