import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb

import bd as bd

# -------- Variaveis -------
materia = StringVar()
av1 = DoubleVar()
av2 = DoubleVar()
av3 = DoubleVar()
avd = DoubleVar()
avds = DoubleVar()
media = DoubleVar()

winNotas = None
tableNotas = None



# -------- Métodos --------
def consultarNotas():
    tableNotas.delete(*tableNotas.get_children())
    fetch = bd.consultar_materias()
    for data in fetch:
        tableNotas.insert('', 'end', values=(data))

def submitNota():
    global media
    if materia.get() == "" or av1.get() == 0 or av2.get() == 0 or avd.get() == 0:
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        if av3.get() == 0:
            av3.set(0)
    
        if avds.get() == 0:
            av3.set(0)
        tableNotas.delete(*tableNotas.get_children())
        bd.inserir_nota(av1.get(), av2.get(), av3.get(), avd.get(), avds.get(), media.get())
        materia.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        media.set("")
        
def updateNota():
    pass

def calcularMedia():
    global media
    notas =  [av1.get(), av2.get(), avd.get()]
    if av1.get() < av3.get() or av2.get() < av3.get():
        if av1.get() < av2.get():
            notas.insert(0, av3.get())
        else:
            notas.insert(1, av3.get())
    
    if avd.get() < avds.get():
        notas.insert(2, avds.get())
    
    total = 0
    for nota in notas:
        total += nota

    media = total/len(notas)    





# ---------- Notas ---------
def scNotas(event):
    global winNotas, tableNotas
    materia.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
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

    tk.Button(winNotas, text="Incluir Nota", bg="#009900", font=("Arial"), fg="#ffffff").grid(row=0, column=0, padx=8)
    tk.Button(winNotas, text="Editar Nota", bg="#0000ff", font=("Arial"), fg="#ffffff").grid(row=1, column=0, padx=8, pady=8)
    tk.Button(winNotas, text="Remover Nota", bg="#bb0000", font=("Arial"), fg="#ffffff").grid(row=2, column=0, padx=8, pady=8)

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
    #tableNotas.bind('<Double-Button-1>', visualizarNotas)
