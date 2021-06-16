import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb


app = tk.Tk()
app.title('Cadastro de alunos e notas')
app.resizable(False, False)
width = 400
height = 200
sc_width = app.winfo_screenwidth()
sc_height = app.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
app.geometry("%dx%d+%d+%d" % (width, height, x, y))
app.config(bg='#167ec4')


tk.Button(app, text="Alunos", font=("Arial")).grid(row=0, column=0, padx=(100, 10), pady=50)
tk.Button(app, text="Matérias", font=("Arial")).grid(row=0, column=1)

if __name__ == "__main__":
    app.mainloop()