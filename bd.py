import sqlite3

# --------- VARIAVEIS -----------

# ----------- INIT --------------
def init():
    table_alunos()
    table_materias()
    table_notas()

# ---------- ALUNOS -------------
def table_alunos():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
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

def inserir_aluno(nome, idade, email, telefone):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ INSERT INTO 'alunos' (nome, idade, email, telefone) VALUES (?, ?, ?, ?) """
    cursor.execute(query, (nome, idade, email, telefone))
    conn.commit()
    cursor.close()
    conn.close()

def remover_aluno(matricula):
    print(type(matricula))
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ DELETE FROM 'alunos' WHERE matricula = ? """
    cursor.execute(query, (matricula, ))
    conn.commit()
    cursor.close()
    conn.close()

def editar_aluno(matricula, nome, idade, email, telefone):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ UPDATE 'alunos' SET nome = ?, idade = ?, email = ?, telefone = ? WHERE matricula = ?"""
    cursor.execute(query, (nome, idade, email, telefone, matricula))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_alunos():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ SELECT * FROM alunos ORDER BY matricula """
    cursor.execute(query)
    fetch = cursor.fetchall()
    cursor.close()
    conn.close()
    return fetch








# ---------- MATERIA -------------
def table_materias():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS materias(
        id_materia INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        materia TEXT NOT NULL
    ) """
    cursor.execute(query)
    conn.commit()
    conn.close()

def inserir_materia(materia):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ INSERT INTO 'materias' (materia) VALUES (?) """
    cursor.execute(query, (materia, ))
    conn.commit()
    cursor.close()
    conn.close()

def remover_materia(id_materia):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ DELETE FROM 'materias' WHERE id_materia = ? """
    cursor.execute(query, (id_materia, ))
    conn.commit()
    cursor.close()
    conn.close()

def editar_materia(id_materia, materia):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ UPDATE 'materias' SET materia = ? WHERE id_materia = ? """
    cursor.execute(query, (materia, id_materia))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_materias():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ SELECT * FROM materias ORDER BY id_materia """
    cursor.execute(query)
    fetch = cursor.fetchall()
    cursor.close()
    conn.close()
    return fetch









# ---------- NOTAS -------------
def table_notas():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS notas(
        AV1 REAL NOT NULL,
        AV2 REAL NOT NULL,
        AV3 REAL NOT NULL,
        AVD REAL NOT NULL,
        AVDS REAL NOT NULL,
        media REAL NOT NULL,
        matricula_aluno INTEGER,
        id_materia INTEGER,
        FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula)
        FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
    ) """
    cursor.execute(query)
    conn.commit()
    conn.close()

def inserir_nota(av1, av2, av3, avd, avds, media):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """INSERT INTO 'notas' (AV1, AV2, AV3, AVD, AVDS, media) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (av1, av2, av3, avd, avds, media))
    conn.commit()
    cursor.close()
    conn.close()

def remover_nota(matricula_aluno, id_materia):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ DELETE FROM 'notas' WHERE matricula_aluno = ? AND id_materia = ? """
    cursor.execute(query, (matricula_aluno, id_materia, ))
    conn.commit()
    cursor.close()
    conn.close()

def editar_nota(matricula_aluno, id_materia, av1, av2, av3, avd, avds, media):
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ UPDATE 'notas' SET av1 = ?, av2 = ?, av3 = ?, avd = ?, avds = ?, media = ? WHERE id_materia = ? AND matricula_aluno = ?"""
    cursor.execute(query, (av1, av2, av3, avd, avds, media, id_materia, matricula_aluno))
    cursor.close()
    conn.close()

def consultar_notas():
    conn = sqlite3.connect('./universidade.db')
    cursor = conn.cursor()
    query = """ SELECT * FROM notas ORDER BY media """
    cursor.execute(query)
    fetch = cursor.fetchall()
    cursor.close()
    conn.close()
    return fetch

