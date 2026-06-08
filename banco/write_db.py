import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# cursor.execute(
#     """
#         INSERT INTO estudantes (nome, idade) VALUES
#         (?, ?)    
#     """,
#     ("Joana", 15)
# )

cursor.execute(
    """
        INSERT INTO disciplinas (nome_disciplina, estudante_id) VALUES
        (?, ?)    
    """,
    ("Informatica", 1)
)

conn.commit()
conn.close()