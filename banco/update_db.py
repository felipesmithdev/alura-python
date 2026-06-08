import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute(
    """
        UPDATE estudantes
        SET nome =  ?,
        idade = ?
        WHERE id = ? 
""",
("Felipe", 21, 1)
)

conn.commit()
conn.close()