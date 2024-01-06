from tkinter import *
janela = Tk()
janela.geometry("500x200")
janela.resizable(False, False)

# Label
label = Label(janela, text='Cadastro do aluno', font=('Arial',12))
label.pack()

entry_nome = StringVar()
entry = Entry(janela, textvariable=entry_nome, show='*')
entry.pack()

entry_idade = StringVar()
entry = Entry(janela, textvariable=entry_idade, show='*')
entry.pack()

entry_nota = StringVar()
entry = Entry(janela, textvariable=entry_nota, show='*')
entry.pack()

def button_click():
    label.config(text=entry.get())

botao = Button(janela, text="Confirmar", command=button_click)
botao.pack()
janela.mainloop()