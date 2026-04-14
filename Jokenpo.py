import random
j1 = 0
j2 = 0

print("Bem vindo ao Jokenpô!\n")

print("1. Humano X Humano")
print("2. Humano X Computador")
print("3. Computador X Computador")
print("4. Secreto1")
print("5. Secreto2\n")

modalidade = int(input("Escolha uma modalidade (1-5): "))

print("\033[H\033[J", end="") # Limpa a tela do terminal

if modalidade == 1:
    while j1 != "pedra" and j1 != "papel" and j1 != "tesoura":
        j1 = input("Jogador 1, escolha 'pedra', 'papel', ou 'tesoura': ").lower()
        if j1 != "pedra" or j1 != "papel" or j1 != "tesoura":
            print("Não é uma possibilidade, insira novamente.\n")

    print("\033[H\033[J", end="") # Limpa a tela do terminal

    while j2 != "pedra" and j2 != "papel" and j2 != "tesoura":
        j2 = input("Jogador 2, escolha 'pedra', 'papel', ou 'tesoura': ").lower()
        if j2 != "pedra" or j2 != "papel" or j2 != "tesoura":
            print("Não é uma possibilidade, insira novamente.\n")

    print("\033[H\033[J", end="") # Limpa a tela do terminal

    if j1 == "pedra" and j2 == "pedra":
        print("O jogo empatou.")
    elif j1 == "pedra" and j2 == "papel":
        print("O jogador 2 venceu!")
    elif j1 == "pedra" and j2 == "tesoura":
        print("O jogador 1 venceu!")

    elif j1 == "papel" and j2 == "papel":
        print("O jogo empatou.")
    elif j1 == "papel" and j2 == "pedra":
        print("O jogador 1 venceu!")
    elif j1 == "papel" and j2 == "tesoura":
        print("O jogador 2 venceu!")

    elif j1 == "tesoura" and j2 == "tesoura":
        print("O jogo empatou.")
    elif j1 == "tesoura" and j2 == "pedra":
        print("O jogador 2 venceu!")
    elif j1 == "tesoura" and j2 == "papel":
        print("O jogador 1 venceu!")