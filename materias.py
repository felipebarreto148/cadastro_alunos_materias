import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb

import bd as bd


# ---------- Config Tela ----------
app = tk.Tk()
app.title('Cadastro de matérias')
app.resizable(False, False)
width = 700
height = 500
sc_width = app.winfo_screenwidth()
sc_height = app.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
app.geometry("%dx%d+%d+%d" % (width, height, x, y))
app.config(bg='#167ec4')


# ----------- Variaveis ------------
    
    # --------- Telas -----------
updateWindow = None


# --------- Matérias ----------
id_materia = None
materia = StringVar()

# ---------- MÉTODOS Matérias --------
def consultarMaterias():
    tableMaterias.delete(*tableMaterias.get_children())
    fetch = bd.consultar_materias()
    for data in fetch:
        tableMaterias.insert('', 'end', values=(data))

def inserirDadosMaterias():
    if materia.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        bd.inserir_materia(str(materia.get()))
        consultarMaterias()
        materia.set("")

def atualizarDadosMaterias():
    tableMaterias.delete(*tableMaterias.get_children())
    bd.editar_materia(int(matricula), str(materia.get()))
    consultarMaterias()
    materia.set("")
    updateWindow.destroy()


# ------------- Telas Materias -------------
def adicionarMateria():
    print()
    newWin = tk.Toplevel()
    newWin.title('Cadastrar Materia')
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
    Label(formTitle, text="Inserindo Materia", font=('arial', 18), fg= '#ffffff', bg='#119922').pack(fill=X)
    Label(formContact, text="Matéria", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=0, sticky=W, pady=8)

    # --------- ENTRY DO INCLUDE ----------
    Entry(formContact, textvariable=materia, font=('arial', 12)).grid(row=0, column=1)

    # --------- BUTTON DO INCLUDE ---------
    Button(formContact, text="Inserir", font=('Arial', 18), command=inserirDadosMaterias).grid(row=6, columnspan=2, pady=10)

def deletarMateria():
    if not tableMaterias.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista para remover.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja excluir o Materia?")
        if resultado == 'yes':
            selectItem = tableMaterias.focus()
            conteudo = (tableMaterias.item(selectItem))
            selectedItem = conteudo['values']
            bd.remover_materia(selectedItem[0])
            tableMaterias.delete(selectItem)
            consultarMaterias()

def editarMateria():
    if not tableMaterias.selection():
        resultado = msb.showwarning('', 'Por favor, selecione um Materia na lista para editar.', icon="warning")
    else:
        global matricula, updateWindow
        selectItem = tableMaterias.focus()
        conteudo = (tableMaterias.item(selectItem))
        selectedItem = conteudo["values"]
        matricula = selectedItem[0]
        materia.set("")
        materia.set(selectedItem[1])

        #--------- CRIANDO JANELA UPDATE ---------
        updateWindow = Toplevel()
        updateWindow.title("Atualizar Materia")
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
        Label(formTitle, bg='#335599', fg='#ffffff', text="Atualizando Materia", font=('arial', 18), width=300).pack(fill=X)
        Label(formContact, bg='#335599', fg='#ffffff', text="Matéria", font=('arial', 12)).grid(row=0, sticky=W, pady=8)
        
        # --------- ENTRY DO ATUALIZAR ----------
        Entry(formContact, textvariable=materia, font=('arial', 12)).grid(row=0, column=1)
        
        # --------- BUTTON DO ATUALIZAR ---------
        Button(formContact, bg='#335599', fg="#ffffff", text="Atualizar", font=('Arial', 18), command=atualizarDadosMaterias).grid(row=6, columnspan=2, pady=10)



# ---------- Buttons Materias ---------
tk.Button(app, text="Incluir Materia", bg="#009900", font=("Arial"), fg="#ffffff", command=adicionarMateria).grid(row=1, column=0, padx=8, pady=8)
tk.Button(app, text="Editar Materia", bg="#0000ff", font=("Arial"), fg="#ffffff", command=editarMateria).grid(row=2, column=0, padx=8, pady=8)
tk.Button(app, text="Remover Materia", bg="#bb0000", font=("Arial"), fg="#ffffff", command=deletarMateria).grid(row=3, column=0, padx=8, pady=8)

# ---------- Tabela Materia ---------
    # ---- Columns -----
columnsM = ("id", "Materia")

#----- Table Materia -----
tableMaterias = ttk.Treeview(app, columns=columnsM, show="headings", selectmode="extended")

tableMaterias.heading("id", text="ID", anchor=W)
tableMaterias.heading("Materia", text="Materia", anchor=W)

tableMaterias.column('#1', stretch=NO, minwidth=0, width=50)
tableMaterias.column('#2', stretch=NO, minwidth=0, width=100)

tableMaterias.grid(row=1, column=2, padx=(8, 0), pady=8, rowspan=3)
#tableMaterias.bind('<Double-Button-1>', visualizarNotas)


if __name__ == "__main__":
    bd.init()
    consultarMaterias()
    app.mainloop()