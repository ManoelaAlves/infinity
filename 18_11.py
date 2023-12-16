#Escreva uma função lambda que receba um número e verifique se ele é par ou ímpar. 
#A função deve retornar "par" se o número for par e "ímpar" caso contrário.
#lambda {argumentos}: {expressão}
# par_impar= lambda x: "par" if x %2 == 0 else "ímpar"
# x= float(input("Digite uma número:")) 
# print(par_impar(x))

#Implemente uma função lambda que receba duas strings e retorne a concatenação das duas, apenas se ambas as strings tiverem mais de 5 caracteres.
# Caso contrário, a função deve retornar uma mensagem de erro.
# x= str(input("Digite uma palavra:")) 
# y= str(input("Digite uma palavra:"))
# palavra= lambda x,y: "Não é possível fazer a concatenação" if len(x)<=5 and len(y)<=5 else print(x+y)
# print(palavra(x,y))

#Escreva uma função lambda que receba um número e verifique se ele é maior que 10.
#Se for maior, a função deve retornar o próprio número; caso contrário, deve retornar o número dividido por 2.
# num = lambda x: x if x>10 else print(x/2)
# x= float(input("Digite uma número:")) 
# print(num(x))

#Implemente uma função lambda que receba um número e verifique se ele é divisível por 3 e por 5.
#A função deve retornar "divisível" se a condição for satisfeita e "não divisível" caso contrário.
# num = lambda x: "Divisível" if x%3 ==0 and x%5 == 0 else print("Não divisível")
# x= float(input("Digite uma número:")) 
# print(num(x))

#A partir de uma lista de strings, utilize map() e uma função lambda para converter todas as letras em maiúsculas.
# lista = []
# while True:
#     palavra = (input("Digite uma palavra: ")) 
#     lista.append(palavra)
#     fim = int(input("Qualquer número - Finalizar ou 2 - Inserir outro aluno "))
#     if fim == 2: 
#         continue
#     else:
#         break
# num = list(map(lambda x: x.upper(), lista))
# print(num)

#A partir de uma lista de palavras, utilize filter() e uma função lambda para filtrar apenas as palavras que possuem mais de 5 letras.
# lista = []
# while True:
#     palavra = (input("Digite uma palavra: ")) 
#     lista.append(palavra)
#     fim = int(input("Qualquer número - Finalizar ou 2 - Inserir outro aluno "))
#     if fim == 2: 
#         continue
#     else:
#         break
# num = list(filter(lambda x: len(x)>5, lista))
# print(num)

# uma lista de valores numéricos, utilize reduce() e uma função lambdapara obter o valor máximo da lista.
# from functools import reduce 
# numeros = [1,21,54,7,63]
# max = reduce(lambda x,y: x if x>y else y, numeros)
# print(max)

#A partir de uma lista de dicionários, cada um representando uma pessoa com os campos "nome" e "idade", utilize map() 
# e uma função lambda para obter uma nova lista contendo apenas os nomes das pessoas.
# pessoas = {'Jose':'32','Carlos':'25','Lucas':'18'}
# nomes = list(map(lambda x: x, pessoas))
# print(nomes)
