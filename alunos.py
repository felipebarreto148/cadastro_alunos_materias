import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb

import bd as bd


# ---------- Config Tela ----------
app = tk.Tk()
app.title('Cadastro de alunos')
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


    # --------- Alunos ----------
matricula = None
nome = StringVar()
idade = StringVar()
email = StringVar()
telefone = StringVar()


# ---------- MÉTODOS ALUNOS --------
def consultarAlunos():
    tableAlunos.delete(*tableAlunos.get_children())
    fetch = bd.consultar_alunos()
    for data in fetch:
        tableAlunos.insert('', 'end', values=(data))

def inserirDadosAlunos():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        bd.inserir_aluno(nome.get(), idade.get(), email.get(), telefone.get())
        consultarAlunos()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")

def atualizarDadosAlunos():
    tableAlunos.delete(*tableAlunos.get_children())
    bd.editar_aluno(int(matricula), str(nome.get()), int(idade.get()), str(email.get()), str(telefone.get()))
    consultarAlunos()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    updateWindow.destroy()


# ------------- Telas Alunos -------------
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
    Button(formContact, text="Inserir", font=('Arial', 18), command=inserirDadosAlunos).grid(row=6, columnspan=2, pady=10)

def deletarAluno():
    if not tableAlunos.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista para remover.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja excluir o aluno?")
        if resultado == 'yes':
            selectItem = tableAlunos.focus()
            conteudo = (tableAlunos.item(selectItem))
            selectedItem = conteudo['values']
            bd.remover_aluno(selectedItem[0])
            tableAlunos.delete(selectItem)
            consultarAlunos()

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
        idade.set(selectedItem[2])
        email.set(selectedItem[3])
        telefone.set(selectedItem[4])

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
        Label(formTitle, bg='#335599', fg='#ffffff', text="Atualizando Aluno", font=('arial', 18), width=300).pack(fill=X)
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
        Button(formContact, bg='#335599', fg="#ffffff", text="Atualizar", font=('Arial', 18), command=atualizarDadosAlunos).grid(row=6, columnspan=2, pady=10)


#============================================
#============================================
#============================================
# =================== Notas =================
# -------- Variaveis -------
materia = StringVar()
av1 = DoubleVar()
av2 = DoubleVar()
av3 = DoubleVar()
avd = DoubleVar()
avds = DoubleVar()
media = DoubleVar()
matricula = IntVar()
materia = StringVar()

winNotas = None
tableNotas = None

# -------- Métodos --------
def consultarNotas(matricula):
    tableNotas.delete(*tableNotas.get_children())
    fetch = bd.consultar_notas(matricula)
    for data in fetch:
        tableNotas.insert('', 'end', values=(data))

def submitNota():
    getAluno()
    calcularMedia()
    if materia.get() == "" or av1.get() == 0 or av2.get() == 0 or avd.get() == 0:
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        if av3.get() == 0:
            av3.set(0)
    
        if avds.get() == 0:
            av3.set(0)
        tableNotas.delete(*tableNotas.get_children())
        bd.inserir_nota(av1.get(), av2.get(), av3.get(), avd.get(), avds.get(), media.get(), matricula.get(), materia.get())
        consultarNotas(getAluno())
        materia.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        media.set("")
        
def updateNota():
    pass
    consultarNotas(getAluno())


# Actions
def calcularMedia():
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

    media.set(total/len(notas))

def getMaterias():
    global vSelect
    vSelect = []
    fetch = bd.consultar_materias()
    for value in fetch:
        vSelect.append(value[1])

def getAluno():
    tableAlunos.focus()
    selectItem = tableAlunos.focus()
    conteudo = (tableAlunos.item(selectItem))
    selectedItem = conteudo['values']
    matricula.set(selectedItem[0])
    return selectedItem[0]


# CRUD
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
            bd.remover_nota(selectedItem[0])   
            consultarNotas(getAluno())       

def adicionarNota():
    getMaterias()
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
    Label(formContact, text="av1", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=1, sticky=W, pady=8)
    Label(formContact, text="av2", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=2, sticky=W, pady=8)
    Label(formContact, text="av3", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=3, sticky=W, pady=8)
    Label(formContact, text="avd", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=4, sticky=W, pady=8)
    Label(formContact, text="avds", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=5, sticky=W, pady=8)

    # --------- ENTRY DO INCLUDE ----------
    ttk.Combobox(formContact, textvariable=materia, values=vSelect).grid(row=0, column=1)
    Entry(formContact, textvariable=av1, font=('arial', 12)).grid(row=1, column=1)
    Entry(formContact, textvariable=av2, font=('arial', 12)).grid(row=2, column=1)
    Entry(formContact, textvariable=av3, font=('arial', 12)).grid(row=3, column=1)
    Entry(formContact, textvariable=avd, font=('arial', 12)).grid(row=4, column=1)
    Entry(formContact, textvariable=avds, font=('arial', 12)).grid(row=5, column=1)

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
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        materia.set(selectedItem[1])
        av1.set(selectedItem[2])
        av2.set(selectedItem[3])
        av3.set(selectedItem[4])
        avd.set(selectedItem[5])
        avds.set(selectedItem[6])
        
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
        Label(formContact, text="av1", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=1, sticky=W, pady=8)
        Label(formContact, text="av2", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=2, sticky=W, pady=8)
        Label(formContact, text="av3", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=3, sticky=W, pady=8)
        Label(formContact, text="avd", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=4, sticky=W, pady=8)
        Label(formContact, text="avds", font=('arial', 12), bg='#119922', fg='#ffffff').grid(row=5, sticky=W, pady=8)

        # --------- ENTRY DO INCLUDE ----------
        Entry(formContact, textvariable=materia, font=('arial', 12)).grid(row=0, column=1)
        Entry(formContact, textvariable=av1, font=('arial', 12)).grid(row=1, column=1)
        Entry(formContact, textvariable=av2, font=('arial', 12)).grid(row=2, column=1)
        Entry(formContact, textvariable=av3, font=('arial', 12)).grid(row=3, column=1)
        Entry(formContact, textvariable=avd, font=('arial', 12)).grid(row=4, column=1)
        Entry(formContact, textvariable=avds, font=('arial', 12)).grid(row=5, column=1)
        
        # --------- BUTTON DO ATUALIZAR ---------
        Button(formContact, bg='#335599', fg="#ffffff", text="Atualizar", font=('Arial', 18), command=updateNota).grid(row=6, columnspan=2, pady=10)


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

    tk.Button(winNotas, text="Incluir Nota", bg="#009900", font=("Arial"), fg="#ffffff", command=adicionarNota).grid(row=0, column=0, padx=8)
    tk.Button(winNotas, text="Editar Nota", bg="#0000ff", font=("Arial"), fg="#ffffff", command=editarNota).grid(row=1, column=0, padx=8, pady=8)
    tk.Button(winNotas, text="Remover Nota", bg="#bb0000", font=("Arial"), fg="#ffffff", command=deletarNota).grid(row=2, column=0, padx=8, pady=8)

    columnsN = ("Materia", "av1", "av2", "av3", "avd", "avds", "Media")

        #----- Table Alunos -----
    tableNotas = ttk.Treeview(winNotas, columns=columnsN, show="headings", selectmode="extended")

    tableNotas.heading("Materia", text="Materia", anchor=W)
    tableNotas.heading("av1", text="av1", anchor=W)
    tableNotas.heading("av2", text="av2", anchor=W)
    tableNotas.heading("av3", text="av3", anchor=W)
    tableNotas.heading("avd", text="avd", anchor=W)
    tableNotas.heading("avds", text="avds", anchor=W)
    tableNotas.heading("Media", text="Media", anchor=W)

    tableNotas.column('#1', stretch=NO, minwidth=0, width=150)
    tableNotas.column('#2', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#3', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#4', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#5', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#6', stretch=NO, minwidth=0, width=60)
    tableNotas.column('#7', stretch=NO, minwidth=0, width=60)

    tableNotas.grid(row=0, column=2, padx=20, pady=8, rowspan=3)

    consultarNotas(getAluno())




#===========================================
#===========================================
#===========================================
# FIM DAS NOTAS
#===========================================
#===========================================

# ---------- Buttons Alunos ---------
tk.Button(app, text="Incluir Aluno", bg="#009900", font=("Arial"), fg="#ffffff", command=adicionarAluno).grid(row=1, column=0, padx=8, pady=8)
tk.Button(app, text="Editar Aluno", bg="#0000ff", font=("Arial"), fg="#ffffff", command=editarAluno).grid(row=2, column=0, padx=8, pady=8)
tk.Button(app, text="Remover Aluno", bg="#bb0000", font=("Arial"), fg="#ffffff", command=deletarAluno).grid(row=3, column=0, padx=8, pady=8)

# ---------- Tabela Alunos ---------
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

tableAlunos.grid(row=1, column=2, padx=(8, 0), pady=8, rowspan=3)
tableAlunos.bind('<Double-Button-1>', scNotas)


if __name__ == "__main__":
    bd.init()
    consultarAlunos()
    app.mainloop()