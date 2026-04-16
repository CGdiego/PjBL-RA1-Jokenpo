import time
import random
import pyfiglet
j1 = 0
nome1 = ""
vJ1 = 0
j2 = 0
nome2 = ""
vJ2 = 0
modalidade = 0
repeat = ""
repeatF = "s"

print(pyfiglet.figlet_format("Jokenpo", font="larry3d")) # Título usando biblioteca "pyfiglet"

print("1. Humano X Humano")
print("2. Humano X Computador")
print("3. Computador X Computador")
print("4. Secreto1")
print("5. Secreto2\n")

while modalidade < 1 or modalidade > 5:
    modalidade = int(input("Escolha uma modalidade (1-5): "))
    if modalidade < 1 or modalidade > 5:
        print("Não é uma possibilidade, insira novamente.\n")

print("\033[H\033[J", end="") # Limpa a tela do terminal

if modalidade == 1:
    while repeatF == "s":
        repeat = ""
        while j1 != "1" and j1 != "2" and j1 != "3":
            j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n").lower()
            if j1 != "1" and j1 != "2" and j1 != "3":
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        while j2 != "1" and j2 != "2" and j2 != "3":
            j2 = input("Jogador 2, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n").lower()
            if j2 != "1" and j2 != "2" and j2 != "3":
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("O jogo empatou.")
        elif j1 == "1" and j2 == "2":
            print("O jogador 2 venceu!")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("O jogador 1 venceu!")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("O jogo empatou.")
        elif j1 == "2" and j2 == "1":
            print("O jogador 1 venceu!")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("O jogador 2 venceu!")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("O jogo empatou.")
        elif j1 == "3" and j2 == "1":
            print("O jogador 2 venceu!")
            vJ2 += 1
        else:
            print("O jogador 1 venceu!")
            vJ1 += 1

        if j1 == "1":
            nome1 = "pedra"
        elif j1 == "2":
            nome1 = "papel"
        else:
            nome1 = "tesoura"

        if j2 == "1":
            nome2 = "pedra"
        elif j2 == "2":
            nome2 = "papel"
        else:
            nome2 = "tesoura"

        print(f"O jogador 1 escolheu {nome1} e o jogador 2 escolheu {nome2}.")

        while repeat != "s" and repeat != "n":
            repeat = input("\nGostaria de jogar novamente? (s/n)\n").lower()
            repeatF = repeat
            if repeat == "s":
                j1 = 0
                j2 = 0
                print("\033[H\033[J", end="") # Limpa a tela do terminal
            elif repeat == "n":
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(pyfiglet.figlet_format("Placar\n", font="alligator")) # Título usando biblioteca "pyfiglet"
                print(f"               O jogador 1 obteve {vJ1} pontos.\n               O jogador 2 obteve {vJ2} pontos.")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
            else:
                print("Não é uma possibilidade, insira novamente.")

if modalidade == 2:
    while repeatF == "s":
        repeat = ""
        while j1 != "1" and j1 != "2" and j1 != "3":
            j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n").lower()
            if j1 != "1" and j1 != "2" and j1 != "3":
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        j2 = random.randint(1, 3)
        j2 = str(j2)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("O jogo empatou.")
        elif j1 == "1" and j2 == "2":
            print("O jogador 2 venceu!")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("O jogador 1 venceu!")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("O jogo empatou.")
        elif j1 == "2" and j2 == "1":
            print("O jogador 1 venceu!")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("O jogador 2 venceu!")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("O jogo empatou.")
        elif j1 == "3" and j2 == "1":
            print("O jogador 2 venceu!")
            vJ2 += 1
        else:
            print("O jogador 1 venceu!")
            vJ1 += 1

        if j1 == "1":
            nome1 = "pedra"
        elif j1 == "2":
            nome1 = "papel"
        else:
            nome1 = "tesoura"

        if j2 == "1":
            nome2 = "pedra"
        elif j2 == "2":
            nome2 = "papel"
        else:
            nome2 = "tesoura"

        print(f"O jogador 1 escolheu {nome1} e o jogador 2 escolheu {nome2}.")

        while repeat != "s" and repeat != "n":
            repeat = input("\nGostaria de jogar novamente? (s/n)\n").lower()
            repeatF = repeat
            if repeat == "s":
                j1 = 0
                j2 = 0
                print("\033[H\033[J", end="") # Limpa a tela do terminal
            elif repeat == "n":
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(pyfiglet.figlet_format("Placar\n", font="alligator")) # Título usando biblioteca "pyfiglet"
                print(f"               O jogador 1 obteve {vJ1} pontos.\n               O jogador 2 obteve {vJ2} pontos.")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
            else:
                print("Não é uma possibilidade, insira novamente.")