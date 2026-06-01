import csv
import json

# with open('dados.txt', 'w') as f:
#     f.write('Hello World!\n')

# with open('dados.txt', 'a') as f:
#     f.write("\nUltima linha papai")

# with open('dados.txt', 'r') as f:
#     conteudo = f.read()  

# print(conteudo)

# with open('dados.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Nome', 'Idade'])
#     writer.writerow(['Alice', 28])

# with open('dados.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# dados = {
#     'nome': 'Ana',
#     'idade': 28,
#     'enderecos': ['avenida paulista', 'rua das flores']
# }

# # with open('dados.json', 'w') as f:
# #     json.dump(dados, f)

# with open('dados.json', 'r') as f:
#     dados_lidos = json.load(f)
#     print(dados_lidos)


# o comando with open é utilizado para criar um arquivo ou abrir um arquivo existente. Utilizamos funções como read(r), write(w) e append(a) para
# ler, escrever ou adicionar uma nova linha, também possui o modo newline para ler arquivos csv.
# Logo após setar uma opção, é necessario instaciar esse objeto, seja ele um reader, um writer ou um dump(dump é utilizado para arquivos .json)
