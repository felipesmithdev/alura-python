import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#         SELECT * FROM estudantes
#         """
# )

# cursor.execute(
#     """
#         SELECT e.nome as estudante, d.nome_disciplina as disciplina FROM estudantes e
#         JOIN disciplinas d
#         ON e.id = d.estudante_id
#     """
# )

cursor.execute(
    """
        SELECT * FROM estudantes 
        WHERE idade >= 18
    """
)

conn.commit()

estudantes = cursor.fetchall()

# for estudante in estudantes:
#     print(estudante)

# for estudante, disciplina in estudantes:
#     print(f'O estudante {estudante} tem a disciplina {disciplina}')

for estudante in estudantes:
    print(f'Estudante: {estudante[1]}, Idade: {estudante[2]}')


conn.close()
