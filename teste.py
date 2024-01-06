from tkinter import *

#Configuração
janela = Tk()
janela.geometry("700x435")
janela.resizable(False, False)

canvas = Canvas(janela, width=200, height=100)
canvas.pack()

canvas.create_rectangle(10,10,100,60, fill='aqua')

'''
frame = Frame(bg='black', width=350, height=350)
frame.pack()

rotulo = Label(frame, text='VITÓRIA', fg='red')
rotulo.pack()
rotulo.place(x=50, y=60)
'''


# Label
label = Label(janela, text='Isso é um rótulo', font=('Arial',12))
label.pack()

#Entrada
entry_text = StringVar()
entry = Entry(janela, textvariable=entry_text, show='*')
entry.pack()

'''
esta_exibindo_senha == False

#Senha
def btn_mostrar_senha():
    entry.config(show='')

mostrar_senha = Button(janela, text="MOSTRAR SENHA", command=btn_mostrar_senha)
mostrar_senha.pack()
'''

#Botão
def button_click():
    label.config(text=entry.get())

botao = Button(janela, text="Clique aqui", command=button_click)
botao.pack()

#Caixa de texto
text = Text(janela, height=5, width=30)
text.pack()
text.insert(END, "Exemplo de caixa de texto")

janela.mainloop()