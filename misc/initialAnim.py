import time
import random

while True:
    for i in range(3):
        print("\033[H\033[J", end="") # Limpa a tela do terminal
        print("   O            O\n  /|\          /|\ \n  / \          / \ ")
        time.sleep(0.2)
        print("\033[H\033[J", end="") # Limpa a tela do terminal
        print("   O            O\n  /|/          \|\ \n  / \          / \ ")
        time.sleep(0.2)
    print("\033[H\033[J", end="") # Limpa a tela do terminal

    rand = random.randint(1, 9)

    if rand == 1:
        print("   O            O\n  /|\✊      ✊/|\ \n  / \          / \ ")
    elif rand == 2:
        print("   O            O\n  /|\✊      🖐️ /|\ \n  / \          / \ ")
    elif rand == 3:
        print("   O            O\n  /|\✊      ✌ /|\ \n  / \          / \ ")
    elif rand == 4:
        print("   O            O\n  /|\🖐️       🖐️ /|\ \n  / \          / \ ")
    elif rand == 5:
        print("   O            O\n  /|\🖐️       ✊/|\ \n  / \          / \ ")
    elif rand == 6:
        print("   O            O\n  /|\🖐️       ✌ /|\ \n  / \          / \ ")
    elif rand == 7:
        print("   O            O\n  /|\✌       ✌ /|\ \n  / \          / \ ")
    elif rand == 8:
        print("   O            O\n  /|\✌       ✊/|\ \n  / \          / \ ")
    else:
        print("   O            O\n  /|\✌       🖐️ /|\ \n  / \          / \ ")

    time.sleep(1)