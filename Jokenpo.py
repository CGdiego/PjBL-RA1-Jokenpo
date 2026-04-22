print("\033[H\033[J", end="") # Limpa a tela do terminal

import time
import random
import pyfiglet
import winsound

musica = random.randint(1, 3)

# if musica == 1:
#     winsound.PlaySound("sounds/music.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
# elif musica == 2:
#     winsound.PlaySound("sounds/music2.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
# else:
#     winsound.PlaySound("sounds/music3.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

j1 = 0
nome1 = ""
vJ1 = 0
j2 = 0
nome2 = ""
vJ2 = 0
j3 = 0
nome3 = ""
j4 = 0
nome4 = ""
equipe1 = ""
equipe2 = ""
vEquipe1 = 0
vEquipe2 = 0

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
print("4. 2v2 (W.I.P.)")
print("5. Battle Royale (W.I.P.)\n")

while modalidade != "1" and modalidade != "2" and modalidade != "3" and modalidade != "4" and modalidade != "5":
    modalidade = (input("Escolha uma modalidade (1-5): "))
    if modalidade != "1" and modalidade != "2" and modalidade != "3" and modalidade != "4" and modalidade != "5":
        print("Não é uma possibilidade, insira novamente.\n")

print("\033[H\033[J", end="") # Limpa a tela do terminal

# Modo Humano X Humano
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

        for i in range(5):
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("   O            O\n  /|\          /|\ \n  / \          / \ ")
            time.sleep(0.2)
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("   O            O\n  /|/          \|\ \n  / \          / \ ")
            time.sleep(0.2)
        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("   O            O\n  /|\✊      ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "1" and j2 == "2":
            print("   O            O\n  /|\✊      🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 2 venceu!\033[0m")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("   O            O\n  /|\✊      ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 1 venceu!\033[0m")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("   O            O\n  /|\🖐️       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "2" and j2 == "1":
            print("   O            O\n  /|\🖐️       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 1 venceu!\033[0m")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("   O            O\n  /|\🖐️       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 2 venceu!\033[0m")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("   O            O\n  /|\✌       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "3" and j2 == "1":
            print("   O            O\n  /|\✌       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 2 venceu!\033[0m")
            vJ2 += 1
        else:
            print("   O            O\n  /|\✌       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador 1 venceu!\033[0m")
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

# Modo Humano X Computador
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

        for i in range(5):
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("   O           📺\n  /|\          /|\ \n  / \          / \ ")
            time.sleep(0.2)
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("   O           📺\n  /|/          \|\ \n  / \          / \ ")
            time.sleep(0.2)
        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("   O           📺\n  /|\✊      ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "1" and j2 == "2":
            print("   O           📺\n  /|\✊      🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador venceu!\033[0m")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("   O           📺\n  /|\✊      ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador venceu!\033[0m")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("   O           📺\n  /|\🖐️       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "2" and j2 == "1":
            print("   O           📺\n  /|\🖐️       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador venceu!\033[0m")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("   O           📺\n  /|\🖐️       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador venceu!\033[0m")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("   O           📺\n  /|\✌       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "3" and j2 == "1":
            print("   O           📺\n  /|\✌       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador venceu!\033[0m")
            vJ2 += 1
        else:
            print("   O           📺\n  /|\✌       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogador venceu!\033[0m")
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

# Modo Computador x Computador
elif modalidade == "3":
    while repeatF == "s":
        repeat = ""

        j1 = random.randint(1, 3)
        j1 = str(j1)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        j2 = random.randint(1, 3)
        j2 = str(j2)

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        for i in range(5):
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("  📺           📺\n  /|\          /|\ \n  / \          / \ ")
            time.sleep(0.2)
            print("\033[H\033[J", end="") # Limpa a tela do terminal
            print("  📺           📺\n  /|/          \|\ \n  / \          / \ ")
            time.sleep(0.2)
        print("\033[H\033[J", end="") # Limpa a tela do terminal

        if j1 == "1" and j2 == "1":
            print("  📺           📺\n  /|\✊      ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "1" and j2 == "2":
            print("  📺           📺\n  /|\✊      🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 2 venceu!\033[0m")
            vJ2 += 1
        elif j1 == "1" and j2 == "3":
            print("  📺           📺\n  /|\✊      ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 1 venceu!\033[0m")
            vJ1 += 1

        elif j1 == "2" and j2 == "2":
            print("  📺           📺\n  /|\🖐️       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "2" and j2 == "1":
            print("  📺           📺\n  /|\🖐️       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 1 venceu!\033[0m")
            vJ1 += 1
        elif j1 == "2" and j2 == "3":
            print("  📺           📺\n  /|\🖐️       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 2 venceu!\033[0m")
            vJ2 += 1

        elif j1 == "3" and j2 == "3":
            print("  📺           📺\n  /|\✌       ✌ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO jogo empatou.\033[0m")
        elif j1 == "3" and j2 == "1":
            print("  📺           📺\n  /|\✌       ✊/|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 2 venceu!\033[0m")
            vJ2 += 1
        else:
            print("  📺           📺\n  /|\✌       🖐️ /|\ \n  / \          / \ ")
            time.sleep(0.5)
            print("\033[1mO computador 1 venceu!\033[0m")
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

# Modo 2v2
elif modalidade == "4":
    while repeatF == "s":
        j1 = 0
        j2 = 0
        j3 = 0
        j4 = 0

        print("TIME 1")

        while j1!="1" and j1!="2" and j1!="3":
            j1 = input("J1 escolha (1 Pedra 2 Papel 3 Tesoura): ")
        alvoJ1 = ""
        while alvoJ1 != "1" and alvoJ1 != "2":
            alvoJ1 = input("J1 ataca (1)J3 ou (2)J4: ")
            if alvoJ1 != "1" and alvoJ1 != "2":
                print("Não é uma possibilidade, insira novamente.")
        print("\033[H\033[J", end="")

        while j2!="1" and j2!="2" and j2!="3":
            j2 = input("J2 escolha (1 Pedra 2 Papel 3 Tesoura): ")
        alvoJ2 = ""
        while alvoJ2 != "1" and alvoJ2 != "2":
            alvoJ2 = input("J2 ataca (1)J3 ou (2)J4: ")
            if alvoJ2 != "1" and alvoJ2 != "2":
                print("Não é uma possibilidade, insira novamente.")
        print("\033[H\033[J", end="")

        print("TIME 2")

        while j3!="1" and j3!="2" and j3!="3":
            j3 = input("J3 escolha (1 Pedra 2 Papel 3 Tesoura): ")
        alvoJ3 = ""
        while alvoJ3 != "1" and alvoJ3 != "2":
            alvoJ3 = input("J3 ataca (1)J1 ou (2)J2: ")
            if alvoJ3 != "1" and alvoJ3 != "2":
                print("Não é uma possibilidade, insira novamente.")
        print("\033[H\033[J", end="")

        while j4!="1" and j4!="2" and j4!="3":
            j4 = input("J4 escolha (1 Pedra 2 Papel 3 Tesoura): ")
        alvoJ4 = ""
        while alvoJ4 != "1" and alvoJ4 != "2":
            alvoJ4 = input("J4 ataca (1)J1 ou (2)J2: ")
            if alvoJ4 != "1" and alvoJ4 != "2":
                print("Não é uma possibilidade, insira novamente.")
        print("\033[H\033[J", end="")

        vivoJ1 = True
        vivoJ2 = True
        vivoJ3 = True
        vivoJ4 = True

        # J1 escolhe quem ataca
        if alvoJ1 == "1":
            if j1 != j3 and not ((j1=="1" and j3=="3") or (j1=="2" and j3=="1") or (j1=="3" and j3=="2")):
                vivoJ1 = False
            elif (j1=="1" and j3=="3") or (j1=="2" and j3=="1") or (j1=="3" and j3=="2"):
                vivoJ3 = False
        else:
            if j1 != j4 and not ((j1=="1" and j4=="3") or (j1=="2" and j4=="1") or (j1=="3" and j4=="2")):
                vivoJ1 = False
            elif (j1=="1" and j4=="3") or (j1=="2" and j4=="1") or (j1=="3" and j4=="2"):
                vivoJ4 = False

        # J2 escolhe quem ataca
        if alvoJ2 == "1":
            if j2 != j3 and not ((j2=="1" and j3=="3") or (j2=="2" and j3=="1") or (j2=="3" and j3=="2")):
                vivoJ2 = False
            elif (j2=="1" and j3=="3") or (j2=="2" and j3=="1") or (j2=="3" and j3=="2"):
                vivoJ3 = False
        else:
            if j2 != j4 and not ((j2=="1" and j4=="3") or (j2=="2" and j4=="1") or (j2=="3" and j4=="2")):
                vivoJ2 = False
            elif (j2=="1" and j4=="3") or (j2=="2" and j4=="1") or (j2=="3" and j4=="2"):
                vivoJ4 = False

        # J3 escolhe quem ataca
        if alvoJ3 == "1":
            if j3 != j1 and not ((j3=="1" and j1=="3") or (j3=="2" and j1=="1") or (j3=="3" and j1=="2")):
                vivoJ3 = False
            elif (j3=="1" and j1=="3") or (j3=="2" and j1=="1") or (j3=="3" and j1=="2"):
                vivoJ1 = False
        else:
            if j3 != j2 and not ((j3=="1" and j2=="3") or (j3=="2" and j2=="1") or (j3=="3" and j2=="2")):
                vivoJ3 = False
            elif (j3=="1" and j2=="3") or (j3=="2" and j2=="1") or (j3=="3" and j2=="2"):
                vivoJ2 = False

        # J4 escolhe quem ataca
        if alvoJ4 == "1":
            if j4 != j1 and not ((j4=="1" and j1=="3") or (j4=="2" and j1=="1") or (j4=="3" and j1=="2")):
                vivoJ4 = False
            elif (j4=="1" and j1=="3") or (j4=="2" and j1=="1") or (j4=="3" and j1=="2"):
                vivoJ1 = False
        else:
            if j4 != j2 and not ((j4=="1" and j2=="3") or (j4=="2" and j2=="1") or (j4=="3" and j2=="2")):
                vivoJ4 = False
            elif (j4=="1" and j2=="3") or (j4=="2" and j2=="1") or (j4=="3" and j2=="2"):
                vivoJ2 = False

        print("\nMortos:")
        if not vivoJ1: print("J1 morreu")
        if not vivoJ2: print("J2 morreu")
        if not vivoJ3: print("J3 morreu")
        if not vivoJ4: print("J4 morreu")

        time1_vivos = vivoJ1 + vivoJ2
        time2_vivos = vivoJ3 + vivoJ4

        if time1_vivos > time2_vivos:
            print("\033[1mTIME 1 venceu\033[0m")
            vEquipe1 += 1
        elif time2_vivos > time1_vivos:
            print("\033[1mTIME 2 venceu\033[0m")
            vEquipe2 += 1
        else:
            print("\033[1mEmpate\033[0m")

        repeatF = input("\nOutra rodada? (s/n): ")
    else:
        print("\033[H\033[J", end="") # Limpa a tela do terminal
        print(pyfiglet.figlet_format("Placar Final\n", font="alligator")) # Título usando biblioteca "pyfiglet"
        print(f"          A equipe 1 obteve {vEquipe1} ponto(s).\n          A equipe 2 obteve {vEquipe2} ponto(s).")
        time.sleep(5)
        print("\033[H\033[J", end="") # Limpa a tela do terminal
        print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")
    


# Modo Battle Royale
else:
    while repeatF == "s":
        nomesPedra = ""
        nomesPapel = ""
        nomesTesoura = ""
        quantJog = pedra + papel + tesoura
        pedra = 0
        papel = 0
        tesoura = 0
        j1 = ""
        j2 = ""

        while quantJog <= 1:
            quantJog = int(input("Insira a quantidade de jogadores: "))
            if quantJog <= 1:
                print("Não é uma possibilidade, insira novamente.\n")

        print("\033[H\033[J", end="") # Limpa a tela do terminal

        # Quando tiver mais que dois jogadores
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
                print("Apenas um time foi escolhido, nada acontece. :(")

            elif pedra == papel == tesoura:
                print("Todos os times empataram, nada acontece. :(")

            elif pedra > papel and pedra > tesoura:
                print(f"Pedra domina, logo, {tesoura} tesoura(s) foram eliminadas: {nomesTesoura}")
                quantJog -= tesoura
                tesoura = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesPapel}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif papel > pedra and papel > tesoura:
                print(f"Papel domina, logo, {pedra} pedra(s) foram eliminadas: {nomesPedra}")
                quantJog -= pedra
                pedra = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPapel}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif tesoura > pedra and tesoura > papel:
                print(f"Tesoura domina, logo, {papel} papel(éis) foram eliminados: {nomesPapel}")
                quantJog -= papel
                papel = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif pedra == papel and tesoura != pedra:
                print(f"Pedra e papel empataram, logo, {tesoura} tesoura(s) foram eliminadas: {nomesTesoura}")
                quantJog -= tesoura
                tesoura = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesPapel}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif papel == tesoura and pedra != papel:
                print(f"Papel e tesoura empataram, logo, {pedra} pedra(s) foram eliminadas: {nomesPedra}")
                quantJog -= pedra
                pedra = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPapel}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")

            elif pedra == tesoura and papel != pedra:
                print(f"Pedra e tesoura empataram, logo, {papel} papel(éis) foram eliminados: {nomesPapel}")
                quantJog -= papel
                papel = 0
                time.sleep(5)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print(f"Os sobreviventes são: {nomesPedra}, {nomesTesoura}.")
                repeat = input("\nDigite qualquer coisa para ir para a próxima rodada.\n")
        
        # Quando restarem apenas 2 jogadores
        elif quantJog == 2:
            pseudonimo = input("Insira seu nome: ")
            while j1 != "1" and j1 != "2" and j1 != "3":
                j1 = input(f"\n{pseudonimo}, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
                if j1 != "1" and j1 != "2" and j1 != "3":
                    print("Não é uma possibilidade, insira novamente.\n")

            if j1 == "1":
                pedra += 1
            elif j1 == "2":
                papel += 1
            else:
                tesoura += 1

            print("\033[H\033[J", end="") # Limpa a tela do terminal

            pseudonimoF = input("Insira seu nome: ")
            while j2 != "1" and j2 != "2" and j2 != "3":
                j2 = input(f"\n{pseudonimoF}, escolha:\n'1' - Pedra\n'2' - Papel\n'3' - Tesoura\n")
                if j2 != "1" and j2 != "2" and j2 != "3":
                    print("Não é uma possibilidade, insira novamente.\n")

            if j2 == "1":
                pedra += 1
            elif j2 == "2":
                papel += 1
            else:
                tesoura += 1

            print("\033[H\033[J", end="") # Limpa a tela do terminal

            for i in range(5):
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("   O            O\n  /|\          /|\ \n  / \          / \ ")
                time.sleep(0.2)
                print("\033[H\033[J", end="") # Limpa a tela do terminal
                print("   O            O\n  /|/          \|\ \n  / \          / \ ")
                time.sleep(0.2)
            print("\033[H\033[J", end="") # Limpa a tela do terminal

            if j1 == "1" and j2 == "1":
                print("   O            O\n  /|\✊      ✊/|\ \n  / \          / \ \n")
                time.sleep(0.5)
                print("O jogo empatou.")
                time.sleep(3)
            elif j1 == "1" and j2 == "2":
                print("   O            O\n  /|\✊      🖐️ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimoF
            elif j1 == "1" and j2 == "3":
                print("   O            O\n  /|\✊      ✌ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimo

            elif j1 == "2" and j2 == "2":
                print("   O            O\n  /|\🖐️       🖐️ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                print("O jogo empatou.")
                time.sleep(3)
            elif j1 == "2" and j2 == "1":
                print("   O            O\n  /|\🖐️       ✊/|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimo
            elif j1 == "2" and j2 == "3":
                print("   O            O\n  /|\🖐️       ✌ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimoF

            elif j1 == "3" and j2 == "3":
                print("   O            O\n  /|\✌       ✌ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                print("O jogo empatou.")
                time.sleep(3)
            elif j1 == "3" and j2 == "1":
                print("   O            O\n  /|\✌       ✊/|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimoF
            else:
                print("   O            O\n  /|\✌       🖐️ /|\ \n  / \          / \ \n")
                time.sleep(0.5)
                quantJog = 1
                vencedor = pseudonimo

        if quantJog > 1:
            repeatF = "s"
        else:
            repeatF = "n"
    
    print(pyfiglet.figlet_format("Victory Royale!", font="big_money-ne")) # Título usando biblioteca "pyfiglet"
    print(f"\033[1m{vencedor}\033[0m")
    time.sleep(5)
    print("\033[H\033[J", end="") # Limpa a tela do terminal
    print("Muito obrigado por jogar!\nFeito por Daniel Godri, Diego Soares e João Victor M. B.")