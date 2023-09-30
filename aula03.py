# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))

# imc = peso/(altura * altura)

# if imc <17:
#     print ("Muito abaixo do peso")
# elif (imc >= 17) and (imc <= 18.49):
#     print ("Abaixo do peso")
# elif (imc >= 18.5) and (imc <= 24.99):
#     print ("Peso normal")
# elif (imc >= 25) and (imc <= 29.99):
#     print ("Acima do peso")
# elif (imc >= 30) and (imc <= 34.99):
#     print ("Obesidade 1")
# elif (imc >= 35) and (imc <= 39.99):
#     print ("Obesidade 2")
# else:
#     print ("Obesidade 3")
#nome = (input("Digite seu nome: "))

# for i in range(0,21,2):
#    print(i)

#print(sum(int(i) for i in range (1,101)))

# soma = 0
# for i in range(1,6): 
#     numero = float(input(f"Digite o número {i}: 5"))
#     soma = soma + numero
#     media= soma // i
# print(media)

nome = str.upper(input("Digite seu nome: "))
con = 0
for letra in nome:
    if letra != "A" and letra != "E" and  letra != "I" and letra != "O" and letra != "U":
        con = con +1
print(f"Tem {con} consoante")

# nome = (input("Digite seu nome: "))
# vogal = "AEIOUaeiou"
# contador = 0
# for letra in nome:
#     if letra in vogal:
#         contador +=1
# print (f"Tem {contador} vogais")


####################################################################################