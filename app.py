import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb
import sqlite3

# --------- Variables -----------
app = tk.Tk()
app.title('Cadastro de alunos e notas')
app.resizable(False, False)

app.geometry('700x400')
app.config(bg='#167ec4')

def inserirData():
    pass


# ----- VARIAVEIS ALUNO -----
nome = StringVar()
idade = StringVar()
email = StringVar()
telefone = StringVar()

updateWindow = None
matricula = None

# ----- VARIAVEIS NOTAS -----
winNotas = None
materia = StringVar()
AV1 = StringVar()
AV2 = StringVar()
AV3 = StringVar()
AVD = StringVar()
AVDS = StringVar()
media = StringVar()
tableNotas = None

# ----- METODOS -----
def init():
    conn = sqlite3.connect('./cadastro.db')
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS alunos(
        matricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    ) """
    cursor.execute(query)
    query = """SELECT * FROM alunos ORDER BY nome"""
    cursor.execute(query)
    fetch = cursor.fetchall()
    for data in fetch:
        tableAlunos.insert('', 'end', values=(data))
    conn.commit()
    conn.close()

def submitAluno():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tableAlunos.delete(*tableAlunos.get_children())
        conn = sqlite3.connect("./cadastro.db")
        cursor = conn.cursor()
        query = """ INSERT INTO 'alunos' (nome, telefone, email, idade) VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(telefone.get()), 
                        str(email.get()), str(idade.get())))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY matricula')
        fetch = cursor.fetchall()
        for data in fetch:
            tableAlunos.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")

def updateAluno():
    tableAlunos.delete(*tableAlunos.get_children())
    conn = sqlite3.connect("./cadastro.db")
    cursor = conn.cursor()
    query = """ UPDATE 'alunos' SET nome = ?, telefone = ?, idade = ?, email = ? WHERE matricula = ?"""
    cursor.execute(query, (str(nome.get()), str(telefone.get()),
                           str(idade.get()), str(email.get()), int(matricula)))
    conn.commit()
    cursor.execute('SELECT * FROM alunos ORDER BY matricula')
    fetch = cursor.fetchall()
    for data in fetch:
        tableAlunos.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    updateWindow.destroy()


# ---------- Functions / telas DO ALUNO ---------

def deletarAluno():
    if not tableAlunos.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista para remover.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar o contato?")
        if resultado == 'yes':
            selectItem = tableAlunos.focus()
            conteudo = (tableAlunos.item(selectItem))
            selectedItem = conteudo['values']
            tableAlunos.delete(selectItem)
            conn = sqlite3.connect("./cadastro.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'alunos' WHERE matricula = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()

def adicionarAluno():
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Aluno')
    width = 400
    height = 300
    sc_width = newWin.winfo_screenwidth()
    sc_height = newWin.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWin.config(bg='#119922')
    newWin.resizable(0, 0)

    # --------- FRAME DO INCLUDE ----------
    formTitle = Frame(newWin)
    formTitle.pack(side=TOP)
    formContact = Frame(newWin, bg="#119922")
    formContact.pack(side=TOP, pady=10)
    # --------- LABEL DO INCLUDE ----------
    Label(formTitle, text="Inserindo Aluno", font=('arial', 18), fg= '#ffffff', bg='#119922').pack(fill=X)
    Label(formContact, text="Nome", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=0, sticky=W, pady=8)
    Label(formContact, text="Telefone", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=1, sticky=W, pady=8)
    Label(formContact, text="Idade", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=2, sticky=W, pady=8)
    Label(formContact, text="Email", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=3, sticky=W, pady=8)

    # --------- ENTRY DO INCLUDE ----------
    Entry(formContact, textvariable=nome, font=('arial', 12)).grid(row=0, column=1)
    Entry(formContact, textvariable=telefone, font=('arial', 12)).grid(row=1, column=1)
    Entry(formContact, textvariable=idade, font=('arial', 12)).grid(row=2, column=1)
    Entry(formContact, textvariable=email, font=('arial', 12)).grid(row=3, column=1)

    # --------- BUTTON DO INCLUDE ---------
    Button(formContact, text="Inserir", font=('Arial', 18), command=submitAluno).grid(row=6, columnspan=2, pady=10)

def editarAluno():
    if not tableAlunos.selection():
        resultado = msb.showwarning('', 'Por favor, selecione um aluno na lista para editar.', icon="warning")
    else:
        global matricula, updateWindow
        selectItem = tableAlunos.focus()
        conteudo = (tableAlunos.item(selectItem))
        selectedItem = conteudo["values"]
        matricula = selectedItem[0]
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")
        nome.set(selectedItem[1])
        telefone.set(selectedItem[2])
        idade.set(selectedItem[3])
        email.set(selectedItem[4])

        #--------- CRIANDO JANELA UPDATE ---------
        updateWindow = Toplevel()
        updateWindow.title("Atualizar Aluno")
        width = 400
        height = 300
        sc_width = updateWindow.winfo_screenwidth()
        sc_height = updateWindow.winfo_screenheight()
        x = (sc_width/2) - (width/2)
        y = (sc_height/2) - (height/2)
        updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        updateWindow.resizable(0, 0)
        updateWindow.config(bg='#335599')

        # --------- FRAME DO ATUALIZAR ----------
        formTitle = Frame(updateWindow)
        formTitle.pack(side=TOP)
        formContact = Frame(updateWindow, bg='#335599')
        formContact.pack(side = TOP, pady = 10)
        # --------- LABEL DO ATUALIZAR ----------
        Label(formTitle, bg='#335599', fg='#ffffff', text="Atualizando contato", font=('arial', 18), width=300).pack(fill=X)
        Label(formContact, bg='#335599', fg='#ffffff', text="Nome", font=('arial', 12)).grid(row=0, sticky=W, pady=8)
        Label(formContact, bg='#335599', fg='#ffffff', text="Telefone", font=('arial', 12)).grid(row=1, sticky=W, pady=8)
        Label(formContact, bg='#335599', fg='#ffffff', text="Idade", font=('arial', 12)).grid(row=2, sticky=W, pady=8)
        Label(formContact, bg='#335599', fg='#ffffff', text="Email", font=('arial', 12)).grid(row=3, sticky=W, pady=8)

        # --------- ENTRY DO ATUALIZAR ----------
        Entry(formContact, textvariable=nome, font=('arial', 12)).grid(row=0, column=1)
        Entry(formContact, textvariable=telefone, font=('arial', 12)).grid(row=1, column=1)
        Entry(formContact, textvariable=idade, font=('arial', 12)).grid(row=2, column=1)
        Entry(formContact, textvariable=email, font=('arial', 12)).grid(row=3, column=1)
        
        # --------- BUTTON DO ATUALIZAR ---------
        Button(formContact, bg='#335599', fg="#ffffff", text="Atualizar", font=('Arial', 18), command=updateAluno).grid(row=6, columnspan=2, pady=10)


# ---------- FUNCTIONS / TELAS DAS NOTAS --------
def visualizarNotas(event):
    global winNotas, tableNotas
    materia.set("")
    AV1.set("")
    AV2.set("")
    AV3.set("")
    AVD.set("")
    AVDS.set("")
    media.set("")

    winNotas = tk.Toplevel()
    winNotas.title("Notas")
    width = 700
    height = 400
    sc_width = winNotas.winfo_screenwidth()
    sc_height = winNotas.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    winNotas.geometry("%dx%d+%d+%d" % (width, height, x, y))
    winNotas.resizable(0, 0)
    winNotas.config(bg='#22ddba')

    tk.Button(winNotas, text="Incluir Nota", bg="#009900", font=("Arial"), fg="#ffffff", command=adicionarNota).grid(row=0, column=0, padx=8)
    tk.Button(winNotas, text="Editar Nota", bg="#0000ff", font=("Arial"), fg="#ffffff", command=editarNota).grid(row=1, column=0, padx=8, pady=8)
    tk.Button(winNotas, text="Remover Nota", bg="#bb0000", font=("Arial"), fg="#ffffff", command=deletarNota).grid(row=2, column=0, padx=8, pady=8)

    columnsN = ("Materia", "AV1", "AV2", "AV3", "AVD", "AVDS", "Media")

        #----- Table Alunos -----
    tableNotas = ttk.Treeview(winNotas, columns=columnsN, show="headings", selectmode="extended")

    tableNotas.heading("Materia", text="Materia", anchor=W)
    tableNotas.heading("AV1", text="AV1", anchor=W)
    tableNotas.heading("AV2", text="AV2", anchor=W)
    tableNotas.heading("AV3", text="AV3", anchor=W)
    tableNotas.heading("AVD", text="AVD", anchor=W)
    tableNotas.heading("AVDS", text="AVDS", anchor=W)
    tableNotas.heading("Media", text="Media", anchor=W)

    tableNotas.column('#1', stretch=NO, minwidth=0, width=150)
    tableNotas.column('#2', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#3', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#4', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#5', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#6', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#7', stretch=NO, minwidth=0, width=60)

    tableNotas.grid(row=0, column=2, padx=20, pady=8, rowspan=3)
    tableNotas.bind('<Double-Button-1>', visualizarNotas)


def submitNota():
    pass

def updateNota():
    pass



def create_table_notas():
    conn = sqlite3.connect('./cadastro.db')
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS notas(
        materia INTEGER NOT NULL PRIMARY KEY,
        av1 INTEGER NOT NULL,
        av2 INTEGER NOT NULL,
        av3 INTEGER NOT NULL,
        avd INTEGER NOT NULL,
        avds INTEGER NOT NULL
        CONSTRAINT matricula FOREIGN KEY (matricula) REFERENCES alunos (matricula)
    ) """
    cursor.execute(query)
    query = """SELECT * FROM notas ORDER BY materia"""
    cursor.execute(query)
    fetch = cursor.fetchall()
    for data in fetch:
        tableNotas.insert('', 'end', values=(data))
    conn.commit()
    conn.close()

def deletarNota():
    if not tableNotas.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista para remover.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja remover as notas?")
        if resultado == 'yes':
            selectItem = tableNotas.focus()
            conteudo = (tableNotas.item(selectItem))
            selectedItem = conteudo['values']
            tableNotas.delete(selectItem)
            conn = sqlite3.connect("./cadastro.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'materia' WHERE materia = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()

def adicionarNota():
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Notas')
    width = 400
    height = 400
    sc_width = newWin.winfo_screenwidth()
    sc_height = newWin.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWin.config(bg='#119922')
    newWin.resizable(0, 0)

    # --------- FRAME DO INCLUDE ----------
    formTitle = Frame(newWin)
    formTitle.pack(side=TOP)
    formContact = Frame(newWin, bg="#119922")
    formContact.pack(side=TOP, pady=10)
    # --------- LABEL DO INCLUDE ----------
    Label(formTitle, text="Inserindo Notas", font=('arial', 18), fg= '#ffffff', bg='#119922').pack(fill=X)
    Label(formContact, text="Matéria", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=0, sticky=W, pady=8)
    Label(formContact, text="AV1", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=1, sticky=W, pady=8)
    Label(formContact, text="AV2", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=2, sticky=W, pady=8)
    Label(formContact, text="AV3", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=3, sticky=W, pady=8)
    Label(formContact, text="AVD", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=4, sticky=W, pady=8)
    Label(formContact, text="AVDS", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=5, sticky=W, pady=8)

    # --------- ENTRY DO INCLUDE ----------
    Entry(formContact, textvariable=materia, font=('arial', 12)).grid(row=0, column=1)
    Entry(formContact, textvariable=AV1, font=('arial', 12)).grid(row=1, column=1)
    Entry(formContact, textvariable=AV2, font=('arial', 12)).grid(row=2, column=1)
    Entry(formContact, textvariable=AV3, font=('arial', 12)).grid(row=3, column=1)
    Entry(formContact, textvariable=AVD, font=('arial', 12)).grid(row=4, column=1)
    Entry(formContact, textvariable=AVDS, font=('arial', 12)).grid(row=5, column=1)

    # --------- BUTTON DO INCLUDE ---------
    Button(formContact, text="Inserir", font=('Arial', 18), command=submitNota).grid(row=6, columnspan=2, pady=10)

def editarNota():
    if not tableNotas.selection():
        resultado = msb.showwarning('', 'Por favor, selecione um aluno na lista para editar.', icon="warning")
    else:
        global matricula, updateWindow
        selectItem = tableAlunos.focus()
        conteudo = (tableAlunos.item(selectItem))
        selectedItem = conteudo["values"]
        matricula = selectedItem[0]
        materia.set("")
        AV1.set("")
        AV2.set("")
        AV3.set("")
        AVD.set("")
        AVDS.set("")
        materia.set(selectedItem[1])
        AV1.set(selectedItem[2])
        AV2.set(selectedItem[3])
        AV3.set(selectedItem[4])
        AVD.set(selectedItem[5])
        AVDS.set(selectedItem[6])
        
        #--------- CRIANDO JANELA UPDATE ---------
        updateWindow = Toplevel()
        updateWindow.title("Atualizar Notas")
        width = 400
        height = 300
        sc_width = updateWindow.winfo_screenwidth()
        sc_height = updateWindow.winfo_screenheight()
        x = (sc_width/2) - (width/2)
        y = (sc_height/2) - (height/2)
        updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        updateWindow.resizable(0, 0)
        updateWindow.config(bg='#335599')

        # --------- FRAME DO ATUALIZAR ----------
        formTitle = Frame(updateWindow)
        formTitle.pack(side=TOP)
        formContact = Frame(updateWindow, bg='#335599')
        formContact.pack(side = TOP, pady = 10)
        
        # --------- LABEL DO Atualizar ----------
        Label(formTitle, text="Inserindo Notas", font=('arial', 18), fg= '#ffffff', bg='#119922').pack(fill=X)
        Label(formContact, text="Matéria", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=0, sticky=W, pady=8)
        Label(formContact, text="AV1", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=1, sticky=W, pady=8)
        Label(formContact, text="AV2", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=2, sticky=W, pady=8)
        Label(formContact, text="AV3", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=3, sticky=W, pady=8)
        Label(formContact, text="AVD", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=4, sticky=W, pady=8)
        Label(formContact, text="AVDS", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=5, sticky=W, pady=8)

        # --------- ENTRY DO INCLUDE ----------
        Entry(formContact, textvariable=materia, font=('arial', 12)).grid(row=0, column=1)
        Entry(formContact, textvariable=AV1, font=('arial', 12)).grid(row=1, column=1)
        Entry(formContact, textvariable=AV2, font=('arial', 12)).grid(row=2, column=1)
        Entry(formContact, textvariable=AV3, font=('arial', 12)).grid(row=3, column=1)
        Entry(formContact, textvariable=AVD, font=('arial', 12)).grid(row=4, column=1)
        Entry(formContact, textvariable=AVDS, font=('arial', 12)).grid(row=5, column=1)
        
        # --------- BUTTON DO ATUALIZAR ---------
        Button(formContact, bg='#335599', fg="#ffffff", text="Atualizar", font=('Arial', 18), command=updateNota).grid(row=6, columnspan=2, pady=10)


# ------ Buttons Aluno -------
tk.Button(app, text="Incluir Aluno", bg="#009900", font=("Arial"), fg="#ffffff", command=adicionarAluno).grid(row=0, column=0, padx=8)
tk.Button(app, text="Editar Aluno", bg="#0000ff", font=("Arial"), fg="#ffffff", command=editarAluno).grid(row=1, column=0, padx=8, pady=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff", command=deletarAluno).grid(row=2, column=0, padx=8, pady=8)


# ------ Tabelas ----
    # ---- Columns -----
columnsA = ("Matricula", "Nome", "Idade", "Email", "Telefone" )

    #----- Table Alunos -----
tableAlunos = ttk.Treeview(app, columns=columnsA, show="headings", selectmode="extended")

tableAlunos.heading("Matricula", text="ID", anchor=W)
tableAlunos.heading("Nome", text="Nome", anchor=W)
tableAlunos.heading("Idade", text="Idade", anchor=W)
tableAlunos.heading("Email", text="Email", anchor=W)
tableAlunos.heading("Telefone", text="Telefone", anchor=W)

tableAlunos.column('#1', stretch=NO, minwidth=0, width=50)
tableAlunos.column('#2', stretch=NO, minwidth=0, width=100)
tableAlunos.column('#3', stretch=NO, minwidth=0, width=50)
tableAlunos.column('#4', stretch=NO, minwidth=0, width=150)
tableAlunos.column('#5', stretch=NO, minwidth=0, width=100)

tableAlunos.grid(row=0, column=2, padx=(8, 0), pady=8, rowspan=3)
tableAlunos.bind('<Double-Button-1>', visualizarNotas)


if __name__ == "__main__":
    init()
    app.mainloop()