import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb
import sqlite3
import bdalunos as bdA

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

# ----- METODOS -----
def submitData():
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
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tableAlunos.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")


def addAluno():
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Aluno')
    newWin.geometry('400x300')
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
    Button(formContact, text="Inserir", font=('Arial', 18), command=submitData).grid(row=6, columnspan=2, pady=10)


# # ------ Buttons Aluno -------
tk.Button(app, text="Incluir Aluno", bg="#009900", font=("Arial"), fg="#ffffff", command=addAluno).grid(row=0, column=0, padx=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=1, column=0, padx=8, pady=8)


# ------ Tabelas ----
    # ---- Columns -----
columnsA = ("Matricula", "Nome", "Idade", "Email", "Telefone" )
#columnsN = ("Materia", "AV1", "AV2", "AV3", "AVD", "AVDS", "Media")

#     #----- Table Alunos -----
tableAlunos = ttk.Treeview(app, columns=columnsA, show="headings")

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

tableAlunos.grid(row=0, column=2, padx=(8, 0), pady=8, rowspan=2)

    #----- Table Notas -----
# tableNotas = ttk.Treeview(app, columns=columnsN, show="headings")

# tableNotas.heading("Materia", text="Matéria", anchor=W)
# tableNotas.heading("AV1", text="AV1", anchor=W)
# tableNotas.heading("AV2", text="AV2", anchor=W)
# tableNotas.heading("AV3", text="AV3", anchor=W)
# tableNotas.heading("AVD", text="AVD", anchor=W)
# tableNotas.heading("AVDS", text="AVDS", anchor=W)
# tableNotas.heading("Media", text="Media", anchor=W)

# tableNotas.column('#1', stretch=NO, minwidth=0, width=100)
# tableNotas.column('#2', stretch=NO, minwidth=0, width=50)
# tableNotas.column('#3', stretch=NO, minwidth=0, width=50)
# tableNotas.column('#4', stretch=NO, minwidth=0, width=50)
# tableNotas.column('#5', stretch=NO, minwidth=0, width=50)
# tableNotas.column('#6', stretch=NO, minwidth=0, width=50)

# tableNotas.grid(row=2, column=3, columnspan=2)


# ------------------ Criação do Menu ------------------
menu = Menu(app)
app.config(menu=menu)

# Menu Aluno
fileMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label="Alunos", menu=fileMenu)
fileMenu.add_command(label="Criar Novo", command=addAluno)
fileMenu.add_command(label="Editar", command=inserirData)
fileMenu.add_command(label="Deletar", command=inserirData)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=app.destroy)

# Menu Matéria
fileMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label="Matérias", menu=fileMenu)
fileMenu.add_command(label="Criar Nova", command=inserirData)
fileMenu.add_command(label="Editar", command=inserirData)
fileMenu.add_command(label="Remover", command=inserirData)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=app.destroy)


if __name__ == "__main__":
    bdA.connect()
    app.mainloop()