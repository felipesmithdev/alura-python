import sqlite3

conn = sqlite3.connect('banco.db') # cria e conecta ao banco de dados

cursor = conn.cursor() # cria um cursor para executar comandos SQL

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
            )
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_disciplina TEXT NOT NULL,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id))    
    """
)

conn.commit()
conn.close()