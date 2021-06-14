import sqlite3

conn = sqlite3.connect('./trabalhoAV2/escola.db')
cursor = conn.cursor()


def connect():
    query = """ CREATE TABLE IF NOT EXISTS alunos(
        matricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        turma TEXT NOT NULL,
    ) """
    conn.execute(query)


def insert(nome, idade, turma):
    try:
        query = 'INSERT INTO alunos (nome, email, telefone, idade, turma, endereco) VALUES (?, ?, ?, ?, ?, ?)', (
            nome, email, telefone, idade, turma, endereco)
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


def update(id_aluno, nome, idade, turma):
    try:
        query = 'UPDATE alunos SET nome = ?, email = ?, telefone = ?, idade = ?, turma = ?, endereco = ? WHERE id_aluno = ?', (
            nome, email, telefone, idade, turma, endereco, id_aluno)
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        return 'Erro ao alterar uma matéria: ', err


def delete(id_aluno):
    try:
        query = 'DELETE FROM alunos WHERE id_aluno = ?', (id_aluno)
        conn.execute(query)
        conn.commit()
    except sqlite3.Error as err:
        return 'Erro ao deletar uma aluno ', err
