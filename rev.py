#Leia o salario de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior do que 20% do salário imprima:
#Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
# salario= float(input("Digite o seu salário:")) 
# emprestimo= float(input("Digite o valor do empréstimo que você deseja:")) 
# prestacao= int(input("Em quantas vezes deseja dividir esse empréstimo:")) 
# if salario*0.2>(emprestimo/prestacao):
#     print("Empréstimo concedido")
# else:
#     print("Empréstimo não concedido")
    
#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde a altura):
#Homens: (72,7 ∗ h) − 58       Mulheres: (62, 1 ∗ h) − 44,7
# altura= float(input("Digite qual a sua altura:")) 
# sexo= (input("Qual o seu sexo: feminino ou masculino?")).upper()
# if sexo == "FEMININO":
#     peso_ideal = (62.1*altura)-44.7
#     print(f"Seu peso ideal é {peso_ideal}")
# elif sexo == "MASCULINO":
#     peso_ideal = (72.7*altura)-58
#     print(f"Seu peso ideal é {peso_ideal}")
# else:
#     print("Sexo não identificado")

#Atividade prática 1: Dada uma lista de números, crie uma nova lista contendo apenas os números pares.
# lista_1 = [1, 2, 85, 74, 99, 102, 88, 21, 26]
# lista_2 = []
# for num in lista_1:
#     if num%2 == 0:
#         lista_2.append(num)
#     else:
#         continue
# print(lista_2)
#Atividade prática 2: Crie um dicionário com informações de produtos,incluindo nome, preço e quantidade em estoque.
#Implemente funções para adicionar, remover e atualizar produtos no dicionário.
#dicionario = {'nome':'abacaxi', 'preço':'5', 'quantidade':'21', 'nome':'arroz', 'preço':'4', 'quantidade':'50'}
#Atividade prática 3:Crie um conjunto com nomes de cores. Implemente uma função que retorne as cores que têm mais de quatro letras.
# cores = ['amarelo', 'vermelho', 'azul', 'verde', 'laranja', 'turquesa']
# cor_quant_letras= list(filter(lambda x: len(x)> 4, cores))
# print(cor_quant_letras)

#Atividade prática 4: Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.
# lst= ['arara', 'manoela', 'ana', 'joão', 'sol', 'esse']
# new_lista =[]
# def palindromos(lst):
#     for palavra in lst:
#         if palavra[::-1] == palavra:
#             new_lista.append(palavra)
#         else:
#             continue
#     return(new_lista)
# print(palindromos(lst))

#Dado um dicionário que representa as vendas de produtos, encontre o produto mais vendido (ou os produtos mais vendidos, se houver um empate).
dicionario = 