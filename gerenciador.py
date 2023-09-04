import sqlite3


def adicionar_tarefa(self, task):
    conn = sqlite3.connect('tasks.db')
    conn.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, False))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def marcar_como_concluida(task_id):
    conn = sqlite3.connect('tasks.db')
    conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (True, task_id))
    conn.commit()
    conn.close()

def excluir_tarefa(task_id):
    conn = sqlite3.connect('tasks.db')
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

