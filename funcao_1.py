# Aula de funções
# defino minha função, dentro do parentese eu passo o argumento da minha função
# return serve para mostrar o que sua função deve responder quando for chamada, seja uma str ou resultado.
# def saudacao(nome):
#     return f"Olá, {nome.title()}"

# print(saudacao("Manoela Bastos"))
#####################################################
#Crie uma função para calcular o IMC de 4 pessoas. Em seguida crie um programa que peça o peso e a altura de uma pessoa e implemente a função em seu
# def imc(imc):
#     lista= []
#     cont = 0
#     while cont<4:
#         peso = float(input("Digite seu peso: "))
#         altura = float(input("Digite sua altura: "))
#         imc = peso/(altura*altura)
#         lista.append(imc)
#         cont += 1
#     print(lista)
#     return(lista)

# imc(imc)      
#Usando dicionário
def imc(imc):
    dados= {}
    cont = 0
    while cont<4:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso/(altura*altura)
        if imc <17:
            nome= ("Muito abaixo do peso")
        elif (imc >= 17) and (imc <= 18.49):
            nome= ("Abaixo do peso")
        elif (imc >= 18.5) and (imc <= 24.99):
            nome= ("Peso normal")
        elif (imc >= 25) and (imc <= 29.99):
            nome= ("Acima do peso")
        elif (imc >= 30) and (imc <= 34.99):
            nome= ("Obesidade 1")
        elif (imc >= 35) and (imc <= 39.99):
            nome= ("Obesidade 2")
        else:
            nome= ("Obesidade 3")
        dados[imc]= nome
        cont += 1
    print(dados)
    return(dados)

imc(imc)    
#2.Crie uma função que retorne quantas letras possui uma palavra. Se for passado uma frase, a função deverá 
#retornar o número de letras, espaços vazios e quantos sinais de pontuação.
# coisa = str.upper(input("Digite palavra ou frase: "))
# letr =0
# vaz = 0
# sig =0
# def letras(letras, vazio, sinal):
#     dados ={}
#     global letr, vaz, sig
#     sinais= '.,;:"!()-?'
#     for letra in coisa:
#         if letra in " ":
#             vaz += 1
#             #dados["vazio"]= vaz
#         elif letra in sinais:
#             sig += 1
#             #dados["sinal"]= sig
#         else:
#             letr +=1
#             #dados["letras"]= letr
#     dados["letras"]= letr
#     dados["vazio"]= vaz
#     dados["sinal"]= sig
#     #print(dados)
#     return(dados)

# print(letras(letr,vaz,sig))

# 3.Crie uma função que calcule o valor/hora do funcionário, em seguida implemente essa função em um programa de calcular hora e valor do funcionário.