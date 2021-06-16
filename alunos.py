import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as msb

import bd as bd


# ---------- Config Tela ----------
app = tk.Tk()
app.title('Cadastro de alunos e notas')
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
#tableAlunos.bind('<Double-Button-1>', visualizarNotas)


if __name__ == "__main__":
    bd.init()
    consultarAlunos()
    app.mainloop()