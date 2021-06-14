import tkinter as tk
from tkinter import Frame, ttk
from tkinter.constants import TOP

# --------- Variables -----------
app = tk.Tk()
app.title('Cadastro de alunos e notas')
app.resizable(False, False)

app.geometry('1100x600')
app.config(bg='#167ec4')


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
tk.Button(app, text="Editar Aluno", bg="#0000bb", font=("Arial"), fg="#ffffff").grid(row=0, column=1, padx=8, pady=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=2, padx=8, pady=8)

# ------ Label ------
tk.Label(app, text="Bem vindo", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=0, column=3, padx=35)
tk.Label(app, text="Alunos", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=1, column=0, columnspan=2)
tk.Label(app, text="Notas", bg='#167ec4', font=("Arial", 20), fg="#ffffff").grid(row=1, column=3, columnspan=2)

# ------ Buttons Matérias ----
tk.Button(app, text="Incluir Matéria", bg="#009900", font=("Arial"), fg="#ffffff", command=addMateria).grid(row=0, column=4, padx=8, pady=8)
tk.Button(app, text="Editar Matéria", bg="#0000bb", font=("Arial"), fg="#ffffff").grid(row=0, column=5, padx=8, pady=8)
tk.Button(app, text="Remover Matéria", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=6, padx=8, pady=8)


# ------ Tabelas ----
    #----- Table Alunos -----
tableAlunos = ttk.Treeview(app).grid(row=2, column=0, columnspan=3)

    #----- Table Materias -----
tableMaterias = ttk.Treeview(app).grid(row=2, column=3, columnspan=3)


if __name__ == "__main__":
    app.mainloop()