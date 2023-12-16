import random
#variável global
escolha = 0
escolha_outro = 0
#Função de escolha do usuário (pedra papel tesoura) 
def escolha_user():
    global escolha
    while True:
        escolha = int(input("Escolha: (1 - pedra) (2 - papel) (3 - tesoura) "))
        if escolha == 1 or escolha == 2 or escolha == 3:
            print("Sua escolha é válida!")
            break
        else:
            print("Escolha novamente :(")
            continue
    return (escolha)
#Função aleatória para escolher pedra papel ou tesoura do outro "jogador"
def escolha_pc():
    global escolha_outro
    lista = [1, 2, 3]
    escolha_outro = random.choice(lista)
    if escolha_outro == 1:
        print("Escolha do computador foi pedra.")
    elif escolha_outro == 2:
        print("Escolha do computador foi papel.")
    else:
        print("Escolha do computador foi tesoura.")
    return (escolha_outro)
#Função de comparar qual o jogador ganhou
def compara():
    if (escolha == 1 and escolha_outro ==3) or (escolha == 3 and escolha_outro ==2) or (escolha == 2 and escolha_outro ==1):
        print("Você (jogador 1) venceu!")
    elif (escolha == 3 and escolha_outro ==1) or (escolha == 2 and escolha_outro ==3) or (escolha == 1 and escolha_outro ==2):
        print("Jogador 2 venceu!")    
    else:
        print("Empate")
      
escolha_user()
escolha_pc()
compara()