import tkinter as tk
from tkinter import font

# --------- Variables -----------
app = tk.Tk()
app.title('Cadastro de alunos e notas')
app.resizable(True, False)

app.geometry('800x600')
app.config(bg='#ffab65')

# ------ Buttons Aluno -------
tk.Button(app, text="Incluir Aluno", bg="#009900", font=("Arial"), fg="#ffffff").grid(row=0, column=0, padx=8, pady=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=1, padx=8, pady=8)

# ------ Label ------
tk.Label(app, text="Bem vindo", bg='#ffab65', font=("Arial", 20)).grid(row=0, column=2, padx=35)
tk.Label(app, text="Alunos", bg='#ffab65', font=("Arial", 20)).grid(row=1, column=1)
tk.Label(app, text="Matérias", bg='#ffab65', font=("Arial", 20)).grid(row=1, column=3)


# ------ Buttons Matérias ----
tk.Button(app, text="Incluir Matéria", bg="#009900", font=("Arial"), fg="#ffffff").grid(row=0, column=3, padx=8, pady=8)
tk.Button(app, text="Remover Matéria", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=0, column=4, padx=8, pady=8)


if __name__ == "__main__":
    app.mainloop()