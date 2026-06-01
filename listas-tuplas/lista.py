lista = []

lista = [1, "python", 2]

lista[0]

lista[1] = 100


lista.append("novo elemento")

lista.insert(0, "mais um elemento")

# print(lista)


filmes = []
filmes.insert(0, "A Procura da Felicidade")
filmes.append("O lobo de Wall Street")
filmes.insert(2, "Os Vingadores - Guerra Infinita")

# print(filmes)

lancamento = '2016', '2013', '2018'

tupla_final = (filmes, lancamento)
# print(tupla_final)

telefones = {
    "joao": 1914044692,
    "maria": 11914044693
}

# print(telefones)

telefones['elena'] = 11941820399

# print(telefones)

filmes_json = {}

filmes_json[filmes[0]] = lancamento[0]
filmes_json[filmes[1]] = lancamento[1]
filmes_json[filmes[2]] = lancamento[2]

# print(filmes_json)

# for i in lista:
#     print(i)

for k, i in filmes_json.items():
    print(f"Titulo: {k}, Lançamento: {i}")