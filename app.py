import tkinter as tk
from tkinter import Frame, ttk
from tkinter import *
import bdalunos as bdA

# --------- Variables -----------
app = tk.Tk()
app.title('Cadastro de alunos e notas')
app.resizable(False, False)

app.geometry('1000x500')
app.config(bg='#167ec4')


# ----- VARIAVEIS ALUNO -----
nome = StringVar()
idade = StringVar()
turma = StringVar()

# ----- Telas -----
def addAluno():
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Aluno')
    newWin.geometry('400x300')
    newWin.config(bg='#bbffbb')

def addMateria():
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Matéria')
    newWin.geometry('400x300')
    newWin.config(bg='#bbffbb')

# ------ Buttons Aluno -------
tk.Button(app, text="Incluir Aluno", bg="#009900", font=("Arial"), fg="#ffffff", command=addAluno).grid(row=0, column=0, padx=8, pady=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=1, padx=8, pady=8)

# ------ Label ------
tk.Label(app, text="Bem vindo", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=0, column=2, padx=10)
tk.Label(app, text="Alunos", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=1, column=0, columnspan=2)
tk.Label(app, text="Notas", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=1, column=3, columnspan=2)

# ------ Buttons Notas ----
# tk.Button(app, text="Incluir Matéria", bg="#009900", font=("Arial"), fg="#ffffff", command=addMateria).grid(row=0, column=3, padx=8, pady=8)
# tk.Button(app, text="Remover Matéria", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=4, padx=8, pady=8)


# ------ Tabelas ----
    # ---- Columns -----
columnsA = ("Matricula", "Nome", "Idade", "Turma")
columnsN = ("Materia", "AV1", "AV2", "AV3", "AVD", "AVDS", "Media")

    #----- Table Alunos -----
tableAlunos = ttk.Treeview(app, columns=columnsA, show="headings")

tableAlunos.heading("Matricula", text="ID", anchor=W)
tableAlunos.heading("Nome", text="Nome", anchor=W)
tableAlunos.heading("Idade", text="Idade", anchor=W)
tableAlunos.heading("Turma", text="Turma", anchor=W)

tableAlunos.column('#1', stretch=NO, minwidth=0, width=30)
tableAlunos.column('#2', stretch=NO, minwidth=0, width=150)
tableAlunos.column('#3', stretch=NO, minwidth=0, width=50)
tableAlunos.column('#4', stretch=NO, minwidth=0, width=50)

tableAlunos.grid(row=2, column=0, columnspan=2)

    #----- Table Notas -----
tableNotas = ttk.Treeview(app, columns=columnsN, show="headings")

tableNotas.heading("Materia", text="Matéria", anchor=W)
tableNotas.heading("AV1", text="AV1", anchor=W)
tableNotas.heading("AV2", text="AV2", anchor=W)
tableNotas.heading("AV3", text="AV3", anchor=W)
tableNotas.heading("AVD", text="AVD", anchor=W)
tableNotas.heading("AVDS", text="AVDS", anchor=W)
tableNotas.heading("Media", text="Media", anchor=W)

tableNotas.column('#1', stretch=NO, minwidth=0, width=100)
tableNotas.column('#2', stretch=NO, minwidth=0, width=50)
tableNotas.column('#3', stretch=NO, minwidth=0, width=50)
tableNotas.column('#4', stretch=NO, minwidth=0, width=50)
tableNotas.column('#5', stretch=NO, minwidth=0, width=50)
tableNotas.column('#6', stretch=NO, minwidth=0, width=50)

tableNotas.grid(row=2, column=3, columnspan=2)


if __name__ == "__main__":
    #bdA.connect()
    app.mainloop()