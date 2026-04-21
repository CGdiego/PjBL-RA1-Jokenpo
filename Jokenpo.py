import time
import random
import pyfiglet

j1 = 0
nome1 = ""
vJ1 = 0
j2 = 0
nome2 = ""
vJ2 = 0

quantJog = 0
pedra = 0
nomesPedra = ""
papel = 0
nomesPapel = ""
tesoura = 0
nomesTesoura = ""

modalidade = 0
repeat = ""
repeatF = "s"

print(pyfiglet.figlet_format("Jokenpo", font="larry3d")) # Título usando biblioteca "pyfiglet"

print("1. Humano X Humano")
print("2. Humano X Computador")
print("3. Computador X Computador")
print("4. 2v2 (W.I.P. / Alguém faz o 2v2 pfv)")
print("5. Battle Royale (W.I.P.)\n")

while modalidade != "1" and modalidade != "2" and modalidade != "3" and modalidade != "4" and modalidade != "5":
    modalidade = (input("Escolha uma modalidade (1-5): "))
    if modalidade != "1" and modalidade != "2" and modalidade != "3" and modalidade != "4" and modalidade != "5":
        print("Não é uma possibilidade, insira novamente.\n")

print("\033[H\033[J", end="") # Limpa a tela do terminal

if modalidade == "1":
    while repeatF == "s":
        repeat = ""

        while j1 != "1" and j1 != "2" and j1 != "3":
            j1 = input("Jogador 1, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
            if j1 != "1" and j1 != "2" and j1 != "3":
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        while j2 != "1" and j2 != "2" and j2 != "3":
            j2 = input("Jogador 2, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
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
        print("")
        print(pyfiglet.figlet_format("Placar Atual\n", font="chunky")) # Título usando biblioteca "pyfiglet"
        print(f"             O jogador 1 tem {vJ1} ponto(s) atualmente.\n             O jogador 2 tem {vJ2} ponto(s) atualmente.")

        while repeat != "s" and repeat != "n":
            repeat = input("\nGostaria de jogar novamente? (s/n)\n").lower()
            repeatF = repeat
            if repeat == "s":
                j1 = 0
                j2 = 0
                print("\033[H\033[J", end="") # Limpa a tela do terminal
            elif repeat == "n":
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(pyfiglet.figlet_format("Placar Final\n", font="alligator")) # Título usando biblioteca "pyfiglet"
                print(f"          O jogador 1 obteve {vJ1} ponto(s).\n          O jogador 2 obteve {vJ2} ponto(s).")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
            else:
                print("Não é uma possibilidade, insira novamente.")

elif modalidade == "2":
    while repeatF == "s":
        repeat = ""

        while j1 != "1" and j1 != "2" and j1 != "3":
            j1 = input("Jogador, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
            if j1 != "1" and j1 != "2" and j1 != "3":
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        j2 = random.randint(1, 3)
        j2 = str(j2)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("O jogo empatou.")
        elif j1 == "1" and j2 == "2":
            print("O computador venceu!")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("O jogador venceu!")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("O jogo empatou.")
        elif j1 == "2" and j2 == "1":
            print("O jogador venceu!")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("O computador venceu!")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("O jogo empatou.")
        elif j1 == "3" and j2 == "1":
            print("O computador venceu!")
            vJ2 += 1
        else:
            print("O jogador venceu!")
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

        print(f"O jogador escolheu {nome1} e o computador escolheu {nome2}.")
        print("")
        print(pyfiglet.figlet_format("Placar Atual\n", font="chunky")) # Título usando biblioteca "pyfiglet"
        print(f"             O jogador tem {vJ1} ponto(s) atualmente.\n             O computador tem {vJ2} ponto(s) atualmente.")

        while repeat != "s" and repeat != "n":
            repeat = input("\nGostaria de jogar novamente? (s/n)\n").lower()
            repeatF = repeat
            if repeat == "s":
                j1 = 0
                j2 = 0
                print("\033[H\033[J", end="") # Limpa a tela do terminal
            elif repeat == "n":
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(pyfiglet.figlet_format("Placar Final\n", font="alligator")) # Título usando biblioteca "pyfiglet"
                print(f"          O jogador obteve {vJ1} ponto(s).\n          O computador obteve {vJ2} ponto(s).")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
            else:
                print("Não é uma possibilidade, insira novamente.")

elif modalidade == "3":
    while repeatF == "s":
        repeat = ""

        j1 = random.randint(1, 3)
        j1 = str(j1)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        j2 = random.randint(1, 3)
        j2 = str(j2)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("O jogo empatou.")
        elif j1 == "1" and j2 == "2":
            print("O computador 2 venceu!")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("O computador 1 venceu!")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("O jogo empatou.")
        elif j1 == "2" and j2 == "1":
            print("O computador 1 venceu!")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("O computador 2 venceu!")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("O jogo empatou.")
        elif j1 == "3" and j2 == "1":
            print("O computador 2 venceu!")
            vJ2 += 1
        else:
            print("O computador 1 venceu!")
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

        print(f"O computador 1 escolheu {nome1} e o computador 2 escolheu {nome2}.")
        print("")
        print(pyfiglet.figlet_format("Placar Atual\n", font="chunky")) # Título usando biblioteca "pyfiglet"
        print(f"             O computador 1 tem {vJ1} ponto(s) atualmente.\n             O computador 2 tem {vJ2} ponto(s) atualmente.")

        while repeat != "s" and repeat != "n":
            repeat = input("\nGostaria de jogar novamente? (s/n)\n").lower()
            repeatF = repeat
            if repeat == "s":
                j1 = 0
                j2 = 0
                print("\033[H\033[J", end="") # Limpa a tela do terminal
            elif repeat == "n":
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(pyfiglet.figlet_format("Placar Final\n", font="alligator")) # Título usando biblioteca "pyfiglet"
                print(f"          O computador 1 obteve {vJ1} ponto(s).\n          O computador 2 obteve {vJ2} ponto(s).")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
            else:
                print("Não é uma possibilidade, insira novamente.")


# ADICIONAR O 2v2 AQUI!!!!

else:
    while repeatF == "s":
        pedra = 0
        nomesPedra = ""
        papel = 0
        nomesPapel = ""
        tesoura = 0
        nomesTesoura = ""
        quantJog = pedra + papel + tesoura
        j1 = ""
        j2 = ""

        while quantJog <= 1:
            quantJog = int(input("Insira a quantidade de jogadores: "))
            if quantJog <= 1:
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if quantJog > 2:
            for i in range(1, quantJog+1):
                pseudonimo = input("Insira seu nome: ")
                while j1 != "1" and j1 != "2" and j1 != "3":
                    j1 = input(f"\n{pseudonimo}, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
                    if j1 != "1" and j1 != "2" and j1 != "3":
                        print("Não é uma possibilidade, insira novamente.\n")
                
                if j1 == "1":
                    pedra += 1
                    nomesPedra += f"{pseudonimo}, "
                elif j1 == "2":
                    papel += 1
                    nomesPapel += f"{pseudonimo}, "
                else:
                    tesoura += 1
                    nomesTesoura += f"{pseudonimo}, "

                j1 = ""
                
                print("\033[H\033[J", end="") # Limpa a tela do terminal

            if quantJog == pedra or quantJog == papel or quantJog == tesoura:
                print("Apenas um time foi escolhido, todos perdem!")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")

            elif pedra == papel == tesoura:
                print("Todos os times empataram, todos perdem!")
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")

            elif pedra > papel and pedra > tesoura:
                print(f"Pedra domina, logo, as tesouras foram eliminadas: {nomesTesoura}")
                quantJog -= tesoura
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesPapel}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif papel > pedra and papel > tesoura:
                print(f"Papel domina, logo, as pedras foram eliminadas: {nomesPedra}")
                quantJog -= pedra
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPapel}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif tesoura > pedra and tesoura > papel:
                print(f"Tesoura domina, logo, os papéis foram eliminados: {nomesPapel}")
                quantJog -= papel
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif pedra == papel and tesoura != pedra:
                print(f"Pedra e papel empataram, logo, as tesouras foram eliminadas: {nomesTesoura}")
                quantJog -= tesoura
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesPapel}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif papel == tesoura and pedra != papel:
                print(f"Papel e tesoura empataram, logo, as pedras foram eliminadas: {nomesPedra}")
                quantJog -= pedra
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPapel}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif pedra == tesoura and papel != pedra:
                print(f"Pedra e tesoura empataram, logo, os papéis foram eliminados: {nomesPapel}")
                quantJog -= papel
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")
        
        elif quantJog == 2:
            pseudonimo = input("Insira seu nome: ")
            while j1 != "1" and j1 != "2" and j1 != "3":
                j1 = input(f"\n{pseudonimo}, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
                if j1 != "1" and j1 != "2" and j1 != "3":
                    print("Não é uma possibilidade, insira novamente.\n")

            print("\033[H\033[J", end="") # Limpa a tela do terminal

            pseudonimoF = input("Insira seu nome: ")
            while j2 != "1" and j2 != "2" and j2 != "3":
                j2 = input(f"\n{pseudonimoF}, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
                if j2 != "1" and j2 != "2" and j2 != "3":
                    print("Não é uma possibilidade, insira novamente.\n")

            print("\033[H\033[J", end="") # Limpa a tela do terminal

            if j1 == "1" and j2 == "1":
                print("O jogo empatou.")
            elif j1 == "1" and j2 == "2":
                print(f"O {pseudonimoF} venceu!")
            elif j1 == "1" and j2 == "3":
                print(f"O {pseudonimo} venceu!")

            elif j1 == "2" and j2 == "2":
                print("O jogo empatou.")
            elif j1 == "2" and j2 == "1":
                print(f"O {pseudonimo} venceu!")
            elif j1 == "2" and j2 == "3":
                print(f"O {pseudonimoF} venceu!")

            elif j1 == "3" and j2 == "3":
                print("O jogo empatou.")
            elif j1 == "3" and j2 == "1":
                print(f"O {pseudonimoF} venceu!")
            else:
                print(f"O {pseudonimo} venceu!")

        if quantJog > 1:
            repeatF = "s"
        else:
            repeatF = "n"