from tkinter import *
#janela principal 
janela = Tk()
janela.geometry = Tk("500x500")
janela.resizable(False,False)
#frame
frame = Frame(width=350, height=350, bg="aqua")
#a parte qeu a gente escreve no código
label = Label(janela, text= "Isso é rótulo", font=("Arial", 12))
label.pack()


# #Button
# def algo_click():
#     label.config(text="Botão clicado!")
# algo = Button(janela, text="Clique em mim!", command=algo_click, bg="")
# algo.pack()
#loop do evento
# entry_text = StringVar()
# entry = Entry(janela,textvariable=entry_text, show="*")
# entry.pack()
# #senha
# def bnt_mostrar_senha():
#     entry.config(show="")
# mostrar_senha = Button(janela, text= "MOSTRAR SENHA", command=bnt_mostrar_senha)
# mostrar_senha.pack()
# #botão
# def algo_click():
#     label.config(text=entry.get())
# algo = Button(janela, text="Clique em mim!", command=algo_click)
# algo.pack()
# #caixa de texto
# text= Text(janela, height=5, width=30)
# text.pack()
# text.insert(END, "Exemplo de caixa de texto")

janela.mainloop()
