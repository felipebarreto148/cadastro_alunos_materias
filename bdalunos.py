from os import close
import sqlite3


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
        query = 'SELECT * FROM alunos ORDER BY nome'
        cursor.execute(query) 
        fetch = cursor.fetchall()
        return fetch
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
        conn.close()
        cursor.close()
    except sqlite3.Error as err:
        return 'Erro ao deletar uma aluno ', err
