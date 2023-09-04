import sqlite3
import comandos
import gerenciador

# Conectar ao banco de dados (um arquivo SQLite será criado se não existir)
conn = sqlite3.connect('tasks.db')

# Criar uma tabela para armazenar as tarefas
conn.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed BOOLEAN
);
''')

# Fechar a conexão com o banco de dados
conn.close()


