# c=1
# while c<=20:
#     if c%2 == 0:
#         print(c)
#     c = c+1
# print ("Fim")

# soma = 0
# c=0
# while c<=100: 
#      soma = soma + c
#      c=c+1
# print(soma)
################################### DESAFIO 1 ########################
# é uma sequência numérica em que cada número seguinte é a soma dos dois anteriores, iniciando por 0.
# n = int(input("Digite um número? "))
# if n == 0 or n == 1:
#      print (n)
# else:
#     numero1 =  0
#     print (numero1)
#     numero2 = 1
#     print (numero2)
#     for i in range(0,(n-2)): 
#         numero3 = numero1 + numero2
#         print(numero3)
#         numero1= numero2
#         numero2 = numero3
# correção da professora
# Peça ao usuário para inserir o valor de n
# n = int(input("Digite um número inteiro para n: "))
# # Inicialize os dois primeiros números da sequência de Fibonacci
# a, b = 0, 1
# # Inicialize uma variável para contar quantos números já foram gerados
# contador = 0
# # Mostre os primeiros n elementos da sequência de Fibonacci em linhas separadas
# print(f"Os primeiros {n} elementos da sequência de Fibonacci são:")
# while contador < n:
#     print(a)  # Imprime o número atual em uma linha separada
#     a, b = b, a + b  # Calcule o próximo número na sequência
#     contador += 1
################## Desafio 2#################
# Tabuada de multiplicação
# 

########## Desafio 3 #######################
# cálculado com while 
# while True:
#     n1 = float(input("Digite um número "))
#     n2 = float(input("Digite um número "))
#     op = int(input("Escolha uma operação: 1 (soma) 2 (subtração) 3 (multiplicação) 4 (divisão) "))
#     if op == 1:
#         resultado = n1+n2
#         print (resultado)
#     elif op == 2:
#         resultado = n1-n2
#         print (resultado)
#     elif op == 3:
#         resultado = n1*n2
#         print (resultado)
#     elif op == 4:
#         resultado = n1/n2
#         print (resultado)
#     else:
#         print ("O valor não está sendo contemplado!!")
#     fim = int(input(" Qualquer número - Finalizar 2 - Repetir "))
#     if fim == 2:
#         continue
#     else:
#         break
# upper para deixar tudo maiúsculo 
############################## Desafio 4 ############
# while True:
#     nome = str.upper(input("Digite seu nome "))
#     senha = str.upper(input("Digite sua nova senha: "))
#     if senha != nome:
#         print ("Senha aceita!")
#         break
#     else:
#         print ("Senha recusada, tente novamente")
#         continue