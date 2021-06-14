import sqlite3

conn = sqlite3.connect('./cadastro.db')
cursor = conn.cursor()


def connect():
    query = """ CREATE TABLE IF NOT EXISTS alunos(
        matricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    ) """
    cursor.execute(query)
    conn.commit()
    conn.close()


def insert(nome, idade, email, telefone):
    try:
        query = 'INSERT INTO alunos (nome, idade, email, telefone) VALUES (?, ?, ?, ?, ?, ?)', (
            nome, idade, email, telefone)
        conn.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        return 'Erro ao adicionar uma nova matéria: ', err


def consult():
    try:
        query = 'SELECT * FROM alunos'
        return conn.execute(query)
    except sqlite3.Error as err:
        return 'Erro ao consultar as alunos: ', err


def update(matricula, nome, idade, email, telefone):
    try:
        query = 'UPDATE alunos SET nome = ?, email = ?, telefone = ?, idade = ? WHERE matricula = ?', (
            nome, email, telefone, idade, matricula)
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        return 'Erro ao alterar uma matéria: ', err


def delete(matricula):
    try:
        query = 'DELETE FROM alunos WHERE matricula = ?', (matricula)
        conn.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        return 'Erro ao deletar uma aluno ', err
