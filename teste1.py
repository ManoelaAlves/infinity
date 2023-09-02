# nome_completo = str(input("Qual seu nome completo? "))
# sobrenome = str(input("Qual seu sobrenome? "))
# idade2 = int(input("Qual sua idade da sua mãe? "))
# idade = int(input("Qual sua idade? "))
# altura = float(input("Qual sua altura? "))
# print(f"Olá,{nome_completo}!")
# print(f"Sua idade é {idade} e sua altura é {altura}!")
# print(f"A idade da sua mãe é {idade2}!")
##############################################
#Operadores
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))
if numero_1>numero_2:
    soma = numero_1+numero_2
    print(soma)
elif numero_2>numero_1:
    sub= numero_2-numero_1
    print(sub)
else:
    neutro= numero_1*numero_2
    print(neutro)
#################################################
numero_1 = int(input("Qual ano vc nasceu? "))
numero_2 = 2023
idade = numero_2-numero_1
print(f"Sua idade é {idade}")