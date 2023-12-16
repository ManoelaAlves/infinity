'''
#exercícios de revisão
# #Crie uma função que inverte uma string e a retorna de trás para frente.
# def inv():
#     letra = (input("Digite uma palavra: "))
#     return letra[::-1]
# print(inv())
# #Crie uma função enigmática que recebe dois números e retorna o maior deles.
# def misterio(a:float,b:float):
#     if a > b:
#         return a, "é maior"
#     else:
#         return b,"É maior"
    
# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite um número: "))
# print(misterio(num1,num2))
'''
#Crie uma função que recebe uma lista de palavras e retorna a palavra mais longa encontrada.

# def maiorpalavra():
#     lista = []
#     while True:
#       palavra = (input("Digite uma palavra: ")) 
#       lista.append(palavra)
#       fim = int(input(" Qualquer número - Finalizar ou 1 - Inserir outro aluno "))
#       if fim == 2: 
#       elif fim!=2:
#           break
#     tamanho = len(lista)
# maiorpalavra()  
def maiorpalavra():
    lista = []
    
    while True:
        palavra = input("Digite uma palavra: ")
        lista.append(palavra)
        fim = input("Digite 1 para inserir outra palavra ou 2 para finalizar: ")
        if fim == '2':
            break
    
    

# Chame a função para testá-la
maiorpalavra()